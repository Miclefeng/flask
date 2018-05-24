###############################################################
# File Name: http.py
# Author: miclefeng
# mail: miclefengzss@163.com
# Created Time: Thu 24 May 2018 09:13:19 PM CST
#=============================================================
# coding:utf8

# urllib
# requests
from urllib import request
from urllib.parse import quote
from flask import json
import requests

class HTTP:

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

    @staticmethod
    def get_with_request(url, json_return=True):
        url = quote(url, safe='/:?=&')
        try:
            # req = request.Request(url, headers=headers)
            with request.urlopen(url) as r:
                res_str = r.read()
                res_str = str(res_str, encoding='utf-8')
            return json.loads(res_str) if json_return else res.str
        except OSError as e:
            return {} if json_return else None
