from celery import shared_task

@shared_task
def hello():
    print(1+1)