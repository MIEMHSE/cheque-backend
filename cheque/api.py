# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'

from flask import jsonify

from cheque.tasks import hello_task


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
