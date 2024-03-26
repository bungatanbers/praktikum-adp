angka_minimal = 1
angka_maksimal = 80

while angka_minimal <= angka_maksimal :
    for i in range(8):
        if angka_minimal <= angka_maksimal:
            if angka_minimal % 4 == 0:
                print("{:3}".format("DOR"), end=" ")
            else:
                print("{:3}".format(angka_minimal), end=" ")
        angka_minimal += 1
    print()