mi_lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
resultados = []
for numeros in mi_lista:
    sublista = []
    j = 0
    for valor in numeros:
        if valor == 0 and j == 0:
            break
        elif valor == 0 and j != 0:
            continue
        else:
            sublista.append(valor)
        j  = 1
    if sublista:
        resultados.append(sublista)
print(resultados)
