# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'

from time import sleep

from PIL import ImageEnhance
from pymongo import Connection
from pytesseract.pytesseract import image_to_string, TesseractError

from cheque.bridge import celery
from cheque.settings import EVE_SETTINGS
from cheque.utils import get_image_from_gridfs


@celery.task
def hello_task():
    task_id = hello_task.request.id

    print 'Hello task started with task_id {task_id}'.format(task_id=task_id)
    sleep(10)
    result = 42
    print 'Hello task {task_id} ended with result {result}'.format(
            task_id=task_id,
            result=result
    )
    return result


@celery.task
def tesseract_task(cheque_id):
    mongo_connection = Connection(
        EVE_SETTINGS['MONGO_HOST'],
        EVE_SETTINGS['MONGO_PORT']
    )

    db = mongo_connection[EVE_SETTINGS['MONGO_DBNAME']]
    cheque = db.cheque.find_one(cheque_id)

    if cheque:
        try:
            im = get_image_from_gridfs(cheque['image'])
            im = ImageEnhance.Color(im).enhance(0.0)
            im = ImageEnhance.Sharpness(im).enhance(1.5)
            im = ImageEnhance.Contrast(im).enhance(1.7)

        except KeyError:
            raise

        for lang in ('rus', 'eng'):
            try:
                db.cheque.update({'_id': cheque_id}, {'$set': {
                    'text_{lang}'.format(lang=lang): image_to_string(im, lang=lang)
                }})

            except TesseractError:
                pass
