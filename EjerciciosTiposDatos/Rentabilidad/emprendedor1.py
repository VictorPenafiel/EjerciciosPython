"""
Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto.Para ello utiliza input() para solicitar
como dato el precio de suscripción P, el número de usuarios U y el gasto total GT.
"""
# Solicitar datos al usuario
P = float(input("Introduzca el precio de suscripción: "))
U = float(input("Introduzca el número de usuarios: "))
GT = float(input("Introduzca los gastos totales: "))

# Calcular utilidades
Utilidades = P * U - GT

# Mostrar resultado
print(f"Las utilidades esperadas son: {Utilidades}")


