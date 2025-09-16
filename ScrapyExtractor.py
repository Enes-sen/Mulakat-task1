import requests as Resti
from ExtractType import ExtractModel
from bs4 import BeautifulSoup as bs
_url = "https://www.namecheap.com/blog/"
try:
    data = Resti.get(_url,timeout=100)
    content =  data.content
    soup = bs(content,'html.parser')
    datas = soup.prettify()
    for ar in soup.find_all("a",class_="sds-blog-card__info-author-link"):
        for tt in soup.find_all("span",class_="sds-blog-card__title-text"):
            newdata = ExtractModel()
            newdata.AddToTable(tt.text,ar.text)
            
except BaseException as err:
    print("Something wrong about it:",err.args)
    