mi_lista = [10, 3, 21, 44, 12, 19, 28, 0, 5, 50]
for valor in mi_lista:
    if(valor == 0):
        print("El número es cero")
    elif(valor % 2 == 0):
        print(f'El número es {valor} y es par')
    else:
        print(f'El número es {valor} y es impar')