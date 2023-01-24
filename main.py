import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pp


url = 'https://www.dns-shop.ru/product/790d362c7e3e3330/processor-amd-a6-9500e-oem/'

browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
soup = BeautifulSoup(html, 'lxml')

pp(list([i.text for i in soup.find_all(class_="product-characteristics__group")]))
