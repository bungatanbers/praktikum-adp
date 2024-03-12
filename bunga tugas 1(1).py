p = float(input('masukkan panjang balok: '))
l = float(input('masukkan lebar balok: '))
t =float(input('masukkan tinggi balok: '))
s = float(input('masukkan sisi kubus: '))

volume_balok = p*l*t
luas_permukaan_balok = 2*(p*l+p*t+l*t)

volume_kubus = s**3
luas_permukaan_kubus = 6*s**2

print('volume balok adalah: ', volume_balok)
print('luas permukaan balok adalah: ', luas_permukaan_balok)

print('volume kubus adalah: ', volume_kubus)
print('luas permukaan kubus adalah: ', luas_permukaan_kubus)