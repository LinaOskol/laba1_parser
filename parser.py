import requests
from bs4 import BeautifulSoup

url = 'https://www.omgtu.ru/general_information/faculties/'
page = requests.get(url)
print(page.status_code)

faculties = []
allFaculties = []
file = open('result.txt', 'w')
soup = BeautifulSoup(page.text, "html.parser")

allFaculties = soup.find_all('div', id='pagecontent')
for facult in allFaculties:
    faculties.append(facult.find('ul').text)
    
for facult in faculties:
    file.write(facult)

file.close()
