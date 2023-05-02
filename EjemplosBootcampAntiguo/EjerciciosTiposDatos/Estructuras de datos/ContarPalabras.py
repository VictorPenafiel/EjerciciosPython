from itertools import count
import sys

with open("texto.txt", "r") as file:
    texto = file.read()

# A traves de la estructura de datos set se cuentan el numero de caracteres distintos
letras_no_rep = set(texto)
cant_letras = len(letras_no_rep)


# Esto resuelve la separación del texto original por palabras
palabras = texto.split(" ")
palabras2 = set(palabras)
cant_palabras = len(palabras2)

print(f'El numero de caracteres distintos es:{cant_letras}')
print(f'El numero de palabras distintas es:{cant_palabras}')

print
