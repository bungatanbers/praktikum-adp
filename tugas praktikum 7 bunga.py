def input_data():
    while True:
        n = int(input("Masukkan jumlah data: "))
        if n < 2:
            print("!!TIDAK VALID!! Jumlah data harus lebih dari atau sama dengan 2. Silakan input kembali.")
        else:
            break
    data = []
    for i in range(1, n + 1):
        nilai = int(input(f"Masukkan data ke-{i}: "))
        data.append(nilai)
    return data

def hitung_mean(data):
    if not data:
        return None
    total = sum(data)
    mean = total / len(data)
    return mean

def hitung_modus(data_input):
    if not data_input:
        return None
    max_nilai = max(data_input)
    freq = [0] * (int(max_nilai) + 1)
    for nilai in data_input:
        freq[int(nilai)] += 1
    max_freq = max(freq)
    if max_freq == 1:
        return None
    modus = []
    for nilai in range(len(freq)):
        if freq[nilai] == max_freq:
            modus.append(nilai)
    return modus

def hitung_varian(data):
    if not data:
        return None
    mean = hitung_mean(data)
    varian_1 = sum((i - mean) ** 2 for i in data)
    varian = varian_1 / len(data)
    return varian

def hasil(mean, modus, varian):
    lebar_kolom = 15
    print()
    print(f"| {'mean':<{lebar_kolom}} | {mean:<{lebar_kolom}.2f} |")
    if modus is None:
        modus_str = "Tidak ada modus"
    else:
        modus_str = str(modus)
    print(f"| {'modus':<{lebar_kolom}} | {modus_str:<{lebar_kolom}} |")
    print(f"| {'varian':<{lebar_kolom}} | {varian:<{lebar_kolom}.2f} |")

data = input_data()
mean = hitung_mean(data) 
modus = hitung_modus(data)
varian = hitung_varian(data)
hasil(mean, modus, varian)
