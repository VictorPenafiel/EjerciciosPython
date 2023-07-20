#Creación de la lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for item in numeros:
    if item == 0:
        print("El " + str(item) + " es cero")
    elif item % 2 == 0:
        print("El " + str(item) + " es par")
    else:
        print("El " + str(item) + " es impar")