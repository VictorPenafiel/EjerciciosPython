mi_lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
claves = ["A", "B", "C", "D"]

def imprimir_valores(lista):
    for i, valor in enumerate(lista):
        if valor == 0 and i == 0:
            return
        elif valor != 0:
            print('El valor es:', valor)

mi_diccionario = {clave: numeros for clave, numeros in zip(claves, mi_lista)}

for numeros in mi_diccionario.values():
    imprimir_valores(numeros)

print(mi_diccionario)
