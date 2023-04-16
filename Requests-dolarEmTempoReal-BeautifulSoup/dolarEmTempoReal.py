import requests
from bs4 import BeautifulSoup  #pip install beautifulsoup4
#Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
page = requests.get("https://www.google.com/search?q=dolar&oq=dolar&aqs=chrome.0.69i59j0i131i433i512l7j0i512j0i131i433i512.2238j0j15&sourceid=chrome&ie=UTF-8",headers=headers)

# print(page.content)


soup = BeautifulSoup(page.content,'html.parser')

atributos = {'class':'DFlfde SwHCTb'}
valor_dolar = soup.find_all('span',attrs=atributos)[0]
#valor_dolar = soup.find_all('span',class_="DFlfde SwHCTb")

print(valor_dolar)
print(valor_dolar.get_text())
print(valor_dolar.text)
print(valor_dolar['data-value'])