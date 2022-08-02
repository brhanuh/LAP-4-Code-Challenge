from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .Database.db import db
from os import environ
from werkzeug import exceptions

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

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {"message": f"Ooops...{err}"}, 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {"message": f"Ooops...{err}"}, 500
@app.errorhandler(exceptions.MethodNotAllowed)
def handle_405(err):
    return {"message": f"Oooops...{err}"}, 405

if __name__ == '__main__':
    app.run(debug=True)