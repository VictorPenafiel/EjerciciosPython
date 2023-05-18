from pizza import Pizza

print(f"Todas las pizzas tienen un tamaño {Pizza.tamano} y un valor de ${Pizza.precio}.")
print(Pizza.validar_elemento("salsa de tomate",["salsa de tomate", "salsa bbq"]))

pizza_1 = Pizza()
pizza_1.pedir()

print("Tu pedido es el siguiente: ")
print(f"proteina: {pizza_1.prot}")
print(f"Vegetales: {pizza_1.veg_1} y {pizza_1.veg_2}")
print(f"Tipo de masa: {pizza_1.tipo_masa}")
print(F"La pizza solicitada es {'valida' if pizza_1.pedido_valido else 'No valida'}")
