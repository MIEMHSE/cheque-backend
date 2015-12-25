# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'


from cheque.api import hello_endpoint, gridfs_media_endpoint, after_insert_cheque
from cheque.bridge import app
from cheque.settings import EVE_SETTINGS


app.route('/api/v1/hello')(app.route('/api/v1/hello/<task_id>')(hello_endpoint))
app.route('/{media_endpoint}/<file_id>'.format(
    media_endpoint = EVE_SETTINGS.get('MEDIA_ENDPOINT', 'media')
))(gridfs_media_endpoint)

app.on_inserted_cheque += after_insert_cheque


if __name__ == '__main__':
    app.run()
