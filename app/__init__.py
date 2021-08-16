from flask import Flask
from flask_bootsrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet,configure_uploads,IMAGES