# -*- coding: utf-8 -*-

import os
from bottle import route, run

@route("/")
def hello_world():
    MAILGUN_API_KEY=os.environ.get('SENDGRID_USERNAME')
    # return "This is a test page"  # ここで返す内容は何でもよい
    return MAILGUN_API_KEY

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
