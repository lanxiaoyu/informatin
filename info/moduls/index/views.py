import logging
from flask import current_app
from . import index_bp
from info import redis_store
from info.models import User
from flask import render_template

# 2、使用蓝图
@index_bp.route('/')
def hello_world():
    print(current_app.url_map)
    return render_template('news/index.html')

@index_bp.route('/')
def favicon():
    """返回网页的图标"""
    """
    Function used internally to send static files from the static
+        folder to the browser
这个方法是被内部用来发送静态文件到浏览器的
    """
    return current_app.send_static_file('news/favicon.ico')
