import time
from termcolor import cprint
import os

os.system('cls')
# Fungsi untuk pemesanan cream puff
def pesan():
    while True:
        cprint("-----------------------------------------------------------------------------------------------------------", "white", "on_light_yellow")
        cprint("|                              Halo!! Selamat Datang Cream Puff Lovers CPG                                |", "red", "on_white")
        cprint("-----------------------------------------------------------------------------------------------------------", "white", "on_light_yellow")
        cprint("| Menu Cream Puff Gryscl:                                                                                 |", "white", "on_dark_grey")
        cprint("| A. Vanilla ......................................................................................... 5k |", "black", "on_white")
        cprint("| B. Cokelat ......................................................................................... 7k |", "black", "on_white")
        cprint("| C. Greentea ........................................................................................ 8k |", "black", "on_white")
        cprint("-----------------------------------------------------------------------------------------------------------", "white", "on_light_yellow")
        cprint("| Spesial untuk Cream Puff Lovers CPG:                                                                    |", "white", "on_dark_grey")
        cprint("| 1. Diskon sebesar 5% jika pembelian lebih dari 10 pcs                                                   |", "black", "on_white")
        cprint("| 2. Diskon tambahan sebesar 10% jika minimal total belanja Cream Puff Lovers Rp 200.000                  |", "black", "on_white")
        cprint("-----------------------------------------------------------------------------------------------------------", "white", "on_light_yellow")
        while True:
            pesan = input("Halo cream puff lovers, Anda mau pesan varian apa (A/B/C)? ").lower()
            if pesan not in ['a', 'b', 'c']:
                cprint("Maaf varian yang Anda inginkan tidak tersedia. Silakan pilih kembali!", "white", "on_red")
                continue
            else:
                break
        while True:
            jumlah = int(input("Berapa pcs cream puff yang ingin Anda beli? "))
            if jumlah <= 0:
                cprint("Jumlah harus lebih besar dari 0. Silakan masukkan kembali!", "white", "on_red")
                continue
            else:
                break
        if pesan == "a":
            varian = "Vanilla"
            harga = 5000
        elif pesan == "b":
            varian = "Cokelat"
            harga = 7000
        else:
            varian = "Greentea"
            harga = 8000

        total = jumlah * harga
        if jumlah > 10:
            diskon = total * 0.05
        else:
            diskon = 0
        total_harga = total - diskon
        tambah(varian, jumlah, harga, total, diskon, total_harga)
        while True:
            lagi = input("Apakah Anda ingin memesan lagi? (y/n): ").lower()
            if lagi == "y":
                break
            elif lagi == "n":
                return
            else:
                cprint("Pilihan Anda tidak valid. Silakan masukkan Y untuk memesan kembali atau N untuk keluar", "white", "on_red")
# Fungsi untuk menambahkan pesanan ke file
def tambah(nama, jumlah, harga, total, diskon, total_harga):
    with open("data_keranjang.txt", "a") as file:
        file.write(f"{nama},{jumlah},{harga},{total},{diskon},{total_harga}\n")
    cprint("Cream Puff telah berhasil ditambahkan ke dalam keranjang.", "white","on_blue")
# Fungsi untuk menghapus pesanan berdasarkan nomor 
def hapus(nomor):
    with open("data_keranjang.txt", "r") as file:
        lines = file.readlines()
    if 0 < nomor <= len(lines):
        with open("data_keranjang.txt", "w") as file:
            for idx, line in enumerate(lines, 1):
                if idx != nomor:
                    file.write(line)
        for i in range(0, 101, 50):
            print(f"loading {i} %", end="\r")
            time.sleep(1)
        cprint("Cream Puff berhasil dihapus dari keranjang.", "white", "on_blue")
    else:
        cprint("Nomor item tidak sesuai.", "white", "on_red")
# Fungsi untuk menampilkan semua pesanan dari file
def tampilkan():
    with open("data_keranjang.txt", "r") as file:
        data_item = file.readlines()
    if data_item:
        cprint("===========================================================================================================","black","on_white")
        cprint("| {:^5} | {:^20} | {:^10} | {:^10} | {:^15} | {:^10} | {:^15} |".format("No.", "Nama Varian", "Banyak", "Harga/pcs", "Total", "Diskon", "Total Harga"),"black","on_white")
        cprint("===========================================================================================================","black","on_white")
        for idx, data in enumerate(data_item, 1):
            data = data.strip().split(',')
            if len(data) == 6:
                nama, banyak, harga, total, diskon, total_belanja = data
                cprint("| {:<5} | {:<20} | {:^10} | {:^10} | {:>15} | {:>10} | {:>15} |".format(idx, nama, banyak, harga, total, diskon, total_belanja),"black","on_white")
            else:
                print("Format data tidak valid:", data)
        cprint("===========================================================================================================","black","on_white")
    else:
        cprint("Keranjang belanja Cream Puff anda kosong.", "white", "on_red")
# Fungsi untuk mengosongkan keranjang
def kosong():
    open("data_keranjang.txt", "w").close()
    cprint("Terima kasih telah menggunakan program kasir ini, Sampai jumpa!", "white","on_blue")
