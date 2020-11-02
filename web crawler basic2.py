
import requests
from bs4 import BeautifulSoup

no = input("Enter a page number from 3 to 10:")
num=str(no)
nom=int(num)
WebUrl = 'https://www.amazon.in/s?i=stripbooks&bbn=976390031&rh=n%3A976389031%2Cn%3A1318158031%2Cp_n_feature_three_browse-bin%3A9141482031&dc&page=3&fst=as%3Aoff&qid=1604303101&rnid=976390031&ref=sr_pg_'+num

def web(i,WebUrl):
     if(i>2):
          url = WebUrl
          code = requests.get(url)
          plain = code.text
          s = BeautifulSoup(plain, "html.parser")
          print('The links for books: ')
          for link in s.findAll('a', {'class':'a-link-normal s-no-outline','target':'_blank'}):
               tet_2 = link.get('href')
               print(tet_2)
          for price in s.find_all('span',class_ = 'a-price-whole'):
               itemPricetext = price.text
               print(itemPricetext)

for i in range(3,nom+1):
    web(i,WebUrl)

