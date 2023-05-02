def fibonacci_generator(limit):
    num1, num2 = 0, 1
    for _ in range(limit):
        yield num1
        num1, num2 = num2, num1 + num2

# Imprimir los primeros 10 números de la secuencia de Fibonacci
for num in fibonacci_generator(30):
    print(num)