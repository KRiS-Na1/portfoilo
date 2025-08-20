import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY = "Krishna@2001"  # For CSRF protection
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "kkc11669@gmail.com"  # Gmail
    MAIL_PASSWORD = "zgya jtmo tqvw zzhk"   # Gmail App Password
    MAIL_DEFAULT_SENDER = ("Message from Portfolio", MAIL_USERNAME)

  