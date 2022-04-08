import requests

def whereisthisIP(Ip):
    url ="https://m.ip138.com/iplookup.asp?ip="
    try:
        hd ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        r=requests.get(url+Ip, headers = hd)
        r.raise_for_status # 如果状态不是200，引发HTTPError
        r.encoding = r.apparent_encoding
        print(r.text[2000:3000])
    except :
        return "产生异常"

if __name__ =="__main__":
     whereisthisIP("201.218.143.69")
