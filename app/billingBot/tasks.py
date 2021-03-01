from celery.decorators import periodic_task
from celery import shared_task
#
# app = celery('tasks', broker='redis://guest@localhost//')
#
# @periodic_task(run_every=(crontab(hour=21, minute=39, day_of_week=7)), name="some_task", ignore_result=True)
# # @app.shared_task
# def add(payment_date):

@shared_task
def send_notifiction():
     print('Here I\’m')
     # Another trick