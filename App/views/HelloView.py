import base64
import os
import random
import time

from flask import Blueprint, render_template, request

from App.ext import db
from App.models import News
from App.settings import BASE_DIR

blue = Blueprint("blue", __name__, template_folder='../../templates')


@blue.route('/')
def hello_world():
    return 'Hello World!'


@blue.route('/addnews/')
def add_news():
    news = News()
    news.n_title = "周润发%d" % random.randrange(10000)

    news.n_content = "福利社会%d" % random.randrange(200000)

    db.session.add(news)
    db.session.commit()

    return "Add success"


@blue.route('/getnews/')
def get_news():
    news_list = News.query.all()
    news_content = render_template("NewsContent.html", news_list=news_list)

    encode_content = base64.standard_b64encode(news_content.encode("utf-8")).decode("utf-8")
    # print(encode_content)

    add_content_encode_content = "JIUOHhjisha2327HJKHksjk" + encode_content + "sdHJH8728HJKHDhjsh67"
    # print(add_content_encode_content)
    encode_content_twice = base64.standard_b64encode(add_content_encode_content.encode("utf-8")).decode("utf-8")
    # print(encode_content_twice)
    return render_template('NewsList.html', news_content=news_content, encode_content_twice=encode_content_twice)


@blue.route('/getshows/')
def get_shows():

    timestap = request.args.get("t")
    print(timestap)

    c = time.time()*1000
    print(c)
    try:
        timestap = int(timestap)
    except:
        return "2"

    if c > timestap and c - timestap < 1000:
        with open(os.path.join(BASE_DIR, 'App/static/js/shows.js')) as fp:
            js_content = fp.read()
    else:
        return "1"

    return js_content
