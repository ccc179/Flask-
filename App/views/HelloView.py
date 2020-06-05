import base64
import hashlib
import os
import random
import time

import requests
from flask import Blueprint, render_template, request, g, current_app, redirect, url_for, flash, jsonify
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db, mail, cache
from App.models import News, Student
from App.settings import BASE_DIR
from doc.code.SendSMS import send_varify_code

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
    print("第一个请求,当前视图中的请求")
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
    print("当前视图的外链请求", timestap)

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
        return "1 %s" % g.msg

    return js_content


# @blue.before_request
# def before_re():
#     print("更超前的请求", request.url)
#     g.msg = "wode maya"
#
#     config = current_app.config
#     print(config)
#     print("*"*50)
#     keys = config.keys()
#     for k in config:
#         print(k, config[k])


# @blue.after_request
# def after_re(resp):
#     print("after")
#     print(resp)
#     print(type(resp))
#
#     return resp


@blue.route('/student/register/', methods=["GET", "POST"])
def student_register():
    if request.method == "GET":
        return render_template("StudentRegister.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        phone = request.form.get("phone")
        code = request.form.get("code")

        # hash_pwd = generate_password_hash(password)
        if code != cache.get("username"):
            return "验证码错误"
        student = Student()
        student.s_name = username
        student.s_password = password
        student.s_phone = phone

        db.session.add(student)
        db.session.commit()
        return "Register Success"


@blue.route('/student/login/', methods=["GET", "POST"])
def student_login():
    if request.method == "GET":
        return render_template("StudentLogin.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        student = Student.query.filter(Student.s_name.__eq__(username)).first()
            # 会不会报错??

        if student and student.check_password(password):
            # request.user = student

            return "登录成功"
        flash("用户名或密码错误")

        return redirect(url_for("blue.student_login"))


@blue.route('/sendmail/')
def send_mail():
    msg = Message("Flask email", recipients=["5700102@qq.com", ], body="<h2>哈哈哈哈 我是一个来自FLask的邮件1body</h2>",
                  html="<h2>哈哈哈哈 我是一个来自FLask的邮件2html</h2>")
    # msg.body = "<h2>哈哈哈哈 我是一个来自FLask的邮件1body</h2>"
    # msg.html = "<h2>哈哈哈哈 我是一个来自FLask的邮件2html</h2>"

    mail.send(message=msg)

    return "邮件发送成功"


@blue.route('/sendcode/<string:phone>/')
def send_code(phone):
    # 调用send_varify_code模块连接短信平台,发送验证码,返回的是一个json响应
    resp = send_varify_code(phone)
    # 从args里拿用户名
    username = request.args.get("username")
    # 获取验证码返回的json序列
    result = resp.json()
    if result.get("code") == 200:
        varify_code = result.get("obj")
        # 将username和验证码放进缓存中
        cache.set(username, varify_code)

        data = {
            "msg": "ok",
            "status": 200,
        }

        return jsonify(data)
    data = {
        "msg": "fail",
        "status": 400,
    }

    return jsonify(data)


