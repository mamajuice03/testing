#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import math

window = Tk()
window.title("Kalkulator GUI Dengan Python")
window.geometry('400x200')

lbl = Label(window, text="Masukkan Nilai Pertama : ",anchor="e",width=20)
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Masukkan Nilai Kedua : ",anchor="e",width=20)
lbl2.grid(column=0, row=1)

lbl3 = Label(window, text="Hasil : ",anchor="e",width=20)
lbl3.grid(column=0, row=2)

nilai1 = Entry(window,width=20)
nilai1.grid(column=1,row=0)

nilai2 = Entry(window,width=20)
nilai2.grid(column=1,row=1)

hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=2)

def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))

def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))
    
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
    
def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))
    
def xpangkaty():
    hasil.configure(text=(int(nilai1.get())**int(nilai2.get())))
    
def ypangkatx():
    hasil.configure(text=(int(nilai2.get())**int(nilai1.get())))

def modulus():
    hasil.configure(text=(int(nilai1.get())%int(nilai2.get())))

def xakary():
    hasil.configure(text=(math.sqrt(int(nilai1.get()))))

def yakarx():
    hasil.configure(text=(int(nilai2.get())**(1/int(nilai1.get()))))
    
btn = Button(window, text="Tambah", command=tambah)
btn.grid(column=0, row=3)

btn = Button(window, text="Kurang", command=kurang)
btn.grid(column=1, row=3)

btn = Button(window, text="Kali", command=kali)
btn.grid(column=0, row=4)

btn = Button(window, text="Bagi", command=bagi)
btn.grid(column=1, row=4)

btn = Button(window, text="X pangkat Y", command=xpangkaty)
btn.grid(column=0, row=5)

btn = Button(window, text="Y pangkat X", command=ypangkatx)
btn.grid(column=1, row=5)

btn = Button(window, text="Modulus", command=modulus)
btn.grid(column=0, row=6)

btn = Button(window, text="X Akar Y", command=xakary)
btn.grid(column=0, row=7)

btn = Button(window, text="Y Akar X", command=yakarx)
btn.grid(column=1, row=7)

window.mainloop()


# In[ ]:




