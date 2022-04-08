import requests
import re # 正则表达式
from bs4 import BeautifulSoup

def getSoup(url):
    try:
        hd ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        r=requests.get(url, headers = hd)
        r.raise_for_status # 如果状态不是200，引发HTTPError
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text,"html.parser")
        return soup
    except :
        return "产生异常"

if __name__ =="__main__":
    url ="https://python123.io/ws/demo.html"
   # print(getSoup(url).prettify())
    print(getSoup(url).a.attrs["href"])
    print(getSoup(url).a.string)
    for ns in getSoup(url).find_all(re.compile('a')):
        if ns is not None:
            print(ns.name)

    for ns in getSoup(url).find_all("a"):
        if ns is not None:
            print(ns.attrs["href"])
            
    for ns in getSoup(url).find_all(string= re.compile("Python")):
        if ns is not None:
            print(ns.string) 
