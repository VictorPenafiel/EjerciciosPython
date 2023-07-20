numeros = [45, 23, 67, 89, 12, 56, 78, 90]
maximo = numeros[0]

for numero in numeros:
    if numero > maximo:
        maximo = numero

print("El número más grande es:", maximo)
