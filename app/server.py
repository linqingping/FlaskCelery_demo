# !/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request,url_for
from flask_restful import Resource,Api
from .celery import add, flask_app_context,long_task　#导入celery的task
import jsonify

# 实现路由的具体操作类

class Servers(Resource):
    def get(self):
        result = add.delay(1, 2)
        return result.get(timeout=1)
    def post(self):
        data = request.get_json()
        return 'add new data: %s'%data

class Server(Resource):
    def get(self,_id):
         result = flask_app_context.delay()
         return result.get(timeout=1).replace('<Config', '')
    def post(self,_id):
        return 'delete data:%s'%_id
    def put(self,_id):
        data=request.get_json()
        return 'put data %s:%s'%(_id,data)

class Taskstatus(Resource):
    def get(self,_id):
        task = long_task.apply_async()
        return str('Location:'+'taskstatus/'+task.id)
    def post(self,_id):
        task = long_task.AsyncResult(_id)
        if task.state == 'PENDING':
            #job did not start yet
            response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
            }
        elif task.state != 'FAILURE':
            response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
            }
            if 'result' in task.info:
                response['result'] = task.info['result']
        else:
            # something went wrong in the background job
            response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
            }
        return response
