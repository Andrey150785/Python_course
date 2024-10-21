import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import itertools
import lxml
import csv
import time

HOST = "https://novosibirsk.n1.ru/"
URL = "https://novosibirsk.n1.ru/search/?rubric=flats&deal_type=sell&metro=2353440%2C2353441%2C2353442%2C2353443%2C2353444%2C2353445%2C2353446%2C2353447&metro_time=10&rooms=1&is_newbuilding=false&total_area_min=30&total_area_max=50&release_date_min=2000&floor_not_first=true&floors_count_min=10"
HEADERS = {
    "Accept":
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

def get_content(html):
    response = requests.get(html, headers=HEADERS) # получение объекта структуры сайта
    response.encoding = 'utf-8' # кодировка в читаемый формат
    soup = BeautifulSoup(response.text, 'lxml') # получение текстового представления интернет-страницы
    items = soup.find_all("div", class_="living-search-item offers-search__item")
    links_flats = []
    print(soup.find('title').text)
    # print(items)
    for item in items:
        # print(item.find('span', class_='link-text').get_text())
        link_href = item.find('a', class_='link')['href']
        links_flats.append(HOST+link_href)
    #print(links_flats)
    return links_flats, len(links_flats)
print('\n', '-----------------------', '\n')
print(get_content(URL))

