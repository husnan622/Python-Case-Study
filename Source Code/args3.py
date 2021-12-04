# membuat fungsi rata-rata
def rata_rata(*data):
    banyak_data = len(data)
    jumlah_data = sum(data)
    nilai_rata_rata = float(jumlah_data) / float(banyak_data)
    return nilai_rata_rata

print (rata_rata(2,4,1,2,4,1,2,3,4,5,1,8,2))
