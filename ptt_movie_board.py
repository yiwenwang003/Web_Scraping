import requests
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/movie/index.html'

def getMovie():
    with open('MovieArticle_title.txt', mode='w', encoding='utf-8') as f:
        resp= requests.get(url)
        soup= BeautifulSoup(resp.text, 'html.parser')
        
        article_titles= soup.find_all('div', class_='title')
        
        for title in article_titles:
            if title !=None:
                f.write(title.a.string+'\n')
          
        
getMovie()
        