from flask_restful import Resource, Api
from .server import Servers, Server,Taskstatus #导入路由的具体实现方法
from flask import Blueprint

#创建一个蓝图对象
assets_page = Blueprint('assets_page', __name__)
#在这个蓝图对象上进行操作,注册路由
api = Api(assets_page)

#注册路由
api.add_resource(Servers, '/servers')
api.add_resource(Server, '/servers/<_id>')
api.add_resource(Taskstatus, '/taskstatus/<_id>')
