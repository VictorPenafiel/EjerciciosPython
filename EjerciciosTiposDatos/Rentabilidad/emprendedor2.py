
"""
Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién expuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada precios
de suscripción P, así como el número de usuarios Unormal y Upremium y el gasto total GT

"""
P = float(input("Introduzca el Precio de Suscripción: "))
Unormal = float(input("Introduzca el Número de Usuarios Normales: "))
Upremium = float(input("Introduzca el Número de Usuarios Premium: "))
GT = float(input("Introduzca los Gastos Totales: "))


Utilidades = P * Unormal + P *Upremium * 1.5 - GT

print("Las Utilidades esperadas son: ",Utilidades)