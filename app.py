# -*- coding: utf-8 -*-

import os
from threading import Timer
from urllib import parse

import MySQLdb
import requests
from bottle import route, run, template, default_app
from bs4 import BeautifulSoup

APP_URL = os.environ.get('APP_URL')
CLEARDB_DATABASE_URL = os.environ.get('CLEARDB_DATABASE_URL')


@route("/")
def hello_world():
    url = parse.urlparse(CLEARDB_DATABASE_URL)
    db_info = {
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port if url.port else 3306,
    }
    con = MySQLdb.connect(user=db_info.get('USER'),
                          passwd=db_info.get('PASSWORD'),
                          host=db_info.get('HOST'),
                          db=db_info.get('NAME'))
    cur = con.cursor()
    sql = "select * from price"
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close
    con.close
    info = []
    for row in rows:
        one = {}
        one.update({
            'name': row[1],
            'price': row[3],
            'update_time': row[4]
        })
        info.append(one)
    return template('./views/index.html', info=info)  # ここで返す内容は何でもよい


def call():
    t = Timer(1799, call)
    t.start()
    try:
        r = requests.get(APP_URL)
    except:
        pass


if __name__ == '__main__':
    call()
    run(host="gunicorn")

app = default_app()
