#　flask_restful+celery 实现任务接口
预先安装redis数据库,以及pip install celery,pip install redis
##　测试代码
启动   celery:   celery -A run:celery_app worker -l info
启动Flask APP:   python run.py

