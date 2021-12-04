# buka file
file_selamat = open("/program/file_io/selamat.txt", "r")

# baca isi file
selamat = file_selamat.read()

# cetak isi file
print (selamat)

# tutup file
file_selamat.close()
