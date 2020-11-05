
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/Books/b/?ie=UTF8&node=976389031&ref_=nav_cs_books'
code = requests.get(url)
plain = code.text
s = BeautifulSoup(plain, "html.parser")

xyz =  s.find('div',class_='a-row a-expander-container a-expander-extend-container')
i = 0
for book in xyz:
    print(str(i) +  " " + book.text+'\n')
    i = i + 1


href_home = s.findAll("a",{"class" : "a-link-normal s-ref-text-link"})

cats_href = []
for hrefs in href_home:
    cats_href.append(hrefs["href"])  

bookname = input('Type the number of your book category: ')
print('\n The book list is as follows : \n')       

code2 = requests.get(cats_href[int(bookname)])
plain2 = code2.text
s2 = BeautifulSoup(plain2, "html.parser")

xyz2 = s2.findAll('span',class_='a-truncate a-size-base')
for book2 in xyz2:
    print(book2.text+ '\n')
            
