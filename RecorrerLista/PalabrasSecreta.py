palabra_secreta = "manzana"
adivinanzas = []
intentos = 5

while intentos > 0:
    adivinanza = input("Adivina la palabra secreta: ")
    if adivinanza == palabra_secreta:
        print("¡Felicidades! Has adivinado la palabra secreta.")
        break
    else:
        print("Lo siento, esa no es la palabra secreta.")
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")
else:
    print("Lo siento, has agotado todos tus intentos. La palabra secreta era", palabra_secreta)