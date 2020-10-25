#Show examples of how you would use ALL your implementations here
from decouple import config
from src.spider import scrape
from celery import Celery


app = Celery('main', broker=config('CELERY_BROKER'), backend=config('CELERY_BACKEND'), CELERY_IGNORE_RESULT=config('CELERY_IGNORE_RESULT'),CELERY_TRACK_STARTED=config('CELERY_TRACK_STARTED'))

@app.task()
def add():
  return scrape(1)

add()

