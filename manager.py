from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from  redis import StrictRedis
from flask_wtf.csrf import CSRFProtect,generate_csrf
from flask_session import Session

class Config(object):
#1、创建app对象
app = Flask(__name__)
# 将配置类注册到app上
app.config.from_object(Config)

#2、创建数据库对象
db=SQLAlchemy(app)


@app.route('/')
def hello_world():
    return


if __name__ == '__main__':
    app.run(debug=True)