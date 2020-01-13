from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import String, Integer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scott:tiger@localhost:5432/test123'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)