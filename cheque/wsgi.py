# -*- coding: utf-8 -*-

__author__ = 'Sergey Sobko'


from cheque.api import root
from cheque.bridge import app


app.route('/')(root)


if __name__ == '__main__':
    app.run()
