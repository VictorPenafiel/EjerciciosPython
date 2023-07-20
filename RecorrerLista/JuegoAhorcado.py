import random

def jugar_ahorcado():
    palabras = ["manzana", "banana", "naranja", "fresa", "uva"]
    palabra = random.choice(palabras)
    palabra_secreta = list(palabra)
    letras_adivinadas = ["_"] * len(palabra_secreta)
    intentos = 6

    while intentos > 0:
        print(" ".join(letras_adivinadas))
        letra = input("Ingresa una letra: ").lower()
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    letras_adivinadas[i] = letra
            if "_" not in letras_adivinadas:
                print("¡Felicidades! Has adivinado la palabra secreta:", palabra)
                break
        else:
            intentos -= 1
            print(f"Lo siento, la letra {letra} no está en la palabra secreta. Te quedan {intentos} intentos.")
    else:
        print(f"Lo siento, has perdido. La palabra secreta era {palabra}.")

jugar_ahorcado()