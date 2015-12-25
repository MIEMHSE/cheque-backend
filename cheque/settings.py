# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'

CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost//'

SECRET_KEY = 'aSDF#%GSRG#$GsasdfasdfHGGGFSN/.345234'

EVE_SETTINGS = {
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',

    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'cheque_restful',
    'RETURN_MEDIA_AS_BASE64_STRING': False,

    'RETURN_MEDIA_AS_URL': True,

    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'ITEM_METHODS': ['GET', 'PATCH', 'DELETE'],

    'XML': False,

    'MEDIA_BASE_URL': 'https://db.profitware.ru/cheque',
    'MEDIA_ENDPOINT': 'gridfs_media',
    'DOMAIN': {
        'people': {
            'item_title': 'person',
            'schema': {
                'first_name': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 10,
                },
                'last_name': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 15,
                    'required': True,
                    'unique': True,
                },
                'role': {
                    'type': 'list',
                    'allowed': ['author', 'contributor', 'copy'],
                },
                'location': {
                    'type': 'dict',
                    'schema': {
                        'address': {'type': 'string'},
                        'city': {'type': 'string'}
                    },
                },
                'born': {
                    'type': 'datetime',
                },
            }
        },
        'cheque': {
            'schema': {
                'person': {
                    'type': 'objectid',
                    'data_relation': {
                        'resource': 'people',
                        'field': '_id',
                        'embeddable': True
                    },
                },
                'name': {
                    'type': 'string'
                },
                'image': {
                    'type': 'media'
                },
                'text_rus': {
                    'type': 'string'
                },
                'text_eng': {
                    'type': 'string'
                }
            }
        }
    }
}
