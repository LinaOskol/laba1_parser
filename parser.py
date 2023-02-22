from bs4 import BeautifulSoup
import requests
url='https://www.omgtu.ru/general_information/faculties/'
page=requests.get(url)
print(page.status_code)

filteredNews = []
allNews = []
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
allNews = soup.findAll('', class_='')
print(allNews)