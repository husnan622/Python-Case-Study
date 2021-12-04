# buka file
file_selamat = open("/program/file_io/selamat.txt", "r")

# baca isi file
selamat = file_selamat.readlines()

# cetak isi file dengan perulangan
for teks in selamat:
    print (teks)

# tutup file
file_selamat.close()
