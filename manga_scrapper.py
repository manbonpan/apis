import urllib.request
from urllib.request import Request
import re
import time
import time,subprocess,discord
import asyncio
import sys
# Scrapping
exception=['https://horriblesubs.info/release-schedule/','https://discord.gg/TzuEpf8','reddit.com','https://www.reddit.com/r/4anime']

def initialhtml(query):
    query=query.replace(' ','_')
    
    req = Request('https://mangakakalot.com/search/story/{0}'.format(query),headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'})
    with urllib.request.urlopen(req) as response:
       html = response.read()
    return html.decode()
linkz=re.compile(r'<a[^>]* href="([^"]*)"')
pattern=re.compile('(<a rel="nofollow".*>)')
chapp=re.compile('(<a rel="nofollow" class="chapter-name text-nowrap".*>)')
imgs=re.compile('[\=,\(][\"|\'].[^\=\"]+\.(?i:jpg|gif|png|bmp)[\"|\']')
forbidden=['https://mangakakalot.com/manga_list?','register','login']
def links(obj):
    x=pattern.findall(obj)
    linkarr=[]
    for i in x:
        if 'https://mangakakalot.com/manga_list?'  in i:
            continue
        else:
            if 'login'  in i or 'btn-register' in i:
                continue
            else:
                if 'manga' in i:
                    if 'chapter' in i:
                        continue
                    dud=link=linkz.findall(i)[0]
                    linkarr.append(dud)
                else:
                    continue


    return linkarr
                    
def chapscrapper(url):
    linkarr=[]
    req = Request(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'})
    with urllib.request.urlopen(req) as response:
       html = response.read()
    obj=html.decode()
    chaps=chapp.findall(obj)
    for i in chaps:
        dud=linkz.findall(i)[0]
        linkarr.append(dud)
        
    return [len(chaps),linkarr[::-1]]
    
    
    
    
def imgscrpr(url):
    linkarr=[]
    req = Request(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'})
    with urllib.request.urlopen(req) as response:
       html = response.read()
    obj=html.decode()
    img=imgs.findall(obj)
    for i in img:
        if 'mkklcdnv' in i:
            u=i.replace('=','')
            x=u.replace("'","")
            j=x.replace('"','')
            linkarr.append(j)
    
    
        
            
    return linkarr
    
    
    
                

        

    

    

def initiator(query:str,chapter:int):
    obj=initialhtml(query)
    x=links(obj)
    y=chapscrapper(x[0])
    z=imgscrpr(y[1][chapter])
    return z


def fuckit(name:str,chapter:int=1):
        count=0
        initial=time.time()
        links=initiator(name,chapter)
        filename = f"{name}/{chapter}/"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        for i in links:
            count=count+1
            req = Request(i,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70'})
            req.add_header('Referer', 'https://mangakakalot.com/')
            with urllib.request.urlopen(req) as response:
               html = response.read()
            file=open(f'{name}/{chapter}/{count}.jpg','wb')
            file.write(html)
            file.close




linkz=re.compile(r'<a[^>]* href="([^"]*)"')
pattern=re.compile('(<a rel="nofollow".*>)')
chapp=re.compile('(<a rel="nofollow" class="chapter-name text-nowrap".*>)')
imgs=re.compile('[\=,\(][\"|\'].[^\=\"]+\.(?i:jpg|gif|png|bmp)[\"|\']')
forbidden=['https://mangakakalot.com/manga_list?','register','login']

if(len(sys.argv) > 2):
    print(f"Getting {sys.argv[1]}'s Chapter {sys.argv[2]}")
else:
    print("fetching multiple chapters...")

for _ in range(int(sys.argv[2]),int(sys.argv[2])+int(sys.argv[3])):
    fuckit(sys.argv[1],_)
