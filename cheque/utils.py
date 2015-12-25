#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'
__email__ = 'S.Sobko@profitware.ru'
__copyright__ = 'Copyright 2015, The Profitware Group'

from bson import ObjectId
from gridfs import GridFS, NoFile
from pymongo import Connection, errors
from PIL import Image

from cheque.settings import EVE_SETTINGS


def get_image_from_gridfs(file_id):
    try:
        mongo_connection = Connection(
            EVE_SETTINGS['MONGO_HOST'],
            EVE_SETTINGS['MONGO_PORT']
        )
        gridfs_database = GridFS(mongo_connection[EVE_SETTINGS['MONGO_DBNAME']])

        im_stream = gridfs_database.get(ObjectId(file_id))
        im = Image.open(im_stream)
        return im

    except (errors.ConnectionFailure, NoFile):
        raise
