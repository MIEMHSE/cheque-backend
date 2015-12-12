# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'

from time import sleep

from cheque.bridge import celery


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
