import random

numero_aleatorio = random.randint(1, 10)
numero_jugador = 0
intentos = 0

while numero_jugador != numero_aleatorio:
    numero_jugador = int(input("Adivina el número entre 1 y 10: "))
    intentos += 1

    if numero_jugador < numero_aleatorio:
        print("El número es mayor.")
    elif numero_jugador > numero_aleatorio:
        print("El número es menor.")

print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")