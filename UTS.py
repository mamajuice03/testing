#!/usr/bin/env python
# coding: utf-8

# In[10]:


import sqlite3

conn = sqlite3.connect('test.db')

print("Opened database successfully")


# In[3]:


import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

#preparing a cursor
cursorObject = dataBase.cursor()

#createdb
cursorObject.execute("CREATE DATABASE db_sales_V3922048")


# In[4]:


import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='db_sales_V3922048'
)

# preparing cursor object
cursorObject = dataBase.cursor()

# creating table
studentRecord = """CREATE TABLE data_stok_barang (
                   id_barang VARCHAR(15) NOT NULL PRIMARY KEY,
                   nama_barang VARCHAR(70) NOT NULL,
                   harga_barang INT,
                   stok_awal INT,
                   barang_masuk INT,
                   barang_keluar INT,
                   stok_akhir INT
                   )"""

# table created
cursorObject.execute(studentRecord)

# disconnect from server
dataBase.close()


# In[ ]:


import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd = '',
    database = 'db_sales_V3922048'
)

def insert_data(id_barang, nama_barang, harga_barang, stok_awal, barang_masuk,
               barang_keluar, stok_akhir):
    cursorObject = dataBase.cursor()
    sql = "INSERT INTO data_stok_barang (id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir)
    cursorObject.execute(sql, val)
    dataBase.commit()
    print(cursorObject.rowcount, "Data berhasil ditambahkan")

def show_data():
    cursorObject = dataBase.cursor()
    cursorObject.execute("SELECT * FROM data_stok_barang")
    myresult = cursorObject.fetchall()
    for x in myresult:
        print(x)

def update_data(id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir):
    cursorObject = dataBase.cursor()
    sql = "UPDATE data_stok_barang SET nama_barang=%s, harga_barang=%s, stok_awal=%s, barang_masuk=%s, barang_keluar=%s, stok_akhir=%s WHERE id_barang=%s"
    val = (nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir, id_barang)
    cursorObject.execute(sql, val)
    dataBase.commit()
    print(cursorObject.rowcount, "Data berhasil diupdate")
    
def delete_data(id_barang):
    cursorObject = dataBase.cursor()
    sql = "DELETE FROM data_stok_barang WHERE id_barang = %s"
    val = (id_barang,)
    cursorObject.execute(sql, val)
    dataBase.commit()
    print(cursorObject.rowcount, "Data berhasil dihapus")

def search_data(keyword):
    cursorObject = dataBase.cursor()
    sql = "SELECT * FROM data_stok_barang WHERE nama_barang LIKE %s"
    val = ("%" + keyword + "%",)
    cursorObject.execute(sql, val)
    myresult = cursorObject.fetchall()
    for x in myresult:
        print(x)

        
print("=== Aplikasi Database Python ===")
print("1. Insert Data")
print("2. Tampilkan Data")
print("3. Update Data")
print("4. Hapus Data")
print("5. Cari Data")
print("0. Keluar")
print("-------------------------")

menu = input("Pilih Menu: ")

while menu != "0":
    if menu == "1":
        id_barang = input("Masukkan ID Barang: ")
        nama_barang = input("Masukkan Nama Barang: ")
        harga_barang = int(input("Masukkan Harga Barang: "))
        stok_awal = int(input("Masukkan Stok Awal Barang: "))
        barang_masuk = int(input("Masukkan Barang Masuk: "))
        barang_keluar = int(input("Masukkan Barang Keluar: "))
        stok_akhir = stok_awal + barang_masuk - barang_keluar

        insert_data(id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir)

    elif menu == "2":
        show_data()

    elif menu == "3":
        id_barang = input("Masukkan ID Barang yang akan diupdate: ")
        nama_barang = input("Masukkan Nama Barang Baru: ")
        harga_barang = int(input("Masukkan Harga Barang Baru: "))
        stok_awal = int(input("Masukkan Stok Awal Barang Baru: "))
        barang_masuk = int(input("Masukkan Barang Masuk Baru: "))
        barang_keluar = int(input("Masukkan Barang Keluar Baru: "))
        stok_akhir = stok_awal + barang_masuk - barang_keluar

        update_data(id_barang, nama_barang, harga_barang, stok_awal, barang_masuk, barang_keluar, stok_akhir)

    elif menu == "4":
        id_barang = input("Masukkan ID Barang yang akan dihapus: ")
        delete_data(id_barang)

    elif menu == "5":
        keyword = input("Masukkan Kata Kunci: ")
        search_data(keyword)

    else:
        print("Menu tidak tersedia")

    print("-------------------------")
    menu = input("Pilih Menu: ")

print("Program selesai") 


# In[ ]:




