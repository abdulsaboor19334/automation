import pandas as pd

file_without_sp = pd.ExcelFile('data.xlsx')
excel_without_sp = pd.read_excel(file_without_sp, skiprows=1)
excel_without_sp.dropna(subset=['Date'],inplace=True)
col_lis = excel_without_sp.columns
frame_without_sp = {}
excel_without_sp['Date'] = pd.to_datetime(excel_without_sp['Date'])
need_from_excel_without_sp = ['Date', 'Item Name',
                              'Grams/ML', 'Buying Price', 'Buying Quantity']

file_with_sp = pd.ExcelFile('data2.xlsx')
need_from_excel_with_sp = ['date', 'sku', 'selling']
retailo = pd.read_excel(file_with_sp, skiprows=1, nrows=24)
retailo['Date'] = pd.to_datetime(retailo['Date'])
bazaar = pd.read_excel(file_with_sp, skiprows=28, nrows=47)
bazaar['Date'] = pd.to_datetime(bazaar['Date'])
jugnoo = pd.read_excel(file_with_sp, skiprows=82, nrows=6)
jugnoo['Date'] = pd.to_datetime(jugnoo['Date'])
retailo_frame = {}
bazaar_frame = {}
jugnoo_frame = {}

# extract needed rows
for col in col_lis:
    if col.strip() in need_from_excel_without_sp:
        frame_without_sp.update({col: excel_without_sp[col]})

for col in retailo.columns:
    if col.lower().strip() in need_from_excel_with_sp:
        retailo_frame.update({col: retailo[col]})
        bazaar_frame.update({col: bazaar[col]})
        jugnoo_frame.update({col: jugnoo[col]})

dataFrame_without_sellingprice = pd.DataFrame(frame_without_sp)
retailo_df = pd.DataFrame(retailo_frame)
bazaar_df = pd.DataFrame(bazaar_frame)
jugnoo_df = pd.DataFrame(jugnoo_frame)

for index,row in excel_without_sp.iterrows():
    pass

print(jugnoo_df['Date'][0])
