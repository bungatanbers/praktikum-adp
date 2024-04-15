nilai_x = list(range(-10, 11))

nilai_fx = []
for x in nilai_x:
    if x > 0:
        nilai_fx.append ((x**2) + (2*x))
    elif x < 0:
        nilai_fx.append (1/x)
    else:
        nilai_fx.append (10)

print("| {:<4} | {:<20} |".format("x", "f(x)"))
for i in range(len(nilai_x)):
    x = nilai_x[i]
    fx = nilai_fx[i]
    print("| {:<4} | {:<20} |".format(x,fx))