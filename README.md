# flask_restful+celery 实现任务接口
预先安装redis数据库,以及pip install celery,pip install redis,pip install flower
## 测试代码
启动celery:   
```
项目根目录下，输入命令:
celery -A run:celery_app worker -l info 
此时celery在终端窗口运行，关闭终端celery就会停止。
----------------------------------------------
输入命令:
celery multi start w1 -A run:celery_app -l info --logfile = celerylog.log --pidfile = celerypid.pid 
此时celery为守护进程，日志记录在celerylog.log里。
日志文件可以指定路径PATH/celerylog.log，此时会在指定路径下创建日志文件。进程号文件类似。
停止或重启将开始换为stop或restart即可，所以需记录w1，即需记录woker的名称来方便重启和停止。
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

