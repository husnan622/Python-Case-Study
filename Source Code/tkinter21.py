from tkinter import *
 
from tkinter import filedialog
 
file = filedialog.askopenfilename()
 
window = Tk()
 
window.title("Sistem Informasi Penjualan")
 
window.geometry('350x200')
 
file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
 
window.mainloop()
