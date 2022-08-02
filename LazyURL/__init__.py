from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .Database.db import db
from os import environ

from .Routes.main import lazy_index
load_dotenv()
database_uri = environ.get('DATABASE_URL')

app = Flask(__name__)

app.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')
)

CORS(app)

db.app = app
db.init_app(app)



app.register_blueprint(lazy_index)

if __name__ == '__main__':
    app.run(debug=True)