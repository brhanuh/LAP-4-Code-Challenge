from flask import Blueprint, render_template, request
from .short_api.api import api_shorten

lazy_index = Blueprint("main", __name__)

@lazy_index.route("/", methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        print(request.form['url'])
        long_url = request.form['url']
        api_shorten(long_url)
    else:
        print("else post")
    return render_template("index.html")