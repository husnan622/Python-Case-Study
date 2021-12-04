# file: baca-xls.py

import xlrd
data = {}

dat_file = xlrd.open_workbook("daftar-3-pnb.xls")
dat_sheet = dat_file.sheet_by_index(0)
jum_baris = dat_sheet.nrows

for i in range(2, jum_baris): 
    data[dat_sheet.cell_value(rowx=1, colx=1)] = \
            dat_sheet.cell_value(rowx=i, colx=2)

print(data)
