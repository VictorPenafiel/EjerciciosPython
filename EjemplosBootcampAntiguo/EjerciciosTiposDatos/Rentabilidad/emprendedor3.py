"""
Considera ahora una tercera versión llamada emprendedor3.py utilizando la fórmula
original de utilidades donde el usuario ingrese el precio de suscripción P, el número
de usuarios normales U y los gastos GT. Adicionalmente, solicita las utilidades del
año anterior Uanterior, todo esto mediante input(). El programa debe calcular las
utilidades actuales y mostrar la razón entre las utilidades actuales y las del año
anterior con dos decimales

"""

# Solicitar datos al usuario
P = float(input("Introduzca el precio de suscripción: "))
U = float(input("Introduzca el número de usuarios: "))
GT = float(input("Introduzca los gastos totales: "))
Ua = float(input("Introduzca las utilidades del año anterior: "))

# Calcular utilidades
Utilidades = P * U - GT

# Calcular razón entre utilidades actuales y del año anterior
razon = Utilidades / Ua

# Mostrar resultados
print(f"Las utilidades esperadas son: {Utilidades}")
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon:.2f}")