from requests import *
import re, os

def dl(url):
        r = get(url)
        urlv = re.search(r'\"(http[s]\:\/\/video.*?\.mp4\?.*?)\"',r.text)
        if urlv:
                print("sedang mendownload..")
                urlv = urlv.group(1).replace(";","&amp;")
                file = open("video_2.mp4","wb")
                konten = get(urlv).content
                file.write(konten)
                print("download berhasil")
        else:
                print("video tidak di temukan")

if __name__=='__main__':
        os.system("clear")
        url = input("masukkan url video: ")
        dl(url)