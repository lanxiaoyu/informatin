from flask_sqlalchemy import  SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect,generate_csrf
from flask import Flask,session
from flask_session import Session
from config import config_dict

# 暂时没有app对象，就不会去初始化，只是声明一下
db= SQLAlchemy()
# redis 数据库对象的声明(全局变量)
redis_store=None   #type:StrictRedis

"""ofo 生产单车： 原材料 --->车间 --->小黄
工厂方法：传入配置名称--->返回对应配置的app对象
development:--->app开发模式的app对象
production:---->app线上模式的app对象"""

def create_app(config_name):
   """创建app的方法，工厂方法"""

#1、创建app对象
    app = Flask(__name__)

    # development -->DevelopmentConfig 开发模式的配置类
    # production --->ProductionConfig线上模式的配置类
    configClass=config_dict['development']
    # 将配置类注册到app上  根据不同配置类，赋予了不同模式的app
    app.config.from_object(configClass)

    #2、创建数据库对象
    # 懒加载思想，延迟加载
    db.init_app(app)
    # 3、创建redis数据库对象(懒加载思想）
    global redis_store
    redis_store = StrictRedis(host=configClass.REDIS_HOST,port=configClass.REDIS_POST,db=configClass.REDIS_NUM)

    """
    # 4、开启csrf保护机制
    1、自动获取cookie中打csrf_token,
    2、自动获取ajax请求头中的csrf_token
    3、自己校验这两个值

    """
    csrf = CSRFProtect(app)


    # 5、创建Session对象，将session的存储方法进行调整（flask后端内存--->redis数据库）
    Session(app)

   # 返回不同模式下的app对象
    return app