# Fungsi untuk cetak struk dan keluar dari program
def cetak_dan_selesai():
    with open("data_keranjang.txt", "r") as file:
        data_item = file.readlines()
    if data_item:
        total_semua = 0
        tambahan_diskon = 0
        total_akhir = 0
        for idx, data in enumerate(data_item, 1):
            data = data.strip().split(',')
            if len(data) == 6:
                nama, banyak, harga, total, diskon, total_harga = data
                total_semua += float(total_harga)
        if total_semua >= 200000:
            tambahan_diskon = total_semua * 0.10 
        else :
            tambahan_diskon = 0
        total_akhir = total_semua - tambahan_diskon
        while True:
            lembar_uang = int(input("Masukkan jumlah lembar uang pecahan 50.000 yang akan dibayarkan: "))
            uang_dibayar = lembar_uang * 50000
            if uang_dibayar >= total_akhir:
                kembalian = uang_dibayar - total_akhir
                break
            else:
                cprint("Uang yang dibayarkan tidak cukup. Silakan masukkan kembali.","white","on_red")   
        for i in range(0, 101, 50):
            print(f"loading {i} %", end="\r")
            time.sleep(1)
        time.sleep(1)
        cprint("Struk Belanja berhasil dicetak.","white","on_green")
        time.sleep(1)
        cprint("===========================================================================================================","red","on_white")
        cprint("|                                            CREAM PUFF GRYSCL                                            |","magenta","on_white")
        cprint("|                                            Jalan Hamka no.14                                            |","red","on_white")
        cprint("|                                               Bukittinggi                                               |","red","on_white")
        cprint("===========================================================================================================","red","on_white")
        cprint("| {:^5} | {:^20} | {:^10} | {:^10} | {:^15} | {:^10} | {:^15} |".format("No.", "Nama Varian", "Banyak", "Harga/pcs", "Total", "Diskon", "Total Harga"),"black","on_white")
        cprint("===========================================================================================================","red","on_white")
        for idx, data in enumerate(data_item, 1):
            data = data.strip().split(',')
            if len(data) == 6:
                nama, banyak, harga, total, diskon, total_harga = data
                cprint("| {:<5} | {:<20} | {:^10} | {:^10} | {:>15} | {:>10} | {:>15} |".format(idx, nama, banyak, harga, total, diskon, total_harga),"black","on_white")
            else:
                print("Format data tidak valid:", data)
        cprint("-----------------------------------------------------------------------------------------------------------","red","on_white")
        cprint("| {:<87} {:>15} |".format("Total Belanja", total_semua),"black","on_white")
        cprint("| {:<87} {:>15} |".format("Tambahan Diskon", tambahan_diskon),"black","on_white")
        cprint("-----------------------------------------------------------------------------------------------------------","red","on_white")
        cprint("| {:<87} {:>15} |".format("Total Akhir", total_akhir),"black","on_white")
        cprint("===========================================================================================================","red","on_white")
        cprint("| {:<87} {:>15} |".format("Cash", uang_dibayar),"black","on_white")
        cprint("| {:<87} {:>15} |".format("Change", kembalian),"black","on_white")
        cprint("===========================================================================================================","red","on_white")
        cprint("|                               Terima kasih telah berbelanja di toko kami                                |","light_magenta","on_white")
        cprint("|                                      Semoga hari Anda menyenangkan                                      |","light_magenta","on_white")
        cprint("|                                 Sampai jumpa di kunjungan berikutnya :D                                 |","light_magenta","on_white")
        cprint("===========================================================================================================","red","on_white")        
        time.sleep(1)
        cprint("Keranjang Cream Puff berhasil dikosongkan!","black","on_yellow")
        kosong()  
    else:
        cprint("Keranjang belanja Cream Puff anda kosong.","white","on_red")
# Program Utama
while True:
    print("")
    cprint("-----------------------------------------------------------------------------------------------------------", "white", "on_light_magenta")
    cprint("|                                    SELF-CHECK OUT CREAM PUFF GRYSCL                                     |", "magenta", "on_light_grey")
    cprint("-----------------------------------------------------------------------------------------------------------", "white", "on_light_magenta")
    cprint("| Menu:                                                                                                   |", "magenta", "on_light_grey")
    cprint("| 1. Pesan Cream Puff                                                                                     |", "black", "on_light_grey")
    cprint("| 2. Hapus Pesanan                                                                                        |", "black", "on_light_grey")
    cprint("| 3. Tampilkan Semua Pesanan                                                                              |", "black", "on_light_grey")
    cprint("| 4. Cetak Struk dan Selesai                                                                              |", "black", "on_light_grey")
    cprint("| 5. Keluar                                                                                               |", "black", "on_light_grey")
    cprint("-----------------------------------------------------------------------------------------------------------", "white", "on_light_magenta")
    pilihan = input("Pilih menu (1/2/3/4/5): ")
    if pilihan == "1":
        pesan()
    elif pilihan == "2":
        nomor = input("Masukkan nomor item yang akan dihapus: ")
        if nomor.isdigit():
            hapus(int(nomor))
        else:
            cprint("Masukkan nomor yang valid.","white","on_red")
    elif pilihan == "3":
        tampilkan()
    elif pilihan == "4":
        cetak_dan_selesai()
        break
    elif pilihan == "5":
        kosong()
        break
    else:
        cprint("!!!ERROR!!! Pilihan tidak valid. Silakan pilih menu yang tersedia!","white","on_red")
