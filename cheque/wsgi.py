# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'


from cheque.api import hello_endpoint
from cheque.bridge import app


app.route('/api/v1/hello')(app.route('/api/v1/hello/<task_id>')(hello_endpoint))


if __name__ == '__main__':
    app.run()
