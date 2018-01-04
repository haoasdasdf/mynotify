# -*- coding: utf-8 -*-

import os
from bottle import route, run
from threading import Timer
import requests

APP_URL = os.environ.get('APP_URL')


@route("/")
def hello_world():
    return "This is a test page"  # ここで返す内容は何でもよい


def call():
    t = Timer(1799, call)
    t.start()
    try:
        r = requests.get(APP_URL)
    except:
        pass


def main():
    call()
    run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)))


if __name__ == '__main__':
    main()
