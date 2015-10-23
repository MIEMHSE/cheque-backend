# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'

from flask import Flask
from celery import Celery

from cheque.config import (
    CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND,
    SECRET_KEY
)


app = Flask(__name__)

app.config['DEBUG'] = True

app.config['CELERY_BROKER_URL'] = CELERY_BROKER_URL
app.config['CELERY_RESULT_BACKEND'] = CELERY_RESULT_BACKEND

app.config['SECRET_KEY'] = SECRET_KEY

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
