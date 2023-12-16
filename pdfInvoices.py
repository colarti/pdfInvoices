import os
import pandas
import glob



filepaths = glob.glob('excel/*xlsx')
print(filepaths)

# for item in os.listdir('.\\excel'): #option 1
for item in filepaths:  #option 2
    # df = pandas.read_excel(f'.\\excel\\{item}') #option 1
    df = pandas.read_excel(item, sheet_name='Sheet 1') #option 2
    # print(f'{df}')

    for idx, row in df.iterrows():
        print(f'idx:{idx}\tProduct Id:{row["product_id"]}]\tProduct Name:{row["product_name"]}\tAmt Purchased:{row["amount_purchased"]} \
              \tPrice Per Unit: {row["price_per_unit"]}\tTotal Price:{row["total_price"]}')

