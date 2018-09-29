from redis import StrictRedis
import logging

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

class DevelopmentConfig(Config):
   """开发环境的项目配置"""
   DEBUG = True

#    开发模式的日志级别：DEBUG
    LOG_LELEL= logging.DEBUG

class ProductionConfig(Config):
    """生产环境的项目配置"""
    DEBUG = False

#     线上模式的日志级别：WANRNING
    LOG_LEVEL = logging.WARNING


# 给外界暴露一个使用配置类的接口
# 使用方法: config_dict['development'] --->DevelopmentConfig 开发环境的配置类
config_dict={
   'development':DevelopmentConfig,
   'production':ProductionConfig
}