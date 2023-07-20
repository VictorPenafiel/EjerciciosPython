a = int(input("ingresa un numero"))

if a > 1:
    es_primo = True
    for x in range(2, a):
        if (a % x) == 0:
            es_primo = False
            break
    if es_primo:
        print("Primo")
    else:
        print("no es primo")
else:
    print("no es primo")