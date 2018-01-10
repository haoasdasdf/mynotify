# -*- coding: utf-8 -*-

import os
from threading import Timer
from urllib import parse

import MySQLdb
import requests
from bottle import route, run, template
from bs4 import BeautifulSoup

APP_URL = os.environ.get('APP_URL')
CLEARDB_DATABASE_URL = os.environ.get('CLEARDB_DATABASE_URL')


@route("/")
def hello_world():
    return ("hello:" + CLEARDB_DATABASE_URL)
    # url = parse.urlparse(
    #     'mysql://b8f52406326a20:c044b4d5@us-cdbr-iron-east-05.cleardb.net/heroku_d72f255429a03f3?reconnect=true')
    # db_info = {
    #     'NAME': url.path[1:],
    #     'USER': url.username,
    #     'PASSWORD': url.password,
    #     'HOST': url.hostname,
    #     'PORT': url.port if url.port else 3306,
    # }
    # con = MySQLdb.connect(user=db_info.get('USER'),
    #                       passwd=db_info.get('PASSWORD'),
    #                       host=db_info.get('HOST'),
    #                       db=db_info.get('NAME'))
    # cur = con.cursor()
    # sql = "select * from price"
    # cur.execute(sql)
    # rows = cur.fetchall()
    # cur.close
    # con.close
    # info = []
    # for row in rows:
    #     one = {}
    #     one.update({
    #         'name': row[1],
    #         'price': row[3],
    #         'update_time': row[4]
    #     })
    #     info.append(one)
    # return template('./views/index.html', info=info)  # ここで返す内容は何でもよい


def call():
    t = Timer(1799, call)
    t.start()
    try:
        r = requests.get(APP_URL)
    except:
        pass


def main():
    # call()
    run(host="127.0.0.1", port=int(os.environ.get("PORT", 5000)))


if __name__ == '__main__':
    main()
