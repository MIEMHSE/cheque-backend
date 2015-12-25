# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'

from cStringIO import StringIO
from flask import jsonify, send_file

from cheque.utils import get_image_from_gridfs
from cheque.tasks import hello_task, tesseract_task


def hello_endpoint(task_id=None):
    if task_id:
        task = hello_task.AsyncResult(task_id)

    else:
        task = hello_task.delay()

    response = {
        'message': 'Hello, world!',
        'task_id': str(task),
        'task_state': str(task.state),
        'result': str(task.result)
    }

    return jsonify(response)


def gridfs_media_endpoint(file_id):
    im = get_image_from_gridfs(file_id)

    img_io = StringIO()
    im.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


def after_insert_cheque(items):
    tesseract_task.delay(items[0]['_id'])
