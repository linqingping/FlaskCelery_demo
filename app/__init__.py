from flask import Flask
from .celery import celery_app


def create_app():
    app = Flask(__name__)
    
    celery_app.conf.update({"broker_url": 'redis://127.0.0.1:6379/0',
                            "result_backend": 'redis://127.0.0.1:6379/0', })
    # 导入创建的蓝图
    from .urls import assets_page
    # 注册这个蓝图对象
    app.register_blueprint(assets_page)
    return app

