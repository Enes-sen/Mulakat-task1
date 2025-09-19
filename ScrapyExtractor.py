import requests as Resti
from ExtractType import AddToTable
from bs4 import BeautifulSoup as bs
_url = "https://www.namecheap.com/blog/"
try:
    data = Resti.get(_url,timeout=250)
    content =  data.content
    soup = bs(content,'html.parser')
    datas = soup.prettify()
    
    for sp in soup.find_all("span",class_="sds-blog-card__title-text"):
        for atr in  soup.find_all("a",class_="sds-blog-card__info-author-link"):
            for lnk in soup.find_all("a",class_="sds-blog-card__title"):
                AddToTable(sp.text,atr.text,lnk["href"])
            
except BaseException as err:
    print("Something wrong about it:",err.args)
