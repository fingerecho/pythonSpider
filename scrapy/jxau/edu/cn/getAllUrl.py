#!/usr/bin/python
import requests,re

#url:http://http://www.jxau.edu.cn/
def getUrl(main_url):
    res = requests.get(main_url)
    reg =r'https?:\/\/.*'
    regpat = re.compile(
