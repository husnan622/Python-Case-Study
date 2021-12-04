# file: tulis-xls.py

import xlwt

data1 = ["PT. Maju", "PT. Jaya"]
data2 = ["Bandung", "Balikpapan"]

wb = xlwt.Workbook()
ws = wb.add_sheet("Data Penerbit")

ws.write(0, 0, "Nama Penerbit")
ws.write(0, 1, "Nama Kota")

i= 1
for x,y in zip(data1, data2):
    ws.write(i, 0, x)
    ws.write(i, 1, y)
    i += 1

print("Peringatan! Data Telah Tersimpan")
wb.save("data-pnb2.xls")

    
