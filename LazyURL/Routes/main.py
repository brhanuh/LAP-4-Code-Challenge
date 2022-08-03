from flask import Blueprint, redirect, render_template, request
from .short_api.api import api_shorten
from ..Database.db import db
from ..Models.lazy import LazyUrl
lazy_index = Blueprint("main", __name__)

@lazy_index.route("/", methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        print(request.form['url'])
        long_url = request.form['url']
        missing = LazyUrl.query.filter_by(original_url=long_url).first()
        short_url = api_shorten(long_url)
        if missing is None:
            new_url = LazyUrl(original_url=long_url, short_url=short_url)
            db.session.add(new_url)
            db.session.commit()
        
        short = f"https://fp-lazyurl.herokuapp.com/{short_url}"
        return render_template("index.html", short_url=short)
    else:
        return render_template("index.html")

@lazy_index.route("/<short>", methods=['GET'])
def handle_url(short):
    print(short)
    url = LazyUrl.query.filter_by(short_url=short).first()
    if url is None:
        return redirect("/")
    else:
        original_url = url.original_url
        return redirect(original_url)