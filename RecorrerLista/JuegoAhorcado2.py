import random

personas = ["Natalia", "Joaquin", "Onofrio", "Adrian", "Victor", "Eduardo", "Federico", "Aaron", "Ignacio", "Camilo"]
palabra = random.choice(personas).lower()
adivinado = []
vidas = 6

# Función para mostrar el estado actual del juego
def mostrar_estado(adivinado, palabra):
    """ Muestra el estado actual del juego, con las letras adivinadas y las letras que faltan por adivinar """
    for letra in palabra:
        if letra in adivinado:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print("\n")

# Comenzar el juego
print("¡Bienvenido al juego del ahorcado, versiòn compañeros del Bootcamp!\n")
mostrar_estado(adivinado, palabra)

while True:
    letra = input("Introduce una letra: ")
    adivinado.append(letra)
    if letra not in palabra:
        vidas -= 1
        print("La letra", letra, "no está en el nombre del compañero. Te quedan", vidas, "vidas.")
        if vidas == 0:
            print("¡Has perdido! el compañero era", palabra)
            break
    else:
        print("¡La letra", letra, "está en el nombre!")
    # Mostrar el estado actual del juego
    mostrar_estado(adivinado, palabra)
    # Comprobar si el jugador ha adivinado todas las letras
    if all(letra in adivinado for letra in palabra):
        print("¡Felicidades! ¡Has ganado!")
        break