import pandas as pd

writer = pd.ExcelWriter('./output.xlsx', 'xlsxwriter')
file = pd.ExcelFile('./data.xlsx')

read = pd.read_excel(file)
vendor_series = read['vendor ']
price = read['price']
quantity = read['quantity']
frame = {'vendor': vendor_series, 'price': price, 'quantity': quantity}
dataFrame = pd.DataFrame(frame)


# itterate through all sheets
# sheet_list = file.sheet_names
# for x in sheet_list:
#     read = pd.read_excel(file,sheet_name=x)
#     print(read)
print(dataFrame)
writer.save()
