# buka file
file_selamat = open("/program/file_io/selamat.txt", "r")

# baca isi file
selamat = file_selamat.readlines()

# cetak baris pertama
print (selamat[0])
# cetak baris kedua
print (selamat[1])

# tutup file
file_selamat.close()
