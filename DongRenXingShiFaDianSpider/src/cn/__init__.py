#/usr/bin/python
#-*-encoding:utf-8-*-

import requests,re,threading

#target-url:http://www.drxsfd.com/xf/x.htm

url="http://www.drxsfd.com/xf/zhang.asp"
headers = {
"Host":"www.drxsfd.com",
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
"Accept":" text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language":" zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding":" gzip, deflate",
"Referer":" http://www.drxsfd.com/xf/x.htm",
"Cookie":" ASPSESSIONIDAQTQSQDA=CPBKHJBCGKLPDOIHGAEOCFGH",
"Connection":" keep-alive",
"Upgrade-Insecure-Requests":" 1",
"Cache-Control":" max-age=0"}

#url  = "http://www.drxsfd.com/xf/zuiming.asp"
def getTitleChinese(title):
    pat = '第([\d]+)条'
    re.compile(pat)
    num = str(re.findall(pat,title))[2:-2]
    num = int(num)
    dushu=""
    chinese = ["",
        "一","二","三",
        "四", "五", "六",
        "七", "八", "九","零"]
    weishu =["十","百","千"]
    wei = 0
    while num>0:
        index = num%10
        dushu+=chinese[index]
        if num>10:
           dushu+=weishu[wei]
        wei+=1
        num=int(num/10)
    return "第"+dushu[::-1]+"条"
def getAByParas(url , paras , session):
    res = session.get(url,params = paras)
    print(res.url)
    if res.status_code == 200:
        res.encoding = "gb2312"
        context = res.text
        titlePatUrl  = r'<title>(.*?)</title>'
        titlePat = re.compile(titlePatUrl,re.M)
        title = re.findall(titlePat,context)
        #titlePatInItem = getTitleChinese(str(title))
        itemPatUrl = '(第.*?条[\u4E00-\u9FA5|&nbsp;].*[<br>]?.*[.\n]?.*[.\n]?.*[.\n]?.*[.\n]?.*[.\n]?.*[.\n]?.*)<\/span>'
        itemPat = re.compile(itemPatUrl,re.M)
        item = re.findall(itemPat,context)
    else :
        return None
    return (title+item)

def writeIntoFile(content):
    with open("./../../temp/result_1.txt","a+",encoding='utf-8') as f:
        f.write(str(content[0]))
        f.write("\n")
        for i in range(1,content.__len__()):
            f.writelines(str(content[i]))
        f.flush()

def getContext(start,end):
    url = "http://www.drxsfd.com/xf/xx.asp" # bh = 0 -509
    session = requests.session()
    with open("./../../temp/result_1.txt", "a+", encoding='utf-8') as f:
        for i in range(start,end):
            params = {"bh": str(i)}
            content = getAByParas(url = url, paras=params,session=session)
            if content == None:
                continue
            #print(content)
            f.write(str(content[0]))
            f.write("\n")
            for i in range(1, content.__len__()):
                f.writelines(str(content[i]))
            f.flush()

getContext(0,509)
# class SpiderThread (threading.Thread):
#     def __init__(self,threadID,name,start, end):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.start = int(start)
#         self.end = int(end)
#     def run(self):
#         print ("开始线程：" + self.start)
#         getContext(self.start,self.end)
#         print ("退出线程：" + self.end)
#
# # 创建新线程
# thread1 = SpiderThread(1,"hello",0,50)
# thread2 = SpiderThread(2,"hello",50, 100)
# thread3 = SpiderThread(3,"hello",100,150)
# thread4 = SpiderThread(4,"hello",150, 200)
# thread5 = SpiderThread(5,"hello",200,250)
# thread6 = SpiderThread(6,"hello",250, 300)
# thread7 = SpiderThread(7,"hello",300,350)
# thread8 = SpiderThread(8,"hello",350, 400)
# thread9 = SpiderThread(9,"hello",400, 450)
# thread10 = SpiderThread(10,"hello",450, 509)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
# thread6.start()
# thread7.start()
# thread8.start()
# thread9.start()
# thread10.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
# thread4.join()
# thread5.join()
# thread6.join()
# thread7.join()
# thread8.join()
# thread9.join()
# thread10.join()
