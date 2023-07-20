precios = [25.50, 12.30, 36.40, 9.75, 15.20]
descuento = 10

precios_con_descuento = [precio * (1 - descuento / 100) for precio in precios]
precio_total = sum(precios)
precio_con_descuento = sum(precios_con_descuento)

print("Precio total sin descuento:", precio_total)
print("Precio total con descuento:", precio_con_descuento)
