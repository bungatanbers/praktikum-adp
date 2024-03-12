panjang = float(input('masukkan panjang balok: '))
lebar = float(input('masukkan lebar balok: '))
tinggi =float(input('masukkan tinggi balok: '))
sisi_kubus = float(input('masukkan sisi kubus: '))

volume_balok = panjang*lebar*tinggi
luas_permukaan_balok = 2*(panjang*lebar+panjang*tinggi+lebar*tinggi)

volume_kubus = sisi_kubus**3
luas_permukaan_kubus = 6*sisi_kubus**2

print('volume balok adalah: ', volume_balok)
print('luas permukaan balok adalah: ', luas_permukaan_balok)

print('volume kubus adalah: ', volume_kubus)
print('luas permukaan kubus adalah: ', luas_permukaan_kubus)
