def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Imprimir los primeros 10 números de la secuencia de Fibonacci
for i in range(30):
    print(fibonacci_recursive(i))