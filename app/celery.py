from celery import Celery
from flask import current_app
import random
import time

celery_app = Celery(__name__)


@celery_app.task
def add(x, y):
    """
    加法
    :param x:
    :param y:
    :return:
    """
    return str(x + y)


@celery_app.task
def flask_app_context():
    """
    celery使用Flask上下文
    :return:
    """
    with current_app.app_context():
        return str(current_app.config)


@celery_app.task(bind=True)
def long_task(self):
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshaper', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10,50)
    for i in range(total):
        if not message or random.random()<0.25:
            message='{0}{1}{2}...'.format(random.choice(verb),random.choice(adjective),random.choice(noun))
            self.update_state(state='PROGRESS',
                              meta={'current':i,'total':total,'status':message})
            time.sleep(1)
    return{'current':100,'total':100,'status':'Task completed!','result':42}                

