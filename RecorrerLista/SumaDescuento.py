precios = [25.50, 12.30, 36.40, 9.75, 15.20]
descuento = 10

# Calcular el precio total sin descuento
precio_total = sum(precios)

# Aplicar el descuento
precio_con_descuento = precio_total * (1 - descuento / 100)

print("Precio total sin descuento:", precio_total)
print("Precio total con descuento:", precio_con_descuento)
