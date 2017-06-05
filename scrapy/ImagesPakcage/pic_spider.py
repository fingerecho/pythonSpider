#!/usr/bin/python

import re
import requests
import random
"""
function:爬取百度贴吧的一些图片
time:2017/3/31
author:fyping
"""
url="http://tieba.baidu.com/f?kw=%E6%A1%8C%E9%9D%A2&ie=utf-8"
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    for i in range(randomlength):
        str=str+chars[random.randint(0, length)]
    return str

def get_content(url):
	res = requests.get(url)
	res.encoding="utf-8"
	html = res.text
	return html

"""data-original="http://imgsrc.baidu.com/forum/wh%3D200%2C90%3B/sign=92cdbc34dc39b6004d9b07b5d9601913/0a9a033b5bb5c9ea92cdbc34dc39b6003af3b328.jpg"""

def get_images(info):
	regex = r'data-original="http://imgsrc.baidu.com/forum/(.+?\.jpg)'
	pat = re.compile(regex)
	images_code=re.findall(pat,info)
	return images_code

def img_download(imgurl):
	length = imgurl.__len__()
	strs = random_str(18)
	file_name ="./Images/"+strs+".jpg"
	img = requests.get(imgurl)
	with open(file_name,"wb") as f:
		for chunk in img.iter_content(chunk_size=1024):
			if chunk:
				f.write(chunk)
				f.flush()
		f.close()
#print(random_str(10))