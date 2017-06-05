from ImagesPakcage.pic_spider import img_download
import requests,re,pickle
"""
scrapy sex_picture ="http://www.yuelulu.com/tp/"

"""
url = "http://www.yuelulu.com/tp/"
def get_all_url(url):
    res = requests.get(url)
    res.encoding="utf-8"
    regex = r'href="(\/tp\/.+?\/\d+.html)".+?title='
    pat = re.compile(regex)
    result= re.findall(pat,res.text)
    for i in range(0,result.__len__()):
        result[i]="http://www.yuelulu.com"+result[i]
    print(result)
    return result

def get_each_url(url):
    print("This url is ",url)
    res = requests.get(url)
    res.encoding = "utf-8"
    regex=r'src="(\/d\/file\/.+?\/.+?\/.+?jpg)'
    #regex = r'<img.+?src="(\/d\/file\/\d.+?\/\d.+?\/\d.+?\.jpg".+?/>'
    pat = re.compile(regex)
    result = re.findall(pat, res.text)
    for i in range(0, result.__len__()):
        result[i] = "http://www.yuelulu.com" + result[i]
    print("result is",result)
    return result
urls=get_all_url(url)
all_pic_result=[]
for i in range(0,urls.__len__()):
    all_pic_result.append(get_each_url(urls[i]))
    #http://www.yuelulu.com/tp/omtp/34804.html
print(" all of the picture is ",all_pic_result)
#pickle.dump(all_pic_result,"./File/sex_picture_img_url.txt",2)
for i in range(0,all_pic_result.__len__()):
    print("the next url is ",all_pic_result[i])
    for j in range(0,all_pic_result[i].__len__()):
        img_download(all_pic_result[i][j])
        with open("./File/sex_picture_img_url.txt","a")as f:
            f.writelines(all_pic_result[i][j]+"\r\n")
            f.close()

    #