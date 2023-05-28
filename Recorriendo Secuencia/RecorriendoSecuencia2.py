mi_lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
mi_diccionario = {}
claves = ["A", "B", "C", "D"]
contador = 0

for numeros in mi_lista:
    # usaremos un contador para saber en qué posición de la lista estamos
    j = 0
    # agregamos los datos al diccionario
    mi_diccionario[claves[contador]] = numeros

    for valor in numeros:
        if valor == 0 and j == 0:
            # omitimos la impresion de la lista
            break
        elif valor == 0 and j != 0:
            # omitimos la impresion solo de este cero
            continue
        else:
            print('El valor es:', valor)

        # debemos actualizar el valor del contador
        j += 1

    # actualizamos el contador
    contador += 1

print(mi_diccionario)