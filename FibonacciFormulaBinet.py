from math import sqrt

# Constante phi (proporción áurea)
phi = (1 + sqrt(5)) / 2

def fibonacci_binet(n):
    return round((phi ** n - (-phi) ** (-n)) / sqrt(5))

# Imprimir los primeros 10 números de la secuencia de Fibonacci
for i in range(30):
    print(fibonacci_binet(i))
