import logging
import sys
import os
from flask import Blueprint, request, jsonify, render_template, current_app, url_for
import tensorflow as tf
import numpy as np
from PIL import Image
from werkzeug.utils import secure_filename
import uuid
import locale

# Configure logging
logging.basicConfig(level=logging.INFO)

# Add a StreamHandler with UTF-8 encoding for Windows console
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# Remove all existing handlers and add the new handler
logging.getLogger().handlers = []
logging.getLogger().addHandler(handler)

# Set up Flask Blueprint
main = Blueprint('main', __name__)

# Load the model (use os.path for cross-platform compatibility)
#MODEL_PATH = MODEL_PATH = 'tomato-disease-flask/app/models/fine_Tomato_disease.keras'
MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models', 'Tomato_disease_mobilenetv2_model.keras')


try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    logging.info("Model loaded successfully with compile=False")
except Exception as e:
    logging.error(f"Failed to load model: {e}")
    model = None

# Class labels
class_labels = {
    0: "Bacterial_spot",
    1: "Early_blight",
    2: "Late_blight",
    3: "Leaf_Mold",
    4: "Septoria_leaf_spot",
    5: "Spider_mites Two-spotted_spider_mite",
    6: "Target_Spot",
    7: "Tomato_Yellow_Leaf_Curl_Virus",
    8: "Tomato_mosaic_virus",
    9: "healthy",
    10: "powdery_mildew"
}

disease_info = {
    "Bacterial_spot": {
        "cause": "Caused by the bacterium Xanthomonas campestris pv. vesicatoria.",
        "prevention": "Use disease-free seeds, rotate crops, and apply copper-based bactericides."
    },
    "Early_blight": {
        "cause": "Caused by the fungus Alternaria solani.",
        "prevention": "Remove infected plant debris, use resistant varieties, and apply fungicides."
    },
    "Late_blight": {
        "cause": "Caused by the oomycete Phytophthora infestans.",
        "prevention": "Avoid overhead watering, remove infected plants, and use fungicides."
    },
    "Leaf_Mold": {
        "cause": "Caused by the fungus Passalora fulva.",
        "prevention": "Improve air circulation, avoid wetting leaves, and apply fungicides."
    },
    "Septoria_leaf_spot": {
        "cause": "Caused by the fungus Septoria lycopersici.",
        "prevention": "Remove infected leaves, rotate crops, and apply fungicides."
    },
    "Spider_mites Two-spotted_spider_mite": {
        "cause": "Caused by the mite Tetranychus urticae.",
        "prevention": "Use miticides, encourage natural predators, and avoid plant stress."
    },
    "Target_Spot": {
        "cause": "Caused by the fungus Corynespora cassiicola.",
        "prevention": "Remove plant debris, rotate crops, and apply fungicides."
    },
    "Tomato_Yellow_Leaf_Curl_Virus": {
        "cause": "Caused by Tomato yellow leaf curl virus transmitted by whiteflies.",
        "prevention": "Control whiteflies, use resistant varieties, and remove infected plants."
    },
    "Tomato_mosaic_virus": {
        "cause": "Caused by Tomato mosaic virus.",
        "prevention": "Use virus-free seeds, disinfect tools, and remove infected plants."
    },
    "healthy": {
        "cause": "No disease detected.",
        "prevention": "Maintain good cultural practices to keep plants healthy."
    },
    "powdery_mildew": {
        "cause": "Caused by several fungal species including Oidium neolycopersici.",
        "prevention": "Improve air circulation, avoid overcrowding, apply sulfur or potassium bicarbonate fungicides."
    }
}


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@main.route('/')
def index():
    return render_template('index.html')

@main.route('/predict_page')
def show_predict_page():
    return render_template('predict.html')

@main.route('/service')
def show_service_page():
    return render_template('service.html')

# @main.route('/predict')
# def show_predict_page():
#     return render_template('predict.html')

@main.route('/about')
def about_page():
    return render_template('about.html')

@main.route('/contacts')
def contacts_page():
    return render_template('contact.html')

@main.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        logging.error("No file part in the request")
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    if file.filename == '':
        logging.error("No selected file")
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        logging.error("File type not allowed")
        return jsonify({'error': 'File type not allowed'}), 400

    try:
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        upload_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, unique_filename)
        file.save(file_path)

        # Fix for encoding error in logging
        try:
            with open(file_path, 'rb') as f:
                img = Image.open(f)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img = img.resize((224, 224))
                img_array = np.array(img)
                img_array = np.expand_dims(img_array, axis=0)
        except Exception as img_e:
            logging.error(f"Image processing error: {str(img_e)}")
            return jsonify({
                'error': 'Failed to process the image',
                'details': str(img_e)
            }), 500

        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)[0]
        predicted_label = class_labels.get(predicted_class, "Unknown")

        logging.info(f"Prediction: {predicted_label}")

        info = disease_info.get(predicted_label, {"cause": "Unknown", "prevention": "Unknown"})

        return jsonify({
            'predicted_class': int(predicted_class),
            'predicted_label': predicted_label,
            'cause': info["cause"],
            'prevention': info["prevention"],
            'uploaded_file_url': url_for('static', filename=f'uploads/{unique_filename}')
        })

    except Exception as e:
        # Fix for encoding error in logging
        try:
            error_message = str(e).encode('utf-8', errors='replace').decode('utf-8')
        except Exception:
            error_message = 'Unknown error'
        logging.error(f"Prediction error: {error_message}")
        return jsonify({
            'error': 'Failed to process the image or make prediction',
            'details': error_message
        }), 500
