import requests
import re # 正则表达式
from bs4 import BeautifulSoup
import bs4

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

def fillUnivList(ulist, soap):
    for tr in soup.find("tbody").children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string,tds[1].string,tds[4].string])

def printUnivList(ulist, num):

    tplt = "{0:<10}\t{1:<15}\t{2:<10}"
    print(tplt.format("排名","学校名称","总分"))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2]))
if __name__ =="__main__":
    uList =[]
    url ="http://www.zuihaodaxue.com/zuihaodaxuepaiming-zongbang-2020.html"
    soup = getSoup(url)
    fillUnivList(uList,soup)
    printUnivList(uList,20)
