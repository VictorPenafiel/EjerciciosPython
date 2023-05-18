"""

Se solicita crear un script escape.py que permita calcular la velocidad de escape
ingresando como datos de entradas el radio r y la constante g. Los datos de entrada
deben ingresarse de manera interactiva utilizando la función input().

El programa debe especificar claramente el formato en el que se deben entregar los
datos de entrada con instrucciones apropiadas.


"""
# Solicitar datos al usuario
r = float(input("Ingrese el radio en kilómetros: "))
g = float(input("Ingrese la constante gravitacional: "))

# Convertir radio a metros
r_metros = r * 1000

# Calcular velocidad de escape
Ve = (2 * g * r_metros) ** 0.5

# Mostrar resultado
print(f"La velocidad de escape es: {Ve} m/s")