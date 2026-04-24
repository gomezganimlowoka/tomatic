# 🍅 Tomatic — Tomato Disease Detection Web App

Tomatic is a Flask-based web application that uses machine learning to detect diseases in tomato plants. Users can upload an image of a tomato leaf, and the app predicts whether the plant is healthy or affected by a disease.

---

## Features

- Upload a tomato leaf image through a simple web interface
- Automatic disease classification using a trained ML model
- Clean, responsive front-end built with HTML, CSS, and JavaScript
- Lightweight Flask backend

---

## Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python, Flask           |
| Frontend   | HTML, CSS, JavaScript   |
| ML Model   | TensorFlow / Keras (CNN)|

---

## Project Structure

```
tomatic/
├── app/
│   ├── __init__.py        # App factory (create_app)
│   ├── routes.py          # URL routes and view logic
│   ├── model/             # Trained ML model files
│   ├── static/            # CSS, JS, images
│   └── templates/         # HTML templates
├── app.py                 # Entry point
├── requirements.txt       # Python dependencies
├── .gitignore
└── LICENSE
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/gomezganimlowoka/tomatic.git
cd tomatic
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

5. **Open in your browser**

```
http://127.0.0.1:5000
```

---

## Usage

1. Navigate to the home page.
2. Upload a clear image of a tomato leaf.
3. Click **Detect** to submit the image.
4. View the predicted disease name and recommended action.

---

## Disease Classes

The model can identify common tomato leaf conditions, including:

- Bacterial Spot
- Early Blight
- Late Blight
- Leaf Mold
- Septoria Leaf Spot
- Spider Mites
- Target Spot
- Tomato Mosaic Virus
- Tomato Yellow Leaf Curl Virus
- Healthy

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Author

**Gomezgani Mlowoka**  
Data Analysis · Machine Learning · Web & Mobile Applications  
