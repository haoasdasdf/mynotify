# -*- coding: utf-8 -*-

import os
from bottle import route, run

@route("/")
def hello_world():
    MAILGUN_API_KEY=os.environ.get('MAILGUN_API_KEY')
    # return "This is a test page"  # ここで返す内容は何でもよい
    return MAILGUN_API_KEY

run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)))
