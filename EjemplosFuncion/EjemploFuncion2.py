""" Crear una función que sume dos números, otra que reste dos números, otra que multiplique dos 
números, y otra que divida dos números. Adicionalmente, crear una función que acepte dos 
números como parámetros y regrese el resultado en forma de tupla de su suma, resta, 
multiplicación y división.
Los resultados se deben almacenar en un diccionario, cuyas claves serán: Suma, Resta, 
Multiplicación y División, y los valores de cada clave serán los resultados obtenidos con la función 
creada anteriormente
 """

def sumar(a, b):
 suma = a + b
 return suma
 
def restar(a, b):
 resta = a - b
 return resta
 
def multiplicar(a,b):
 multiplicacion = a * b
 return multiplicacion
 
def dividir(a,b):
 division = a / b
 return division
 
def calcular(a,b) :
 return sumar(a,b), restar(a,b), multiplicar(a,b), dividir(a,b)
 
datos = [20, 10]
res = calcular(*datos)
mis_resultados = { "Suma" : res[0],
"Resta" : res[1],
"Multiplicacion" : res[2],
"Division" : res[3]
}
print(mis_resultados)
