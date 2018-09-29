
from  flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db

# 从单一职责的思想考虑：manager.py文件仅仅作为项目启动文件即可，其余配置全部抽取出去
# ofo公司 调用工厂方法
app=create_app('development')

# 6、创建管理对象
manager = Manager(app)

# 7、数据库迁移对象
Migrate(app,db)

# 8、添加数据库迁移指令
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()