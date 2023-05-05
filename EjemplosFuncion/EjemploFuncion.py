""" Crear una función que acepte 3 números como parámetros, sume todos los valores, y 
adicionalmente reste el segundo y tercer parámetro al primero.
Al invocar la función, debemos pasarle los parámetros en forma de lista. Esta devolverá ambos 
resultados en una tupla. Los resultados se deben imprimir en pantalla.
 """
datos = [40, 20 , 10]

def calcular(a, b, c):
 suma = a + b + c
 resta = a - b - c
 # regresa una lista de valores
 return suma, resta

resultado = calcular(*datos)
print("El resultado de la suma es:", resultado[0])
print("El resultado de la resta es:", resultado[1])
