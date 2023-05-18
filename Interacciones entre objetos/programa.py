"""

En un archivo programa.py, implementa la lógica necesaria para crear una tienda e
ingresar sus productos. Se debe solicitar ingresar productos hasta que el usuario
indique lo contrario. Luego, se le debe dar al usuario las opciones de listar los
productos existentes, realizar una venta, o salir del programa. Para las primeras dos
opciones, debe hacer llamados a los métodos de su instancia y luego volver a
consultar cuál de las tres acciones se desea realizar. Si se escoge la tercera opción,
se finaliza la ejecución del programa

"""

#Se importan las clases necesarias

from tienda import TiendaRestaurante, TiendaSupermercado, TiendaFarmacia
from producto import Producto

# Se solicitay almacena el tipo de tienda a ingresar, nombre, y costo de delivery

tipo = int(input("Ingrese tipo de la tienda a agregar:\n"
"1. Restaurante\n2. Supermercado\n3. Farmacia\n"))

nombre = input("\nIngrese nombre de la tienda a agregar:\n")

precio_delivery = int(input("\nIngrese precio del deliveyr:\n"))

# Crear instancia de tienda correspondiente.
if tipo == 2:
	tienda = TiendaSupermercado(nombre, precio_delivery)
elif tipo == 3:
	tienda = TiendaFarmacia(nombre, precio_delivery)
else:
	tienda = TiendaRestaurante(nombre, precio_delivery)


""" Hacer ciclo para ingresar un producto a la tienda, y dentro del, consultar nombre, precio y stock del producto."""

opcion = 1

while opcion == 1:
	nombre_producto = input("\nIngrese nombre del producto a ingresar:\n")
	precio = int(input("\nIngrese precio del producto:\n"))
	stock = int(input("\nIngrese stock del producto:\n"))

# aquí ingreso el producto en la tienda (ojo: seguimos dentro del ciclo), y pregunto si se desea añadir otro producto

	tienda.ingresar_producto(nombre_producto, precio, stock)

	opcion = int(input("\n¿Desea agregar otro producto?\n"
	"1. Sí\n2. No\n"))

# Fuera del ciclo anterior, consultar si se desea listar los productos de la tienda, realizar
# una venta, o salir del programa.

opcion_productos = int(input(
"\nIndique qué desea realizar:\n"
"1. Listar productos de la tienda\n"
"2. Realizar una venta de producto\n"
"3. Salir\n"))

# ahora nuevo ciclo para procesar si se escogió 1 o 2

while opcion_productos in (1, 2):
	
	if opcion_productos == 1:
		print(tienda.listar_productos())
	elif opcion_productos == 2:
		nombre_producto = input("\nIngrese nombre del producto a vender:\n")
		cantidad = int(input("\nIngrese cantidad que desea comprar:\n"))
		tienda.realizar_venta(nombre_producto, cantidad)
	
	opcion_productos = int(input(
		"\nIndique qué desea realizar:\n"
		"1. Listar productos de la tienda\n"
		"2. Realizar una venta de producto\n"
		"3. Salir\n"))