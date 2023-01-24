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
    pass


def write_details(details):
    pass


def main():
    for i, ref in get_ref("Export.xlsx", "Export"):
        print(i, ref)


if __name__ == '__main__':
    main()
