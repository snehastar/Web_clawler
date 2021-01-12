import requests
from bs4 import BeautifulSoup
url = 'https://www.amazon.in/Books/b/?ie=UTF8&node=976389031&ref_=nav_cs_books'
#get the url
code = requests.get(url)
plain = code.text

#extract the html file of the source code of web page
s = BeautifulSoup(plain, "html.parser")

#write the path/class to which the book block belongs

xyz =  s.findAll('a',{"class":"a-color-base a-spacing-none a-link-normal acs-product-block__product-title"})
j=1
for book in xyz:
   link = book.get('href')
   print(str(j)+'- '+'https://www.amazon.in'+link)
   j=j+1
    
xyz =  s.findAll('span',{'class':"a-truncate a-size-base"})
i=1
for book in xyz:
    bookname = book.text
    print(str(i)+': '+ bookname)
    i=i+1
