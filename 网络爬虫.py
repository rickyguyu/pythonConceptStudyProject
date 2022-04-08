import requests

def getHTMLtext(url):
    try:
        hd ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        r=requests.get(url, headers = hd)
        r.raise_for_status # 如果状态不是200，引发HTTPError
        r.encoding = r.apparent_encoding
        
        return r.text
    except :
        return "产生异常"

if __name__ =="__main__":
    url ="http://www.unitedlogdom.com"
    print(getHTMLtext(url))
    
def getSEARCHtext(key,engine):
    try:
        hd ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        url1= "http://www.google.com/search"
        pm1 = {"q":key}

        url2= "http://www.baidu.com/s"
        pm2 = {"wd":key}
        
        url3= "http://www.so.com/s"
        pm3 = {"q":key}

        if engine == "google":
            r = requests.get(url1,params = pm1,headers = hd)
        elif engine == "baidu":
            r = requests.get(url2,params = pm2,headers = hd)
        elif engine == "360":
            r = requests.get(url3,params = pm3,headers = hd)
        else:
            r = requests.get(url1,params = pm1,headers = hd)
        r.raise_for_status # 如果状态不是200，引发HTTPError
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ =="__main__":
    # google 爬取成功
    # print(getSEARCHtext("Python","google"))
    # 百度爬取出错
     print(getSEARCHtext("Python","baidu"))
    # 360 爬取成功
    # print(getSEARCHtext("Python","360"))
