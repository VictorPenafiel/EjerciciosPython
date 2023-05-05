# Ciclo For

# Estructura 1:  Recorrer un objeto iterable

animales = ["Perro","Gato","Ratón","Hamster"]

for item in animales:
	print(item)
	
# Estructura 2: Iterar en un rango numérico

for i in range(10):
	print(i)
	
# Estructura 3: Iterar en un rango numérico con inicio y fin

for i in range(2,8):   # En este caso i parte en 2 y termina en 8-1
	print(i)

# Estructura 4: Iterar en un rango numérico con inicio, fin y tamaño del paso (step)

for i in range(2,8,2):   # En este caso i parte en 2 y termina en 8-1, y con paso de 2 en 2.
	print(i)