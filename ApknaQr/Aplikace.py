from tkinter import *
from tkinter import messagebox
import pyqrcode

tk=Tk()
tk.title("QRgenerátor")
tk.config(bg="#00203f")

def generovat_QR():
    if len(vstup_uzivatele.get()) !=0 :
        global qr,img
        qr=pyqrcode.create(vstup_uzivatele.get())
        img=BitmapImage(data=qr.xbm(scale=10))
    else:
        messagebox.showwarning('Varování', "Pole je vyžadované!")
    try:
        displ_kod()
    except:
        pass

def displ_kod():
    img_lbl.config(image=img)
    output.config(text="Qr kód: "+vstup_uzivatele.get())

lbl=Label(tk,text="Vložte Text nebo Url", bg="#adefd1", padx=30, pady=20, font=("Courier", 30))
lbl.pack()

vstup_uzivatele=StringVar()
entry=Entry(tk, textvariable=vstup_uzivatele, width=50, font=("ariel", 15))
entry.pack(padx=50, pady=30)

tlacidlo= Button(tk, text="Generovat QR", width=20, command=generovat_QR, font=("ariel", 15))
tlacidlo.pack(padx=10,pady=10)

img_lbl=Label(tk, bg="#e6e6e6")
img_lbl.pack()

vystup=Label(tk, text="", bg="#adefd1")
vystup.pack()

tk.mainloop()
#jjj
#jjj
#jjjha