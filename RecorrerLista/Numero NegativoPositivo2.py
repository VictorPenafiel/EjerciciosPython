# recibiendo el numero en variable

numero = (input("Ingresa un numero entero: "))
# verificar si es cero
# verificar que sea postivo (mayor a cero)
# verificar si es positivo par, si es positivo impar
# verificar si es negativo par, si es negativo impar
# imprimir
try:
    numero = int(numero)
    if numero == 0:
        print(f"El número {numero} es igual a cero")
    elif numero > 0:
        if (numero % 2) == 0:
            print(f"El número {numero}, es positivo y par")
        else:
            print(f"El número {numero}, es positivo e impar")
    else:           
        if (numero % 2) == 0:
            print(f"El número {numero}, es negativo y par")
        else:
           print(f"El número {numero}, es negativo e impar")
except ValueError:
    print("Lo ingresado NO es un número entero")