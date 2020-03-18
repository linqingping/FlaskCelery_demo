from flask_restful import Resource, Api
from .server import Servers, Server,Taskstatus
from flask import Blueprint

assets_page = Blueprint('assets_page', __name__)
api = Api(assets_page)

#注册路由
api.add_resource(Servers, '/servers')
api.add_resource(Server, '/servers/<_id>')
api.add_resource(Taskstatus, '/taskstatus/<_id>')
