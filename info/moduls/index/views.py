import logging
from flask import current_app
from . import index_bp

# 2、使用蓝图
@index_bp.route('/')
def hello_world():
    logging.debug('我是debug级别日志')
    logging.info('我是info级别日志')
    logging.warning('我是warning级别日志')
    logging.error('我是error级别日志')
    logging.critical('我是critical级别日志')

    # flask 中对logging模块进行封装，直接用current_app调用（常见）
    current_app.logger.debug("flask 中记录的debug日志")
    return 'hello 777'