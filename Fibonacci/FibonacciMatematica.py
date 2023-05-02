from math import sqrt

def F(n):
    return ((1 + sqrt(5)) ** n - (1 - sqrt(5)) ** n) / (2 ** n * sqrt(5))

def fibonacci_formula(startNumber, endNumber):
    n = 0
    cur = F(n)
    result = []
    while cur <= endNumber:
        if startNumber <= cur:
            result.append(cur)
        n += 1
        cur = F(n)
    return result

print(fibonacci_formula(1, 34444330))