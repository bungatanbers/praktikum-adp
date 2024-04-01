lanjut = "y"
while lanjut == "y":
    print("""
    ----------------------------------------------------------------------
    Hai! Selamat Datang Cream Puff Lovers CPG
    ----------------------------------------------------------------------
    Menu Cream Puff Gryscl
    A. Vanilla  : Rp 5.000
    B. Cokelat  : Rp 7.000
    C. Greentea : Rp 8.000
    ----------------------------------------------------------------------
    Spesial untuk Cream Puff Lovers CPG:
    1. Diskon sebesar 20% jika pembelian varian Vanilla lebih dari 5 pcs
    2. Diskon sebesar 25% jika pembelian varian Cokelat lebih dari 5 pcs
    3. Diskon sebesar 30% jika pembelian varian Greentea lebih dari 5 pcs
    
    nb: Jika minimal total belanja Cream Puff Lovers CPG  Rp 200.000 maka
        mendapatkan diskon tambahan sebesar 5%
    ----------------------------------------------------------------------
    
    """)
    
    pesan = str(input("Halo cream puff lovers, Anda mau pesan varian apa (A/B/C)? ")).lower()

    while pesan not in ['a', 'b', 'c']:
        print("Maaf varian yang Anda inginkan tidak tersedia. Silakan pilih kembali.\n")
        pesan = str(input("Anda mau pesan varian apa (A/B/C)? ")).lower()
        
    jumlah = int(input("Berapa pcs cream puff yang ingin Anda beli? "))

    
    if pesan == "a":
        varian = "Vanilla"
        harga = 5000
        if jumlah <= 5:
            diskon = 0
            total_harga = (harga*jumlah) - diskon
        else:
            diskon = (harga*jumlah) * 0.2
            total_harga = (harga*jumlah) - diskon
    elif pesan == "b":
        varian = "Cokelat"
        harga = 7000
        if jumlah <= 5:
            diskon = 0
            total_harga = (harga*jumlah) - diskon
        else:
            diskon = (harga*jumlah) * 0.25
            total_harga = (harga*jumlah) - diskon
    elif pesan == "c":
        varian = "Greentea"
        harga = 8000
        if jumlah <= 5:
            diskon = 0
            total_harga = (harga*jumlah) - diskon
        else:
            diskon = (harga*jumlah) * 0.3
            total_harga = (harga*jumlah) - diskon
    
    if total_harga >= 200000:
        tambahan_diskon = total_harga * 0.05
        total_belanja = total_harga - tambahan_diskon  
    else:
        tambahan_diskon = 0
        total_belanja = total_harga - tambahan_diskon
    
    print("----------------------------------------------------------------------")
    print("Cream Puff rasa                            :", varian)
    print("Jumlah                                     :", jumlah)
    print("Harga/pcs                                  :", harga)
    print("----------------------------------------------------------------------")
    print("Total                                      :", harga*jumlah) 
    print("Diskon                                     :", diskon)
    print("---------------------------------------------------------------------- -")
    print("Total harga                                :", total_harga)
    print("Tambahan diskon                            :", tambahan_diskon)
    print("---------------------------------------------------------------------- +")
    print("Total belanja yang harus anda bayar adalah :", total_belanja)
    print("----------------------------------------------------------------------")


    while True:
        lanjut = input("Apakah Anda ingin memesan kembali? (Y/N): ").lower()
        if lanjut == 'n':
            print("Terima kasih sudah membeli cream puff di CPG!! Selamat menikmati cream puff lovers!!")
            print("------------------------------------------------------------------------------------")
            break
        elif lanjut == 'y':
            break
        else:
            print("Pilihan anda tidak sesuai. Silakan masukkan Y untuk memesan cream puff kembali atau N untuk batal pesan kembali")
