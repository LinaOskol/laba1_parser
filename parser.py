import requests
from bs4 import BeautifulSoup

url = 'https://www.omgtu.ru/general_information/faculties/'
page = requests.get(url)
print(page.status_code)

faculties = []
allFaculties = []
file = open('result.txt', 'w')
soup = BeautifulSoup(page.text, "html.parser")
# print(soup)
allFaculties = soup.find_all('div', class_='main__content')
for facult in allFaculties:
    if facult.find('li') is not None:
        faculties.append(facult.text)
for facult in faculties:
    file.write(facult)

file.close()
