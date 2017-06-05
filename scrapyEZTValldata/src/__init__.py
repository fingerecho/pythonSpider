#!/usr/bin/python

#srcurl  https://eztv.ag/
#### tarurl (https:\/\/zoink.ch\/torrent\/.*?\.mkv\.torrent)

import re,requests


url = "https://eztv.ag/"

def getTar(url):
    res = requests.get(url)
    res.encoding="UTF-8"
    txt = res.text
    pattor = r'"(https:\/\/zoink.ch\/torrent\/.*?\.mkv\.torrent)"'
    pat = r'alt="(.*?)\[eztv\](.*?[A-Z]{2})\)..\"?class=\"epinfo\"'
    result= re.findall(pat,txt)
    resultor= re.findall(pattor,txt)
    count=0
    trueName =[]
    tempName=""
    for i in result:
        if count%2==0:
            tempName=str(i)+""
        elif count%2==1:
            tempName=tempName+str(i)+""
        trueName.append(tempName)
        count=count+1
        tempName=""
    return trueName,resultor
for i in getTar(url):
    print(i)
