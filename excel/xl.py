import pandas as pd

writer = pd.ExcelWriter('excel/output.xlsx', 'xlsxwriter')
file = pd.ExcelFile('excel/data.xlsx')
file2 = pd.ExcelFile('excel/data2.xlsx')


read = pd.read_excel(file,skiprows=1)
col_lis = read.columns
frame = {}
read['Date'] = pd.to_datetime(read['Date'])
need = ['Date','Item Name','Grams/ML','Buying Price','Buying Quantity']
for col in col_lis:
    # print(col.strip())
    if col.strip() in need:
        frame.update({col:read[col]})
    else:
        continue
# excel with selling price

# retailo sp
need2 = ['date','sku','selling']
retailo = pd.read_excel(file2,skiprows=1,nrows=24)
retailo['Date'] = pd.to_datetime(retailo['Date'])
frame2 = {}
for col in retailo.columns:
    if col.strip().lower() in need2:
        frame2.update({col:retailo[col]})

dataFrame_without_sellingprice = pd.DataFrame(frame)
retailo = pd.DataFrame(frame2)

for x in enumerate(retailo['Date']):
    same_date = pd.DataFrame()
    


writer.save()
