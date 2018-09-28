from flask_sqlalchemy import  SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect,generate_csrf
from flask import Flask,session
from flask_session import Session
from  flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

class Config(object):
   """项目配置信息"""
DEBUG = True
# mysql数据库配置信息
# 数据库链接配置
SQLALCHEMY_DATABASE_URI='mysql://root:mysql@127.0.0.1:3306/information'
# 关闭数据库修改跟踪
SQLALCHEMY_TRACK_MODIFICATIONS=False

# redis数据库配置信息
REDIS_HOST = '127.0.0.1'
REDIS_POST = 6379
REDIS_NUM = 1

# 加密字符串
SECRET_KEY = 'FGYUIOL,MNVCXDFTYUIOLM'
# 通过flask_session拓展，将flask中的session（内存）调整到redis的配置信息
# 存储数据库的类型：redis
SESSION_TYPE ='redis'
# 将redis实例对象进行传入
SECRET_REDIS= StrictRedis(host=REDIS_HOST,port=REDIS_POST,db=REDIS_NUM)
#对session数据进行加密处理
SESSION_USE_SIGNER=True
# 关闭永久存储
SESSION_PREMANENT=False
# 过期时长（24h)
RERMANENT_SESSION_LIFETIME = 86400

#1、创建app对象
app = Flask(__name__)
# 将配置类注册到app上
app.config.from_object(Config)

#2、创建数据库对象
db=SQLAlchemy(app)

# 3、创建redis数据库对象
redis_store = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_POST,db=Config.REDIS_NUM)

"""
# 4、开启csrf保护机制
1、自动获取cookie中打csrf_token,
2、自动获取ajax请求头中的csrf_token
3、自己校验这两个值

"""
csrf = CSRFProtect(app)

# 5、创建Session对象，将session的存储方法进行调整（flask后端内存--->redis数据库）
Session(app)

# 6、创建管理对象
manager = Manager(app)

# 7、数据库迁移对象
Migrate(app,db)

# 8、添加数据库迁移指令
manager.add_command('db',MigrateCommand)


@app.route('/')
def hello_world():
    return 'hello66666'
if __name__ == '__main__':
    manager.run()