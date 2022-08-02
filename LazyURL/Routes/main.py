from flask import Blueprint

lazy_index = Blueprint("main", __name__)

@lazy_index.route("/")
def welcome():
    return "Hello world"