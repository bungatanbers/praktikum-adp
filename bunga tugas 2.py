print("""
    --------------------------------------------
    List Harga Menu Paket Makanan
    A. Paket_A : Rp 25.000
    B. Paket_B : Rp 35.000
    C. Paket_C: Rp 45.000
    --------------------------------------------
    """)

pesan=str(input("Anda mau pesan paket apa? (dalam bentuk abjad) ")).lower()
jarak=int(input("Berapa jarak rumah anda dari restoran ini? (dalam meter) "))

if pesan == "a":
    harga = 25000  
    if jarak < 500:
        ongkir = 0  
        total_harga = harga + ongkir
    elif jarak <= 1500 and jarak >= 500:  
        ongkir = 10000 
        total_harga = harga + ongkir
    else :  
        ongkir = 20000  
        total_harga = harga + ongkir
if pesan == "b":
    harga = 30000  
    if jarak < 500:
        ongkir = 0  
        total_harga = harga + ongkir
    elif jarak <= 1500 and jarak >= 500:  
        ongkir = 10000 
        total_harga = harga + ongkir
    else :  
        ongkir = 20000  
        total_harga = harga + ongkir
if pesan == "c":
    harga = 45000  
    if jarak < 500:
        ongkir = 0  
        total_harga = harga + ongkir
    elif jarak <= 1500 and jarak >= 500:  
        ongkir = 10000 
        total_harga = harga + ongkir
    else :  
        ongkir = 20000  
        total_harga = harga + ongkir
        
print("Jadi total yang harus anda bayar adalah ", total_harga)