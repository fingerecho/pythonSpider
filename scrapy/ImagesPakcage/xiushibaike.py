#!/usr/bin/python

"""
爬 糗事百科并填入数据库
“http://www.qiushibaike.com/hot/"
#The nest page :
<a href="/hot/page/2?s=4970401" rel="nofollow">
<!--<a href="/hot/page/2/" rel="nofollow">-->
<span class="page-numbers">
2
</span>
</a>
"""
import requests,re,sys,MySQLdb,time

class GetQiushiBake(object):
    """cursor = MySQLdb.connect(
    '115.159.94.150',
    '3306',
    'root',
    'fy911phutys',
    'Zero')"""
     #   "115.159.94.150","root","fy911phutys","Zero")
    #db = MySQLdb.connect("115.159.94.150", "root", "fy911phutys", "Zero")
    #cursor= db.cursor()
    get_page_count=0
    jokes=""
    mainurl =""
    all_page_url_list=[]
    all_jokes=[]
    next_page_url_regex_pattern= re.compile(r'(\/hot\/page\/.+?=.+?)".*rel="nofollow">')
    nowtime=time.localtime()
    year=str(nowtime.tm_year)
    month=str(nowtime.tm_mon)
    day = str(nowtime.tm_mday)
    hour = str(nowtime.tm_hour)
    min =str(nowtime.tm_min)
    sec = str(nowtime.tm_sec)
    nowtime = "爬取时间为%s年%s月%s日%s：%s：%s\' "%(year,month,day,hour,min,sec)
    def __init__(self,mainUrl):
        self.mainurl= mainUrl
        self.__get_next_page(self.mainurl)
        #print(self.all_jokes)
        sql=self.__get_Sql()
        self.__write_into_file()
        #sql='insert into jokes(jokes,id) values("aaaaddaaaadddaaa",0);'
        #print(sql)

        #self.__insert_into_sql(sql)
        pass
    def __write_into_file(self):
        with open("./File/jokes.txt","a") as f:
            j=0
            for i in self.all_jokes:
                i=str(i)
                print(i)
                f.writelines("("+str(j)+") "+i)
                f.write("\r\n")
                j=j+1
            f.writelines("\r\n"+self.nowtime+"\r\n")
            f.close()

        print(("now we put %d spice jokes into file!")%(self.all_jokes.__len__()))
    def __get_Sql(self):
        print("it start function  sql!")
        j = 0
        sql=[]
        for i in self.all_jokes:
            sql.append( "insert into jokes(jokes , id) values('%s','%d');" % (str(i), j));
            j=j+1
        return (sql)
    def __insert_into_sql(self,sql):
        try:
            db = MySQLdb.connect("115.159.94.150", "root", "fy911phutys", "Zero")
            cursor = db.cursor()
        except:
            print("connection error!")
            sys.exit(-2)
        try:
            #for i in sql:
            #    cursor.execute(i)
            #    print(i,)
            #print(sql[0])
            #cursor.execute(str(sql[0]))
            sqls="insert into jokes(jokes,id) values ('hello world second ',0);"
            #print(type(sqls),)
            #print(type(sql[0]),)
            #cursor.execute(sql)
            db.commit()
            db.close()
        except:
            print("insertion has error!")
            db.rollback()
            db.close()
            sys.exit(-3)
    def __str__(self):
        """
        """
        pass
    def __get_next_page(self,url):
        self.get_page_count=self.get_page_count+1
        if self.get_page_count >=50:
            return
        #if id(url) is id("http://www.qiushibaike.com/hot/page/35?s=4970422"):
        #    print("It has scrapy page 10")
        try:
            res = requests.get(url)
            res.encoding="utf-8"
        except:
            print("Get_next page error!")
            sys.exit(-1)
        html = res.text
        regex_jokes = r'<span>([\u4e00-\u9fa5]$|[^\dA-Za-z_]{30,100})<\/span>'
        regex_com = re.compile(regex_jokes)
        jokes= re.findall(regex_com,html)
        for i in jokes:
            #print(str(i),)
            #print("\r\n")
            self.all_jokes.append(i)
        """for i in jokes:
            try:
                sql = "insert into jokes(jokes) values(\"%s\");"%(str(i))
                self.cursor.execute(sql)
                self.db.autocommit()
            except:
                self.db.rollback()
                """
        result = re.findall(self.next_page_url_regex_pattern,html)
        for i in range(0,result.__len__()):
            result[i]="http://www.qiushibaike.com"+result[i]
            if self.all_page_url_list.__contains__(result[i]):
                continue
            self.all_page_url_list.append(result[i])
            self.__get_next_page(result[i])
            #print(result[i],)
        pass
    pass
#demo = GetQiushiBake("http://www.qiushibaike.com/hot/")
#demo.__get_next_page("http://www.qiushibaike.com/hot/",reg)
"""regex = r'(\/hot\/page\/.+?=.+?)".*rel="nofollow">'
pat = re.compile(regex)
url = "http://www.qiushibaike.com/hot/"
try:
    res = requests.get(url)
    res.encoding = "utf-8"
except:
    print("Get_next page error!")
    sys.exit(0)
html = res.text
result = re.findall(pat,html)
print(type(result))
print(result)"""
mainurl = "http://www.qiushibaike.com/hot/"
#mainurl ="http://www.qiushibaike.com/hot/page/39?s=4970417"
demo = GetQiushiBake(mainurl)
#print(demo.all_page_url_list.__len__())
url_2 = 'http://www.qiushibaike.com/hot/page/2?s=4970419'
#print(demo.all_page_url_list)



