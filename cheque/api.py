# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'

from bson import ObjectId
from cStringIO import StringIO
from flask import jsonify, send_file
from gridfs import GridFS, NoFile
from pymongo import Connection
from PIL import Image

from cheque.settings import EVE_SETTINGS
from cheque.tasks import hello_task

mongo_connection = Connection(
    EVE_SETTINGS['MONGO_HOST'],
    EVE_SETTINGS['MONGO_PORT']
)
gridfs_database = GridFS(mongo_connection[EVE_SETTINGS['MONGO_DBNAME']])


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
    try:
        im_stream = gridfs_database.get(ObjectId(file_id))
        im = Image.open(im_stream)
        img_io = StringIO()
        im.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')

    except NoFile:
        raise
