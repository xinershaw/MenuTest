# coding=utf-8
"""
Created on 2018年5月15日
@author: Xiaoxin
Project:......
"""
from requests_html import HTMLSession


class API(object):
    def __init__(self, base_url):
        self.session = HTMLSession()
        self.base_url = 'http://bk.tuluo56.com'

    def post(self):
        pass

