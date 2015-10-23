# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'

from flask import jsonify


def root():
    response = {
        'message': 'Hello, world!'
    }

    return jsonify(response)
