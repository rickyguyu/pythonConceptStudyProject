import requests
import os
def getHttpPicturefile(url):
    try:
        hd ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        root ="C://Users//Ricky//Documents//python source//pic//"
        path = root + url.split("/")[-1]
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(url, headers = hd)
            r.raise_for_status # 如果状态不是200，引发HTTPError
            with open(path, "wb") as f:
                f.write(r.content)
            f.close()
            print("文件已创建")
        else:
            print("文件已存在")
    except :
        f.close()
        return "产生异常"
        
            

def getHttpPicturefilename(url, filename):
    try:
        hd ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        root ="C://Users//Ricky//Documents//python source//pic//"
        path = root + filename
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r=requests.get(url, headers = hd)
            r.raise_for_status # 如果状态不是200，引发HTTPError
            with open(path, "wb") as f:
                f.write(r.content)
            print("文件已创建")
        else:
            print("文件已存在")
    except :
        return "产生异常"

   

if __name__ =="__main__":
    url ="http://www.unitedlogdom.com/files/4713/8108/1574/logo_dominicana.png"
    #url = "https://www.youtube.com/watch?v=1nbq-bXLEEo&feature=youtu.be&list=LLF4RJ5gk0n_7Tyud18SWKHQ"
    getHttpPicturefile(url)
    
