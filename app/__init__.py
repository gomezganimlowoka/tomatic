from flask import Flask
from flask_mail import Mail

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    from .routes import main
    mail.init_app(app)
    app.register_blueprint(main)
    return app