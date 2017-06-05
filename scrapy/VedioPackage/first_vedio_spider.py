#!/usr/bin/python
import requests,re,pickle,os
from ImagesPakcage.pic_spider import random_str
"""
the first url is :http://www.yuelulu.com/e/DownSys/play/?classid=13&id=34868&pathid=0
vedio urs is :http://jiujiu.4949899.com:81/playapi/61043/?index.mp4
"""
#url="http://www.yuelulu.com/e/DownSys/play/?classid=13&id=34868&pathid=0"
#regex src =var video=['http://jiujiu.4949899.com:81/playapi/61043/?index.mp4->video/mp4'];
#regex stc =var video=['http://jiujiu.4949899.com:81/playapi/64408/?index.mp4->video/mp4'];
#tegex src = href="/e/DownSys/play/?classid=13&id=34867&pathid=0">
#regex stc =view-source:http://www.yuelulu.com/e/DownSys/play/?classid=13&id=34833&pathid=0


url="http://jiujiu.4949899.com:81/playapi/61043/?index.mp4"

def vedio_download(url):
    filename = random_str(10)+".mp4"
    try:
        r = requests.get(url, stream=True)
        f = open("./VedioTemporary/"+filename, "wb")
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    except:
        print("download error exists!")

def get_show_info_url(url):
    try:
        res= requests.get(url)
    except:
        print("the url of ",url," exception !")
        return
    res.encoding="utf-8"
    rege= r'<a href="(\/e\/action\/ShowInfo\.php\?classid=\d+&id=\d+)"'
    pat=re.compile(rege)
    result=re.findall(pat,res.text)
    for i in range(result.__len__()):
        result[i]="http://www.yuelulu.com"+result[i]
    print(result)
    return result
def get_download_info_url(url):
    try:
        res = requests.get(url)
    except:
        print("the url of ",url," exception !")
        return
    res.encoding = "utf-8"
    rege = r'href.?="(\/e\/DownSys\/play\/\?classid=\d+&id=\d+&pathid=\d+)">'
    pat = re.compile(rege)
    result = re.findall(pat, res.text)
    for i in range(result.__len__()):
        result[i] = "http://www.yuelulu.com" + result[i]
    print(result)
    return result
def get_downloadurl(url):
    #var video=['http://jiujiu.4949899.com:81/playapi/61075/?index.mp4->video/mp4'];   'https?://[^/]+?/'
    try:
        res = requests.get(url)
    except:
        print("the url of ",url," exception !")
        return
    res.encoding = "utf-8"
    #rege = r'var.+?video=\[\'(http://jiujiu\.\d+\.com:\d+\/playapi\/\d+\/\?index\.mp4->video\/mp4)\''
    #rege=r"var.video=\['http:\/\/jiujiu\.\d+\.com:\d+\/playapi\/\d+\/\?index\.mp4->video\/mp4\'\]"
    rege=r'(http:\/\/jiujiu\.\d+\.com:\d+\/playapi\/\d+\/\?index\.mp4->video\/mp4)'
    pat = re.compile(rege)
    result = re.findall(pat, res.text)
    print(result)
    return result
mainurl="http://www.yuelulu.com/zx/"
def download_from_index_page(mainurl):
    showinfourls=get_show_info_url(mainurl)
    #print(showinfourls[0])
    watchurl=[]
    with open("./Vedio/vedi0-list.txt","w") as f:
        for i in range(showinfourls.__len__()):
            downloadurls=get_download_info_url(showinfourls[i])
            for i in range(downloadurls.__len__()):
                f.writelines(downloadurls[i]+"\r\n")
                watchurl.append(get_downloadurl(downloadurls[i]))
    #print(downloadurl)
    print(watchurl)
    for i in range(watchurl.__len__()):
        vedio_download(watchurl[i][0])
#download_from_index_page(mainurl)
#get_downloadurl(downloadurl)
