import requests
import re # 正则表达式
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        hd ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        r=requests.get(url, headers = hd)
        r.raise_for_status # 如果状态不是200，引发HTTPError
        r.encoding = r.apparent_encoding
        return r.text
    except :
        return "产生异常"

def fillUnivList(ulist, html):
    name,tamano,precio="","",""
    regionCommune ="",""
    soup = BeautifulSoup(html,"html.parser")
    for tdsujects in soup("td", "subject"): 
        name=tdsujects.find("a").string.lstrip().strip()
        if re.compile(r"(busc|compr)").search(name.lower()) !=None:
            continue
        tamano=tdsujects.find("span","icons__element-text").contents[0].strip()
        punto =tdsujects.findNextSibling("td","listing_price")
        x,precio="",""
        for x in punto.contents:
            if x!="\n":
                precio=precio+x.text.lstrip().strip()
        precio=precio.strip()

        puntoRegion =tdsujects.findNextSibling("td","clean_links")
        regionCommune = puntoRegion.find("span","region").string.lstrip().strip()+ "[" + puntoRegion.find("span","commune").string.lstrip().strip()+"]"
        
        ulist.append([name,tamano,precio,regionCommune])

def printUnivList(ulist, num):

    tplt = "{0:<60}\t{1:<15}\t{2:<30}\t{3:<30}"
    #print(tplt.format("[土地名称]","[土地大小]","[价格]", [地方]))
    print(tplt.format("[Terrero Nombre]","[Terrero Size]","[Price]","[Where]"))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],u[3]))
if __name__ =="__main__":
    uList =[]
    url ="https://www.yapo.cl/chile/comprar?ca=15_s&ret=5&pe=2&ss=5&se=6&cg=1220&&md=li"
    html = getHTMLText(url)
    fillUnivList(uList,html)
    printUnivList(uList,50)
