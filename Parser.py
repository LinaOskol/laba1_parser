import requests
from bs4 import BeautifulSoup


def parse():
    url = 'https://www.omgtu.ru/general_information/faculties/'  # адрес сайта
    page = requests.get(url)  # делаем запрос на сайт
    print(page.status_code)  # вывод ответа сайта, если 200 то все успешно
    faculties = []
    allFaculties = []
    file = open('result.txt', 'w')  # открываем файл с параметром записи в него, перед записью файл будет очищен
    soup = BeautifulSoup(page.text, "html.parser")  # передаем нашу страницу в bs4
    allFaculties = soup.find_all('div', id='pagecontent')  # ищем контейнер с нужным классом

    for facult in allFaculties:
        faculties.append(facult.find('ul').text)  # ищем теги ul и вносим в массив

    faculties = faculties[0][0:len(faculties[0]) - 3].split(
        '\n')  # разделяем по \n нулевой элемент,чтобы получить массив

    for facult in faculties:
        if facult != '':
            file.write(facult + '\n')

    file.close()
