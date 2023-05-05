def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        print("Error: no se puede dividir por cero")
    else:
        return num1 / num2

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion_valida = False
    while not opcion_valida:
        try:
            opcion = int(input("Opción: "))
            if opcion < 1 or opcion > 4:
                print("Ingrese una opción válida (1-4)")
            else:
                opcion_valida = True
        except ValueError:
            print("Ingrese una opción válida (1-4)")
    
    return opcion
def solicitar_numeros():
    num1_valido = False
    while not num1_valido:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num1_valido = True
        except ValueError:
            print("Ingrese un número válido")
    
    num2_valido = False
    while not num2_valido:
        try:
            num2 = float(input("Ingrese el segundo número: "))
            num2_valido = True
        except ValueError:
            print("Ingrese un número válido")
    
    return num1, num2


continuar = True
while continuar:
    opcion = mostrar_menu()
    num1, num2 = solicitar_numeros()
    
    if opcion == 1:
        resultado = sumar(num1, num2)
        print("El resultado es: ", resultado)
    elif opcion == 2:
        resultado = restar(num1, num2)
        print("El resultado es: ", resultado)
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
        print("El resultado es: ", resultado)
    elif opcion == 4:
        resultado = dividir(num1, num2)
        if resultado is not None:
            print("El resultado es: ", resultado)
    
    continuar_str = input("¿Desea realizar otra operación? (s/n): ")
    continuar = continuar_str.lower() == "s"
