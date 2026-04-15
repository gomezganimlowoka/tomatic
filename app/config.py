# config.py
class Config:
    MAIL_SERVER = 'smtp.gmail.com'       # or your SMTP provider
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your@gmail.com'     # sender email
    MAIL_PASSWORD = 'your_app_password'  # use an App Password, not your real one
    MAIL_DEFAULT_SENDER = 'your@gmail.com'
    CONTACT_MAIL_RECIPIENT = 'your@gmail.com'  # where to receive messages