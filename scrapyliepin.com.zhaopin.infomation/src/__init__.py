#!/usr/bin/python
#-*-encoding:utf-8-*-
import requests,re,math
#targeturl = 'https://www.liepin.com/zhaopin/?pubTime=30&ckid=c3ba30ff63805f77&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&dqs=070020&industryType=industry_01&jobKind=&sortFlag=15&degradeFlag=1&industries=010&salary=&compscale=010&key=python&clean_condition=&headckid=c3ba30ff63805f77&curPage=1'
targeturl = 'https://www.liepin.com/zhaopin/'
#GET /zhaopin/?pubTime=30&ckid=c3ba30ff63805f77&fromSearchBtn=2&compkind=&isAnalysis=&init=-1&searchType=1&dqs=070020&industryType=industry_01&jobKind=&sortFlag=15&degradeFlag=1&industries=010&salary=&compscale=010&key=python&clean_condition=&headckid=c3ba30ff63805f77&curPage=1 HTTP/1.1
headers={
'Host': 'www.liepin.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
#Referer: https://www.liepin.com/zhaopin/?industries=010&dqs=070020&salary=&jobKind=&pubTime=30&compkind=&compscale=010&industryType=industry_01&searchType=1&clean_condition=&isAnalysis=&init=1&sortFlag=15&flushckid=0&fromSearchBtn=1&headckid=6b4ae2953cb68714&key=python
'Cookie': 'abtest=0; JSESSIONID=A9C08E169AC55E99F34F34482F7BA866; _fecdn_=1; __uuid=1496216240510.29; __tlog=1496216240511.56%7C00000000%7C00000000%7Cs_00_pz1%7Cs_00_pz1; __session_seq=19; __uv_seq=19; gr_user_id=e6222af4-b4be-48c9-a908-0f109973c257; gr_session_id_bad1b2d9162fab1f80dde1897f7a2972=5e1eb18f-5f6a-40c5-b95c-8fe1181cc9b8; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1496216241; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1496217315; _mscid=s_00_pz1; _uuid=5D6F7B54FFA8420C4833FF0BB66256DD; verifycode=c9712ca6408249338e11393374e6c315; 57de6c16=fec19a997405f4cfc0f309fa5a5674c3; 80fb1dd4=452ae2aa441e6d3e8c45ad40be63eac2; aa13475b=28a8e24fbefc95c2d401a04030abddaa; slide_guide_home=1; user_name=%E6%96%B9%E7%87%95%E5%B9%B3; lt_auth=u%2BZcbnMCmVWstyPZgGdX4%2F1N3ImtVGrA8nsJgh0C0dS5Wffn4PzqQgKGrbYFxBMhlEgmJcULNbn4%0D%0AN%2Bn5yHRI70UbwGqnnoCyv%2FKk0HYFUeVnJ8Wlg%2F6skMWGEZxwwCwGzHRk9y4elEry4RIlZ9O%2FnA%2Bn%0D%0As6HH7qSc8PLNgxw%3D%0D%0A; UniqueKey=fe3883f928d408001a667e00ad0d9493; user_kind=0; user_photo=55557f3b28ee44a8919620ce01a.gif; is_lp_user=true; user_vip=0; gr_cs1_5e1eb18f-5f6a-40c5-b95c-8fe1181cc9b8=UniqueKey%3Afe3883f928d408001a667e00ad0d9493; login_temp=islogin; em_username=4521063980o1871294081; em_token=YWMtKlYdTkXWEeeYsrmeot5bpU8TxtBqMxHkgus5YKfC9XEqUXmwRdYR5585UQni4Qi1AwMAAAFcXX5U6QBPGgAQFg5JSD6SWsJyANFaFI1TzF-VHWta1hHnfP3YdT8xXA',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Cache-Control': 'max-age=0'
}
params ={   'ckid':'c3ba30ff63805f77',
'clean_condition':'',
'compkind':'',
'compscale':'010',
'curPage':'1',
'degradeFlag':'1',
'dqs':'070020',
'fromSearchBtn':'2',
'headckid':'c3ba30ff63805f77',
'industries':'010',
'industryType':'industry_01',
'init':'-1',
'isAnalysis':'',
'jobKind':'',
'key':'python',
'pubTime':'30',
'salary':'',
'searchType':'1',
'sortFlag':'15'
            }

s = requests.session()
r = s.get(targeturl, headers=headers,params=params)
#pattdaiyu = r'<div class="job-info">[.\n].*<h..title="(.*?)">[.\n].*<a.href="(.*?)"[.\n].*[.\n].*(.*?)<\/a>.*[.\n].*[.\n].*[.\n].*[.\n].*title="(.*?)">[.\n].*".(.*?)<\/span>[.\n].*[.\n].*"*area*"*>(.*?)<\/a>[.\n].*"edu">?(.*?)<\/span>[.\n].*>(.*?)<\/span>[.\n].*[.\n].*[.\n]*.*>(.*?)<\/time>'
#pattdaiyu = r'<div class="job-info">[.\n].*<h..title="(.*?)">[.\n].*<a.href="(.*?)"[.\n].*[.\n].*(.*?)<\/a>.*[.\n].*[.\n].*[.\n].*[.\n].*title="(.*?)">[.\n].*".(.*?)<\/span>[.\n].*[.\n].*"*area*"*>(.*?)<\/a>[.\n].*"edu">?(.*?)<\/span>[.\n].*>(.*?)<\/span>[.\n].*[.\n].*[.\n]*.*>(.*?)<\/time>'
def getByEvry():
    patPosition = r'<h..title="(.*?)">'
    patPosition = re.compile(patPosition,re.M)
    patEdu = r'"edu">?(.*?)<\/span>'
    patEdu  = re.compile(patEdu,re.M)
    patArea = r'"*area*"*>([\s\S]*)<\/a>'
    patArea = re.compile(patArea,re.M)
    patExeper = r'"edu">.*<\/span>.*>([\s\S]*)<\/span>'
    patExeper = re.compile(patExeper,re.M)
    posResult = re.findall(patPosition,r.text)
    areaResult = re.findall(patArea,r.text)
    eduResult = re.findall(patEdu,r.text)
    exeperResult = re.findall(patExeper,r.text)
    print(posResult.__len__(),areaResult.__len__(),eduResult.__len__(),exeperResult.__len__())
    for i in range(math.min(posResult.__len__(),areaResult.__len__(),eduResult.__len__(),exeperResu)):
        print(posResult[i],"1      ",areaResult[i],"1      ",eduResult[i],"     1",exeperResult)

#pat = r'<div class="job-info">[.\n].*<h..title="(.*?)">[.\n].*<a.href="(.*?)"[.\n].*[.\n].*(.*?)<\/a>.*[.\n].*[.\n].*[.\n].*[.\n].*title="(.*?)">[.\n].*".(.*?)<\/span>[.\n].*[.\n].*"*area*"*>(.*?)<\/a>[.\n].*"edu">?(.*?)<\/span>[.\n].*>(.*?)<\/span>[.\n].*[.\n].*[.\n]*.*>(.*?)<\/time>'
# pat = r'a'
# s = requests.session()
# rs = s.get(targeturl)
# patall = re.compile(pat,re.M)
# match = patall.match(r.text)
# print(match)
# if match:
#     print(match)
getByEvry()