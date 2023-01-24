import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pp

url = 'https://www.dns-shop.ru/product/790d362c7e3e3330/processor-amd-a6-9500e-oem/'

catalog_pages = {
    "CPU": [
        f"https://www.dns-shop.ru/"
        f"catalog/17a899cd16404e77/processory/?stock=now-today-tomorrow-later-out_of_stock&p={i}"
        for i in range(1, 33)],
    "MotherBoard": [
        f"https://www.dns-shop.ru/"
        f"catalog/17a89a0416404e77/materinskie-platy/?stock=now-today-tomorrow-later-out_of_stock&p={i}"
        for i in range(1, 62)],
    "GPU": [
        f"https://www.dns-shop.ru/"
        f"catalog/17a89aab16404e77/videokarty/?stock=now-today-tomorrow-later-out_of_stock&p={i}"
        for i in range(1, 66)],
    "RAM": [
        f"https://www.dns-shop.ru/"
        f"catalog/17a89a3916404e77/operativnaya-pamyat-dimm/?stock=now-today-tomorrow-later-out_of_stock&p={i}"
        for i in range(1, 111)],
    "PowerSupply": [
        f"https://www.dns-shop.ru/"
        f"catalog/17a89c2216404e77/bloki-pitaniya/?stock=now-today-tomorrow-later-out_of_stock&p={i}"
        for i in range(1, 78)],
    "HDD": [
        f"https://www.dns-shop.ru/"
        f"catalog/17a8914916404e77/zhestkie-diski-35/?stock=now-today-tomorrow-later-out_of_stock&p={i}"
        for i in range(1, 19)],
    "SSD": [
        f"https://www.dns-shop.ru/"
        f"catalog/8a9ddfba20724e77/ssd-nakopiteli/?stock=now-today-tomorrow-later-out_of_stock&p={i}"
        for i in range(1, 26)]

}

browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

pp(list([i.text for i in soup.find_all(class_="product-characteristics__group")]))
