import pandas
import glob
from fpdf import FPDF
import time
from pathlib import Path


filepaths = glob.glob('excel/*xlsx') #grab all xlsx files in the excel file
print(filepaths)

# for item in os.listdir('.\\excel'): #option 1
for item in filepaths:  #option 2
    # df = pandas.read_excel(f'.\\excel\\{item}') #option 1
    df = pandas.read_excel(item, sheet_name='Sheet 1') #option 2
    # print(f'{df}')

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', size=18, style='B')

    # typical path will look like 'excel/10001-2023.1.18.xlsx
    filename = Path(item).stem.split('-')[0]    #Path.stem will return 10001-2023.1.18.xlsx, the split will make a list of [10001, 2023.1.18.xlsx], and choose item 0
    # print(f'filename: {filename}')
    date = Path(item).stem.split('-')[1]

    # filename, date = Path(item).stem    #Another option for using Path

    pdf.cell(w=50, h=8, txt=f'Invoice nr.{filename}', ln=1)
    # pdf.cell(w=50, h=8, txt=f'Date {time.strftime("%Y.%m.%d")}')    #option 1
    pdf.cell(w=50, h=8, txt=f'Date: {date}', align='L', ln=2)

    


    pdf.output(f'.\\invoices\\{filename}.pdf')

    for idx, row in df.iterrows():
        print(f'idx:{idx}\tProduct Id:{row["product_id"]}]\tProduct Name:{row["product_name"]}\tAmt Purchased:{row["amount_purchased"]} \
              \tPrice Per Unit: {row["price_per_unit"]}\tTotal Price:{row["total_price"]}')

