from tkinter import *
import sqlite3

class KelasPemrograman:
    def __init__(self,root):
        
        # mahasiswa
        self.lbmahasiswa = Label(root,text="Rekap Nilai Kelas </Pemrograman>",font="Gungsuh 30",bg="#0098d0")
        self.lbmahasiswa.grid(row=0,column=0,columnspan=7,sticky=W+E+N+S,ipady=20)
        # daftar mahasiswa
        self.lbdtrmhs = Label(root,text="Daftar Mahasiswa:",font="Arial 10",bg="#01bbff")
        self.lbdtrmhs.grid(row=1,column=0,sticky=W+S,padx=5)
        self.listmahasiswa_var = StringVar()
        self.listmahasiswa = Listbox(root,listvariable=self.listmahasiswa_var,font="Arial 15")
        self.listmahasiswa.grid(row=2,column=0,rowspan=4,padx=5,pady=5)
        self.listmahasiswa.bind('<<ListboxSelect>>', self.onListboxPilih)

        # nama dan nim mahasiswa
        self.lbmhs = Label(root,text="Detail Mahasiswa:",font="Arial 10",bg="#01bbff")
        self.lbmhs.grid(row=1,column=1,sticky=W+S,padx=5)
        self.lbmahasiswa = Label(root,text="Nama",font="Arial 10",bg="#01bbff")
        self.lbmahasiswa.grid(row=3,column=1,sticky=E)
        self.mahasiswa_var = StringVar()
        self.mahasiswa = Label(root, bd=1, relief=SUNKEN, textvariable=self.mahasiswa_var,font="Arial 10 bold", width=20,bg="#01bbff")       
        self.mahasiswa.grid(row=3,column=2,sticky=W,padx=5,pady=15)

        self.lbnim = Label(root,text="NIM",font="Arial 10",bg="#01bbff")
        self.lbnim.grid(row=3,column=3,sticky=E)        
        self.nim_var = StringVar()
        self.nim = Label(root, bd=1, relief=SUNKEN, textvariable=self.nim_var,font="Arial 10 bold", width=20,bg="#01bbff")
        self.nim.grid(row=3,column=4,sticky=W,padx=5)

        # nilai mahasiswa
        self.lbnilai_tugas = Label(root,text="Nilai Tugas",font="Arial 10 bold",bg="#01bbff")
        self.lbnilai_tugas.grid(row=4,column=1,sticky=W+E+N+S)         
        self.nilai_tugas_var = IntVar()
        self.nilai_tugas = Label(root, bd=1, relief=SUNKEN, textvariable=self.nilai_tugas_var,font="Arial 20",width=9,bg="#fff")
        self.nilai_tugas.grid(row=5,column=1,sticky=W+E+N+S,padx=5,pady=15)

        self.lbnilai_uts = Label(root,text="Nilai UTS",font="Arial 10 bold",bg="#01bbff")
        self.lbnilai_uts.grid(row=4,column=2,sticky=W+E+N+S)         
        self.nilai_uts_var = IntVar()
        self.nilai_uts = Label(root, bd=1, relief=SUNKEN, textvariable=self.nilai_uts_var,font="Arial 20",width=7,bg="#fff")
        self.nilai_uts.grid(row=5,column=2,sticky=W+E+N+S,padx=5,pady=15)

        self.lbnilai_uas = Label(root,text="Nilai UAS",font="Arial 10 bold",bg="#01bbff")
        self.lbnilai_uas.grid(row=4,column=3,sticky=W+E+N+S)         
        self.nilai_uas_var = IntVar()
        self.nilai_uas = Label(root, bd=1, relief=SUNKEN, textvariable=self.nilai_uas_var,font="Arial 20",width=9,bg="#fff")
        self.nilai_uas.grid(row=5,column=3,sticky=W+E+N+S,padx=5,pady=15)

        self.lbakhir = Label(root,text="Nilai Akhir",font="Arial 10 bold",bg="#01bbff")
        self.lbakhir.grid(row=4,column=4,sticky=W+E+N+S)         
        self.nilai_akhir_var = IntVar()
        self.akhir = Label(root, bd=1, relief=SUNKEN,textvariable=self.nilai_akhir_var,font="Arial 20",width=7,bg="#fff")
        self.akhir.grid(row=5,column=4,sticky=W+E+N+S,padx=5,pady=15)

        self.lbmutu = Label(root,text="MUTU",font="Arial 10",bg="#01bbff")
        self.lbmutu.grid(row=3,column=5,sticky=E)        
        self.mutu_var = StringVar()
        self.mutu = Label(root, textvariable=self.mutu_var,font="Arial 40 bold",width=3,bg="#01bbff")
        self.mutu.grid(row=4,column=5,rowspan=2,columnspan=2,sticky=W+E+N+S,padx=5, pady=10)
        
        # jumlah mahasiswa
        self.statusMahasiswa_var = StringVar()
        self.statusMahasiswa = Label(root, bd=1, relief=SUNKEN, textvariable=self.statusMahasiswa_var,bg="#01bbff")
        self.statusMahasiswa.grid(row=6,column=0,sticky=W+E+N+S,padx=5,pady=5)

        # status kelulusan
        self.statusKelulusan_var = StringVar()
        self.statusKelulusan = Label(root, bd=1, relief=SUNKEN, textvariable=self.statusKelulusan_var,font="Arial 40 bold",bg="#01bbff")
        self.statusKelulusan.grid(row=6,column=1,columnspan=6,sticky=W+E+N+S,padx=5,pady=5)
        
        # tampilan menu1
        self.menubar = Menu(root)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Tambah", command=self.tambahData)
        filemenu.add_command(label="Cari", command=self.cariData)
        filemenu.add_command(label="Edit", command=self.editData)
        filemenu.add_command(label="Hapus", command=self.hapusData)
        filemenu.add_separator()
        filemenu.add_command(label="Keluar", command=root.destroy)
        self.menubar.add_cascade(label="File", menu=filemenu)

        infomenu = Menu(self.menubar, tearoff=0)
        infomenu.add_command(label="Tentang Saya", command=self.adityowartabone)
        self.menubar.add_cascade(label="Info", menu=infomenu)
        root.config(menu=self.menubar)


        # tampilkan data di daftar pemrograman
        self.rows = self.ambilData()
        self.tampilListData()

        # otomatis ke baris pertama
        self.listmahasiswa.select_set(0)
        self.listmahasiswa.event_generate("<<ListboxSelect>>") 

    # TENTANG SAYA
    def adityowartabone(self):
        class ChildWindow:
            def __init__(self,root2):
                self.nama = Label(root2,text="Nama : Adityo Wartabone",font="Courier 20 bold",bg="#fff",fg="#ff9d00")
                self.nama.grid(row=0,column=0,sticky=W)
                self.nim = Label(root2,text="NIM  : 14021106063",font="Courier 20 bold",bg="#fff",fg="#ff9d00")
                self.nim.grid(row=1,column=0,sticky=W)
                self.mk = Label(root2,text="MK   : Pemrograman 2",font="Courier 20 bold",bg="#fff",fg="#ff9d00")
                self.mk.grid(row=2,column=0,sticky=W)
                self.judul = Label(root2,text="Judul: Rekap Nilai Kelas Pemrograman",font="Courier 20 bold",bg="#fff",fg="#ff9d00")
                self.judul.grid(row=3,column=0,sticky=W)
                self.gambar = PhotoImage(file="14021106063.gif")
                self.gambar2 = Label(root2, image=self.gambar,bg="#fff")
                self.gambar2.grid(row=0,column=1,rowspan=4)
                
        root2 = Toplevel()
        test2 = ChildWindow(root2)
        root2.configure(bg="#fff")
        root2.title("Tentang Saya")
        root2.focus_set()
        root2.grab_set()
        root2.transient()
        root2.wait_window(root2)
        
    def ambilData(self):
        db = sqlite3.connect("informatika.db")
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pemrograman")
        rows = cursor.fetchall()
        return rows

    def tampilListData(self):
        self.listmahasiswa.delete(0,self.listmahasiswa.size())
        for row in self.rows:
            self.listmahasiswa.insert(END,row[1])          
        self.statusMahasiswa_var.set("Jumlah Mahasiswa: "+str(len(self.rows)))

    def tampilDetailData(self,index):
        self.id_terpilih = self.rows[index][0]
        self.mahasiswa_var.set(self.rows[index][1])
        self.nim_var.set(self.rows[index][2])
        self.nilai_tugas_var.set(self.rows[index][3])
        self.nilai_uts_var.set(self.rows[index][4])
        self.nilai_uas_var.set(self.rows[index][5])
        self.nilai_akhir_var.set(self.rows[index][6])
        self.mutu_var.set(self.rows[index][7])
        self.statusKelulusan_var.set(self.rows[index][8])
        if self.rows[index][8]=="♥ LULUS":
            self.statusKelulusan = Label(root, bd=1, relief=SUNKEN, textvariable=self.statusKelulusan_var,bg="#adf89f",font="Gabriola 20 bold")
        else:
            self.statusKelulusan = Label(root, bd=1, relief=SUNKEN, textvariable=self.statusKelulusan_var,bg="#f89f9f",font="Gabriola 20 bold")
        self.statusKelulusan.grid(row=6,column=1,columnspan=6,sticky=W+E+N+S,padx=5,pady=5)

    def onListboxPilih(self,evt):
        w = evt.widget
        index = int(w.curselection()[0])
        self.index_terpilih = index
        self.tampilDetailData(self.index_terpilih)
      
    # CREATE NEW DATA
    def tambahData(self):
        class ChildWindow:
            def __init__(self,root2):
                self.lbmahasiswa = Label(root2,text="Mahasiswa")
                self.lbmahasiswa.grid(row=0,column=0,sticky=E,padx=5)
                self.mahasiswa_var = StringVar()
                self.mahasiswa = Entry(root2,textvariable=self.mahasiswa_var)       
                self.mahasiswa.grid(row=0,column=1)

                self.lbnim = Label(root2,text="NIM")
                self.lbnim.grid(row=1,column=0,sticky=E,padx=5)        
                self.nim_var = StringVar()
                self.nim = Entry(root2,textvariable=self.nim_var)
                self.nim.grid(row=1,column=1)

                self.lbnilai_tugas = Label(root2,text="Nilai Tugas")
                self.lbnilai_tugas.grid(row=2,column=0,sticky=E,padx=5)         
                self.nilai_tugas_var = IntVar()
                self.nilai_tugas = Entry(root2,textvariable=self.nilai_tugas_var)
                self.nilai_tugas.grid(row=2,column=1)

                self.lbnilai_uts = Label(root2,text="Nilai UTS")
                self.lbnilai_uts.grid(row=3,column=0,sticky=E,padx=5)         
                self.nilai_uts_var = IntVar()
                self.nilai_uts = Entry(root2,textvariable=self.nilai_uts_var)
                self.nilai_uts.grid(row=3,column=1)

                self.lbnilai_uas = Label(root2,text="Nilai UAS")
                self.lbnilai_uas.grid(row=4,column=0,sticky=E,padx=5)         
                self.nilai_uas_var = IntVar()
                self.nilai_uas = Entry(root2,textvariable=self.nilai_uas_var)
                self.nilai_uas.grid(row=4,column=1,sticky=E,padx=5)
                
                self.btSimpan = Button(root2, text="Simpan",command=self.simpanData)
                self.btSimpan.grid(row=5,column=1,sticky=E,pady=10)
                self.btKembali = Button(root2, text="Kembali",command=root2.destroy)
                self.btKembali.grid(row=5,column=1,sticky=W,pady=10)

                self.mahasiswa.focus()

            def simpanData(self):
                db = sqlite3.connect("informatika.db")
                cursor = db.cursor()
                mahasiswa = self.mahasiswa_var.get()
                nim = self.nim_var.get()
                nilai_tugas = self.nilai_tugas_var.get()
                nilai_uts = self.nilai_uts_var.get()
                nilai_uas = self.nilai_uas_var.get()
                nilai_akhir = (self.nilai_tugas_var.get()*0.25)+(self.nilai_uts_var.get()*0.35)+(self.nilai_uas_var.get()*0.4)
                mutu=""
                if nilai_akhir>=80:
                    mutu="A"
                elif nilai_akhir>=75:
                    mutu="B+"
                elif nilai_akhir>=70:
                    mutu="B"
                elif nilai_akhir>=65:
                    mutu="C+"
                elif nilai_akhir>=55:
                    mutu="C"
                elif nilai_akhir>=35:
                    mutu="D"
                elif nilai_akhir<35:
                    mutu="E"
                    
                if ((mutu=="D") | (mutu=="E")):
                    kelulusan="❌ TIDAK LULUS"
                else:
                    kelulusan="♥ LULUS"
                
                cursor.execute('''INSERT INTO pemrograman(nama,nim,nilai_tugas,nilai_uts,nilai_uas,nilai_akhir,mutu,kelulusan)
                  VALUES(?,?,?,?,?,?,?,?)''',(mahasiswa,nim,nilai_tugas,nilai_uts,nilai_uas,nilai_akhir,mutu,kelulusan))
                db.commit()
                messagebox.showinfo(message='Data sudah disimpan')
                self.kosongkanEntry()

            def kosongkanEntry(self):
                self.mahasiswa_var.set("")
                self.nim_var.set("")
                self.nilai_tugas_var.set("")
                self.nilai_uts_var.set("")
                self.nilai_uas_var.set(0)
                self.mahasiswa.focus()

        root2 = Toplevel()
        test2 = ChildWindow(root2)
        root2.title("Tambah Data pemrograman")
        root2.focus_set()
        root2.grab_set()
        root2.transient()
        root2.wait_window(root2)
        #tampilkan lagi data yang terupdate
        self.rows = self.ambilData()
        self.tampilListData()
        # otomatis ke baris pertama
        self.listmahasiswa.select_set(len(self.rows)-1)
        self.listmahasiswa.event_generate("<<ListboxSelect>>") 

    # UPDATE DATA 
    def editData(self):
        class ChildWindow:
            def __init__(self,root2,id_terpilih):

                self.id_terpilih = id_terpilih
                self.lbmahasiswa = Label(root2,text="Mahasiswa")
                self.lbmahasiswa.grid(row=0,column=0,sticky=E,padx=5)
                self.mahasiswa_var = StringVar()
                self.mahasiswa = Entry(root2,textvariable=self.mahasiswa_var)       
                self.mahasiswa.grid(row=0,column=1)

                self.lbnim = Label(root2,text="NIM")
                self.lbnim.grid(row=1,column=0,sticky=E,padx=5)        
                self.nim_var = StringVar()
                self.nim = Entry(root2,textvariable=self.nim_var)
                self.nim.grid(row=1,column=1)

                self.lbnilai_tugas = Label(root2,text="Nilai Tugas")
                self.lbnilai_tugas.grid(row=2,column=0,sticky=E,padx=5)         
                self.nilai_tugas_var = IntVar()
                self.nilai_tugas = Entry(root2,textvariable=self.nilai_tugas_var)
                self.nilai_tugas.grid(row=2,column=1)

                self.lbnilai_uts = Label(root2,text="Nilai UTS")
                self.lbnilai_uts.grid(row=3,column=0,sticky=E,padx=5)         
                self.nilai_uts_var = IntVar()
                self.nilai_uts = Entry(root2,textvariable=self.nilai_uts_var)
                self.nilai_uts.grid(row=3,column=1)

                self.lbnilai_uas = Label(root2,text="Nilai UAS")
                self.lbnilai_uas.grid(row=4,column=0,sticky=E,padx=5)         
                self.nilai_uas_var = IntVar()
                self.nilai_uas = Entry(root2,textvariable=self.nilai_uas_var)
                self.nilai_uas.grid(row=4,column=1,sticky=E,padx=5)
                self.nilai_akhir_var=IntVar()
                self.mutu_var=StringVar()
                self.statusKelulusan_var=StringVar()
                self.btSimpan = Button(root2, text="Simpan",command=self.simpanData)
                self.btSimpan.grid(row=5,column=1,sticky=E)
                self.btKembali = Button(root2, text="Kembali",command=root2.destroy)
                self.btKembali.grid(row=5,column=1,sticky=W)

                self.ambilData()

            def ambilData(self):
                db = sqlite3.connect("informatika.db")
                cursor = db.cursor()
                cursor.execute("SELECT * FROM pemrograman WHERE id=%d" % self.id_terpilih)
                row = cursor.fetchone()
                self.mahasiswa_var.set(row[1])
                self.nim_var.set(row[2])
                self.nilai_tugas_var.set(row[3])
                self.nilai_uts_var.set(row[4])
                self.nilai_uas_var.set(row[5])
                self.nilai_akhir_var.set(row[6])
                self.mutu_var.set(row[7])
                self.statusKelulusan_var.set(row[8])
                
            def simpanData(self):
                db = sqlite3.connect("informatika.db")
                cursor = db.cursor()
                id_terpilih = self.id_terpilih
                mahasiswa = self.mahasiswa_var.get()
                nim = self.nim_var.get()
                nilai_tugas = self.nilai_tugas_var.get()
                nilai_uts = self.nilai_uts_var.get()
                nilai_uas = self.nilai_uas_var.get()

                nilai_akhir = (self.nilai_tugas_var.get()*0.25)+(self.nilai_uts_var.get()*0.35)+(self.nilai_uas_var.get()*0.4)

                mutu=""
                if nilai_akhir>=80:
                    mutu="A"
                elif nilai_akhir>=75:
                    mutu="B+"
                elif nilai_akhir>=70:
                    mutu="B"
                elif nilai_akhir>=65:
                    mutu="C+"
                elif nilai_akhir>=55:
                    mutu="C"
                elif nilai_akhir>=35:
                    mutu="D"
                elif nilai_akhir<35:
                    mutu="E"
                    
                if ((mutu=="D") | (mutu=="E")):
                    kelulusan="❌ TIDAK LULUS"
                else:
                    kelulusan="♥ LULUS"
                
                cursor.execute('''UPDATE pemrograman SET
                                     nama = ?,
                                     nim = ?,
                                     nilai_tugas = ?,
                                     nilai_uts = ?,
                                     nilai_uas = ?,
                                     nilai_akhir = ?,
                                     mutu = ?,
                                     kelulusan = ?
                                  WHERE id = ?''',(mahasiswa,nim,nilai_tugas,nilai_uts,nilai_uas,nilai_akhir,mutu,kelulusan,id_terpilih))
                db.commit()
                messagebox.showinfo(message='Data sudah disimpan')
                self.mahasiswa.focus()

        root2 = Toplevel()
        test2 = ChildWindow(root2,self.id_terpilih)
        root2.title("Rubah Data pemrograman")
        root2.focus_set()
        root2.grab_set()
        root2.transient()
        root2.wait_window(root2)
        
        #tampilkan lagi data yang terupdate
        self.rows = self.ambilData()
        self.tampilListData()
        self.tampilDetailData(self.index_terpilih)
        self.listmahasiswa.select_set(self.index_terpilih)
        self.listmahasiswa.event_generate("<<ListboxSelect>>")  
        
    # SEARCH DATA 
    def cariData(self):
        class ChildWindow:
            def __init__(self,root2):
                self.lbkeyword = Label(root2,text="Masukkan keyword mahasiswa:")
                self.lbkeyword.grid(row=0,column=0,columnspan=2)

                self.lbmahasiswa = Label(root2,text="mahasiswa")
                self.lbmahasiswa.grid(row=1,column=0)
                self.mahasiswa_var = StringVar()
                self.mahasiswa = Entry(root2,textvariable=self.mahasiswa_var)       
                self.mahasiswa.grid(row=1,column=1)

                self.btSimpan = Button(root2, text="Cari",command=self.cariData)
                self.btSimpan.grid(row=5,column=1,sticky=E)
                self.btKembali = Button(root2, text="Kembali",command=root2.destroy)
                self.btKembali.grid(row=5,column=1,sticky=W)
                
            def cariData(self):
                db = sqlite3.connect("informatika.db")
                cursor = db.cursor()
                mahasiswa = self.mahasiswa_var.get()
                cursor.execute("SELECT * FROM pemrograman WHERE nama LIKE '%"+mahasiswa+"%'")
                self.rows = cursor.fetchall()
                if len(self.rows) == 0:
                    messagebox.showinfo(message='Pencarian tidak ditemukan. Silahkan coba lagi.')
                else:
                    self.btKembali.invoke()
                
        root2 = Toplevel()
        test2 = ChildWindow(root2)
        root2.title("Cari Data pemrograman")
        root2.focus_set()
        root2.grab_set()
        root2.transient()
        root2.wait_window(root2)
        try:
            if len(test2.rows)!= 0:    
                self.rows = test2.rows
        except AttributeError:
            self.index_terpilih = 0
            self.rows = self.ambilData()
        finally:
            self.tampilListData()
            self.listmahasiswa.select_set(0)
            self.listmahasiswa.event_generate("<<ListboxSelect>>") 

    # DELETE DATA         
    def hapusData(self):
        if messagebox.askokcancel(title="Hapus Data Mahasiswa",message="Data akan dihapus. Anda yakin?",icon="warning"):
            db = sqlite3.connect("informatika.db")
            cursor = db.cursor()
            cursor.execute("DELETE FROM pemrograman WHERE id=%d" % self.id_terpilih)
            db.commit()
            messagebox.showinfo(message='Data sudah dihapus')
            #tampilkan lagi data yang terupdate
            self.rows = self.ambilData()
            self.tampilListData()
            # aktifkan baris sebelum baris yg terhapus
            if self.index_terpilih != 0:
                self.index_terpilih = self.index_terpilih-1           
            self.listmahasiswa.select_set(self.index_terpilih)
            self.listmahasiswa.event_generate("<<ListboxSelect>>") 
        
# MAIN PROGRAM 
root = Tk()
myapp = KelasPemrograman(root)
root.configure(bg="#01bbff")
root.title("Rekap Nilai Kelas Pemrograman")
root.mainloop()
