libros_prestados = {'Cien años de soledad', 'El amor en los tiempos del cólera', 'La ciudad y los perros', 'La casa verde', 'El otoño del patriarca', 'Rayuela', 'Pedro Páramo', 'La tregua'}
libros_devueltos = {'Cien años de soledad', 'La ciudad y los perros', 'El otoño del patriarca'}

print(f"La cantidad total de libros prestados es: {len(libros_prestados)}")
print(f"Los libros que aún no han sido devueltos son: {libros_prestados - libros_devueltos}")