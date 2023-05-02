a = int(input("Introduzca los términos: "))

f = 0  # primer elemento de la serie
s = 1  # segundo elemento de la serie

if a <= 0:
    print("Las series requeridas son", f)
else:
    print(f, s, end=" ")
    for x in range(2, a):
        next_term = f + s
        print(next_term, end=" ")
        f = s
        s = next_term
