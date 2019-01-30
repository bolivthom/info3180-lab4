import os
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__, static_url_path='/static')
app.config.from_object(__name__)

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])
UPLOAD_FOLDER = './app/static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app import views