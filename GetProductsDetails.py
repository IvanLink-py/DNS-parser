from bs4 import BeautifulSoup
import openpyxl
from GetProductsList import start_pos, browser


def get_ref(workbook, sheet_name):
    start = start_pos
    index = 0

    wb = openpyxl.load_workbook(workbook, read_only=True)
    sheet = wb[sheet_name]

    while True:
        value = sheet.cell(column=2, row=start+index).value

        # if value is None:
        #     return

        yield index, value

        index += 1


def get_details_by_ref(ref):
    browser.get(ref)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')

    specs = {}

    for spec in soup.find_all(class_="product-characteristics__spec"):
        spec_name = spec.find_next(class_="product-characteristics__spec-title").text.strip()
        spec_val = spec.find_next(class_="product-characteristics__spec-value").text.strip()

        specs[spec_name] = spec_val

    return specs


def write_details(workbook, sheet_name, index, details):
    def get_spec_column(shet, spec_):
        i = 4
        while True:
            value = shet.cell(row=3, column=i).value
            if value is None or value == spec_:
                return i
            i += 1

            if i > 5000:
                raise GeneratorExit()

    start = start_pos

    wb = openpyxl.load_workbook(workbook)
    sheet = wb[sheet_name]

    row = start + index
    for spec in details:
        column = get_spec_column(sheet, spec)

        sheet.cell(row=3, column=column, value=spec)
        sheet.cell(row=row, column=column, value=details[spec])

    wb.save(workbook)


def main():
    skip = 313
    gen = get_ref("Export.xlsx", "Export")
    while True:
        if skip <= 0:
            try:
                i, ref = gen.__next__()
                specs = get_details_by_ref(ref)
                print(i, ref, specs)
                write_details("Export.xlsx", "Export", i, specs)
            except StopIteration:
                print('StopIteration')
                break
            except KeyboardInterrupt:
                print('KeyboardInterrupt')
                break
            except:
                print(skip)
        else:
            gen.__next__()
            skip -= 1


if __name__ == '__main__':
    main()
