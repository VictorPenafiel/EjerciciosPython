"""  Tomando la lista que se entrega a continuación, se solicita realizar las siguientes acciones en el orden indicado:
1. Eliminar los elementos duplicados.
2. Ordenar la lista resultante en orden ascendente.
"""

mi_lista = [5, 20, 15, 20, 25, 50, 20, 5, 18, 15]

# Eliminamos los elementos repetidos creando un set
mi_set = set(mi_lista)
mi_lista = list(mi_set)


# Ordenar la lista resultante en orden ascendente.
""" for i in range(len(mi_lista)):
    for j in range(i + 1, len(mi_lista)):
        if mi_lista[i] > mi_lista[j]:
            mi_lista[i], mi_lista[j] = mi_lista[j], mi_lista[i] """

print(mi_set)
