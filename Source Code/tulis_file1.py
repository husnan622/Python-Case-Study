teks = "ini kumpulan warna"
teks_list = ["Biru", "Hijau", "Cokelat"]

f = open("/program/file_io/filewarna.txt", "w")

# tulis teks ke file
f.write(teks)
f.writelines(teks_list)

# tutup file
f.close()
