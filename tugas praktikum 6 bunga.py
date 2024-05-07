while True:
    ukuran = int(input("masukkan ukuran matriks (contoh, matriks 2x2 tulis 2): "))
    if ukuran > 0:
        break
    else:
        print("!!!TIDAK VALID!!! ukuran matriks harus lebih besar dari 0. Silakan input ukuran matriks kembali.\n")

print("Matriks A:")
matriks_a = []
for i in range(ukuran):
    baris = []
    for j in range(ukuran):
        isi = int(input(f"masukkan isi matriks A baris {i+1}, kolom {j+1}: "))
        baris.append(isi)
    matriks_a.append(baris)

print("\nMatriks B:")
matriks_b = []
for i in range(ukuran):
    baris = []
    for j in range(ukuran):
        isi = int(input(f"masukkan isi matriks B baris {i+1}, kolom {j+1}: "))
        baris.append(isi)
    matriks_b.append(baris)
    
#Perkalian Matriks A dan B
matriks_c = []
for i in range(ukuran):
    baris_c = []
    for j in range(ukuran):
        hasil = 0
        for k in range(ukuran):
            hasil += matriks_a[i][k]*matriks_b[k][j]
        baris_c.append(hasil)
    matriks_c.append(baris_c)

print("\nMatriks C (Matriks A X B) :")
for baris in matriks_c:
    print(baris)
    
#Transpose Matriks A dan B 
mtp_a = []
for i in range(ukuran):
    baris_atp = []
    for j in range(ukuran):
        baris_atp.append(matriks_a[j][i])
    mtp_a.append(baris_atp)

print("\nTranspose matriks A:")
for baris in mtp_a:
    print(baris)

mtp_b = []
for i in range(ukuran):
    baris_btp = []
    for j in range(ukuran):
        baris_btp.append(matriks_b[j][i])
    mtp_b.append(baris_btp)

print("\nTranspose matriks B:")
for baris in mtp_b:
    print(baris)
    
#Penjumlahan penjumlahan transpose matriks A dan transpose matriks B 
matriks_d = []
for i in range(ukuran):
    baris_d = []
    for j in range(ukuran):
        jumlah = mtp_a[i][j] + mtp_b[i][j]
        baris_d.append(jumlah)
    matriks_d.append(baris_d)

print("\nMatriks D (penjumlahan transpose matriks A dan transpose matriks B) :")
for baris in matriks_d:
    print(baris)