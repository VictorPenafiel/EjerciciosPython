# memoria: almacenara los valores previos
fibonacci_cache = {}

def fibonacci_memo(n):
    # si el valor esta almacenado en fibonacci_cache solo lo retornamos
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1 or n == 2:
        val = 1
    else:
        val = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)

    # agregamos resultados a memoria fibonacci_cache
    fibonacci_cache[n] = val
    # retornamos valor
    return val

for x in range(1, 30):
    print(x, " : ", fibonacci_memo(x))