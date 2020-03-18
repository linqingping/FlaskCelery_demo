# flask_restful+celery 实现任务接口
预先安装redis数据库,以及pip install celery,pip install redis,pip install flower
## 测试代码
启动celery:   
```
celery -A run:celery_app worker -l info
```
启动Flask APP:   
```
python run.py
```
--可选启动flower: 
```  
celery -A run:celery_app flower -l info 
```
浏览器访问http://localhost:5555可以查看任务状态!

