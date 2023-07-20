lista = [3, 5, 2, 8, 1, 10]
numero_par = None  # inicializa la variable que contendrá el número par
for numero in lista:
    if numero % 2 == 0:
        numero_par = numero
        break  # termina el bucle en la primera aparición de un número par
if numero_par is not None:  # si se encontró un número par
    indice_numero_par = lista.index(numero_par)
    print(f"El primer número par en la lista es {numero_par} y su índice es {indice_numero_par}")