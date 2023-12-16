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
    pdf.cell(w=50, h=8, txt=f'Date: {date}', align='L', ln=1)
    pdf.ln(20)


    sum = 0     #sum of total price
    # #creating the table from the excel file
    headers = list(df.columns)
    # headers = [header.replace('_', ' ').title() for header in headers]  #another option using list comprehension

    print(f'headers:{headers}')
    pdf.set_font(family='Times', size=10, style='B')
    # pdf.cell(w=23, h=10, border=True, align='C', txt='Product Id')
    # pdf.cell(w=50, h=10, border=True, align='C', txt='Product Name')
    # pdf.cell(w=30, h=10, border=True, align='C', txt='Count')
    # pdf.cell(w=30, h=10, border=True, align='C', txt='Price Per Unit')
    # pdf.cell(w=35, h=10, border=True, align='C', txt='Total Price', ln=1)

    pdf.cell(w=23, h=10, border=True, align='C', txt=headers[0].replace('_', ' ').title())
    pdf.cell(w=50, h=10, border=True, align='C', txt=headers[0].replace('_', ' ').title())
    pdf.cell(w=30, h=10, border=True, align='C', txt=headers[0].replace('_', ' ').title())
    pdf.cell(w=30, h=10, border=True, align='C', txt=headers[0].replace('_', ' ').title())
    pdf.cell(w=35, h=10, border=True, align='C', txt=headers[0].replace('_', ' ').title(), ln=1)

    for idx, row in df.iterrows():
        pdf.set_font(family='Times', size=10, style='B')
        pdf.set_text_color(0,0,0)
        
        pdf.cell(w=23, h=10, border=True, align='C', txt=f'{row["product_id"]}')
        pdf.cell(w=50, h=10, border=True, align='C', txt=f'{row["product_name"]}')
        pdf.cell(w=30, h=10, border=True, align='C', txt=f'{row["amount_purchased"]}')
        pdf.cell(w=30, h=10, border=True, align='C', txt=f'{row["price_per_unit"]}')
        pdf.cell(w=35, h=10, border=True, align='C', txt=f'{row["total_price"]}', ln=1)
        sum += float(row['total_price'])
    
    
    pdf.ln(40)
    pdf.set_font(family='Times', size=20)
    pdf.cell(w=0, h=16, txt=f'Thank you for your purchase, your TOTAL: ${sum}', border=0, align='L', ln=1)
    pdf.ln(5)
    pdf.set_font(family='Times', style='BI')
    pdf.cell(w=0, h=20, border=0, txt='** ECMO Corp **')
    

    pdf.output(f'.\\invoices\\{filename}.pdf')

