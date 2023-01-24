import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from pprint import pp
import openpyxl


def get_ref(workbook, sheet_name):
    start = 4
    index = 0

    wb = openpyxl.load_workbook(workbook)
    sheet = wb[sheet_name]

    while True:
        value = sheet[f"B{start + index}"].value

        if value is None:
            return

        yield index, value

        index += 1


def get_details_by_ref(ref):
    browser = webdriver.Chrome()
    browser.get(ref)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')

    specs = {}

    for spec in soup.find_all(class_="product-characteristics__spec"):
        spec_name = spec.find_next(class_="product-characteristics__spec-title").text.strip()
        spec_val = spec.find_next(class_="product-characteristics__spec-value").text.strip()

        specs[spec_name] = spec_val

    return specs


def write_details(details):
    pass


def main():
    # for i, ref in get_ref("Export.xlsx", "Export"):
    #     print(i, ref)

    pp(get_details_by_ref('https://www.dns-shop.ru/product/f4db8aab61473120'))


if __name__ == '__main__':
    main()
