lista = [3, 5, 2, 8, 1, 10]
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        print("El primer número par en la lista es:", lista[i])
        break
    i += 1