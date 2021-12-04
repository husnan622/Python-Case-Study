# buka file
file_selamat = open("/program/file_io/selamat.txt", "r")

# baca isi file
print (file_selamat.readlines())

# tutup file
file_selamat.close()
