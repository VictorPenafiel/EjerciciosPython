def calcular_precio_con_descuento(precios, descuento):
    precio_total = sum(precios)
    precio_con_descuento = precio_total * (1 - descuento / 100)
    return precio_con_descuento

precios = [25.50, 12.30, 36.40, 9.75, 15.20]
descuento = 10

precio_total = sum(precios)
precio_con_descuento = calcular_precio_con_descuento(precios, descuento)

print("Precio total sin descuento:", precio_total)
print("Precio total con descuento:", precio_con_descuento)
