from functools import reduce, partial

def aplicar_descuento(precio, descuento):
    return precio * (1 - descuento / 100)

precios = [25.50, 12.30, 36.40, 9.75, 15.20]
descuento = 10

aplicar_descuento_parcial = partial(aplicar_descuento, descuento=descuento)
precio_total = sum(precios)
precio_con_descuento = reduce(lambda total, precio: total + aplicar_descuento_parcial(precio), precios, 0)

print("Precio total sin descuento:", precio_total)
print("Precio total con descuento:", precio_con_descuento)
