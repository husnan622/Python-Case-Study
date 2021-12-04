# membuat fungsi dengan parameter *args
def kirim_sms(*nomer):
    print (nomer)

# membuat fungsi dengan parameter **kwargs
def tulis_sms(**isi):
    print (isi)

# Pemanggilan fungsi *args
kirim_sms(123, 888, 4444)

# pemanggilan fungsi **kwargs
tulis_sms(tujuan=123, pesan="Hallo Apa Kabar")
