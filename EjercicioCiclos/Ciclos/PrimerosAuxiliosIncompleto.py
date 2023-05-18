emergencia = int(input("""¿Responde a Estímulos?:
    1. si
    2. no
    > """))
if emergencia == 1:
    print("Valorar la necesidad de llevarlo al hospital más cercano")
elif emergencia == 2:
    print("Abrir la Vía Aérea")

emergencia2 = int(input("¿Respira?"))
if emergencia2 == 1: 
    print("Permitirle posición de suficiente ventilacion")
if emergencia2 == 2:
    print("Administrar 5 ventilaciones y llamar a la Ambulancia")

emergencia3 = int(input("¿Signos de Vida?"))
if emergencia3 == 1:
    print("Reevaluar a la espera de la Ambulancia")
if emergencia3 == 2:
    print("Administar compresiones Torácicas hasta que llegue la ambulancia")

print("¿Llegó la Ambulancia?")
