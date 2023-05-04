def calcular(a, b, c):
 suma = a + b + c
 resta = a - b - c
 # regresa una lista de valores
 return suma, resta
datos = [40, 20 , 10]
resultado = calcular(*datos)
print("El resultado de la suma es:", resultado[0])
print("El resultado de la resta es:", resultado[1])
