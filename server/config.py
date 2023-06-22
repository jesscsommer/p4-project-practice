from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

app = Flask(__name__)

# SET UP APP SECRET KEY HERE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bookish.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False 

# naming convention & metadata updates 
db = SQLAlchemy()

migrate = Migrate(app, db)
db.init_app(app)

bcrypt = Bcrypt(app)

api = Api(app)