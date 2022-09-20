from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'


# config database
file_dir = os.path.dirname(__file__)
db_dir = os.path.join(file_dir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + db_dir
db = SQLAlchemy(app)

import models
import views

