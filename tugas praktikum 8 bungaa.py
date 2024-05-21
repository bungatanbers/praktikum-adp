def tambah_film(judul, nama_penulis_skenario, nama_sutradara, tahun_rilis):
    with open("film_bunga.txt", "a") as file:
        file.write(f"{judul},{nama_penulis_skenario},{nama_sutradara},{tahun_rilis}\n")
    print("Data film berhasil ditambahkan.")

def hapus_film(judul):
    with open("film_bunga.txt", "r") as file:
        lines = file.readlines()
    with open("film_bunga.txt", "w") as file:
        for line in lines:
            data = line.strip().split(',')
            if data[0] != judul:
                file.write(line)
    print("Data film berhasil dihapus.")

def tampilkan_data_film():
    with open("film_bunga.txt", "r") as file:
        data_film = file.readlines()

    if data_film:
        print("================================================================================")
        print("| {:<20} | {:<20} | {:<15} | {:<10} |".format("Judul Film", "Nama Penulis Skenario", "Nama sutradara", "Tahun Rilis"))
        print("================================================================================")
        for data in data_film:
            judul, nama_penulis_skenario, nama_sutradara, tahun_rilis = data.strip().split(',')
            print("| {:<20} | {:<21} | {:<15} | {:<11} |".format(judul, nama_penulis_skenario, nama_sutradara, tahun_rilis))
        print("================================================================================")
    else:
        print("Database film kosong.")

while True:
    print("-----------------------------------")
    print("|    KUMPULAN DATA FILM BUNGA     |")
    print("-----------------------------------")
    print("| Menu:                           |")
    print("| 1. Tambah Data Film             |")
    print("| 2. Hapus Data Film              |")
    print("| 3. Tampilkan Semua Data Film    |")
    print("-----------------------------------\n")
    pilihan = int(input("Pilih menu (1/2/3): "))

    if pilihan == 1 :
        judul = str(input("Masukkan judul film: "))
        nama_penulis_skenario = str(input("Masukkan nama penulis skenario film: "))
        nama_sutradara = str(input("Masukkan nama sutradara film: "))
        tahun_rilis = int(input("Masukkan tahun rilis film: "))
        tambah_film(judul, nama_penulis_skenario, nama_sutradara, tahun_rilis)
    elif pilihan == 2 :
        judul = input("Masukkan judul film yang akan dihapus: ")
        hapus_film(judul)
    elif pilihan == 3 :
        tampilkan_data_film()
    else:
        print("!!!ERROR!!!Pilihan tidak valid. Silakan pilih menu yang tersedia.")
