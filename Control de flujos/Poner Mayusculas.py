mascotas = [
'gato',
'perro',
'tortuga',
'gato',
'perro',
'tortuga',
'gato',
'perro',
'tortuga',
'gato',
'perro',
'tortuga',
'hurón',
'hamster',
'erizo de tierra',
]
mascotas_mayusculas = []
for mascota in mascotas:
    mascotas_mayusculas.append(mascota.upper())
print(mascotas_mayusculas)

mascotas_mayusculas = [mascota.upper() for mascota in mascotas] # List Comprehensions
print(mascotas_mayusculas)


valores = [0,4,5,6,7,8,9]
lista_square = []
for valor in valores:
    lista_square.append(valor**2)
print(lista_square)

lista_square = [valor**2 for valor in valores]  # List Comprehensions
print(lista_square)

#¿Qué pasa si para la lista de mascotas definida anteriormente se quiere transformar enmayúscula sólo a los gatos? La solución con for sería la siguiente:
    
mascotas_mayusculas = []
for i in mascotas:
    if i == 'gato':
        mascotas_mayusculas.append(i.upper())
    else:
        mascotas_mayusculas.append(i.lower())
print(mascotas_mayusculas)

mascotas_mayusculas = [mascota.upper() if mascota == 'gato' else mascota for mascota in mascotas] # List Comprehensions
print(mascotas_mayusculas)

#A continuación, se muestra cómo crear un programa que filtre todos los números de una  lista que sean menores a 1000. Esto es lo mismo que decir "seleccionar todos los elementos mayor o iguales a mil".

a = [100, 200, 1000, 5000, 10000, 10, 5000]
n = len(a)
filtered_array = []
for i in range(n):
    if a[i] >= 1000:
        filtered_array.append(a[i])
print(filtered_array)

print([valor for valor in a if valor >= 1000])
