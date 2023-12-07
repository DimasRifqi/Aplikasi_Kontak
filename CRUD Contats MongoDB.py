import pymongo
import os

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["db_contacts"]
collection = database["contacts"]  

def tambah_kontak(nama, telepon, email):
    kontak = {"nama": nama, "telepon": telepon, "email": email}
    collection.insert_one(kontak)
    print("Kontak berhasil ditambahkan!")

def lihat_kontak():
    kontak_list = list(collection.find())
    for kontak in kontak_list:
        print(f"======================================")
        print(f"Nama    : {kontak['nama']}")
        print(f"Telepon : {kontak['telepon']}")
        print(f"Email   : {kontak['email']}")
        print(f"======================================")

def update_kontak():
    print(f"======================================")
    nama = input("Masukkan nama kontak yang ingin diperbarui : ")
    telepon_baru = input("Masukkan nomor telepon baru : ")
    email_baru = input("Masukkan email baru : ")
    print(f"======================================")
    
    result = collection.update_one({"nama": nama}, {"$set": {"telepon": telepon_baru, "email": email_baru}})
    
    if result.modified_count > 0:
        print("Kontak berhasil diperbarui!")
    else:
        print("Kontak tidak ditemukan.")

def hapus_kontak():
    print(f"======================================")
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    result = collection.delete_one({"nama": nama})
    print(f"======================================")
    
    if result.deleted_count > 0:
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")

# Fungsi switch-case
def switch_case(pilihan):
    switch_dict = {
        1: tambah_kontak,
        2: lihat_kontak,
        3: update_kontak,
        4: hapus_kontak,
        5: exit_program,
    }
    return switch_dict.get(pilihan, lambda: print("Pilihan tidak valid!"))

def exit_program():
    print("Program berhenti. Sampai jumpa!")
    exit()

while True:
    
    print("1. Tambah Kontak")
    print("2. Daftar Kontak")
    print("3. Update Kontak")
    print("4. Hapus Kontak")
    print("5. Exit")
    
    pilihan = input("Masukkan pilihan : ")
    os.system('cls')

    try:
        pilihan = int(pilihan)
    except ValueError:
        print("Masukkan angka '5' untuk keluar.")
        continue
    selected_function = switch_case(pilihan)
    
   
    if selected_function == tambah_kontak:
        nama = input("Masukkan nama kontak : ")
        telepon = input("Masukkan nomor telepon : ")
        email = input("Masukkan email : ")
        selected_function(nama, telepon, email)
    else:
      
        selected_function()
