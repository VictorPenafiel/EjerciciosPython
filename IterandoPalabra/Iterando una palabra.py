i = 0
palabra = "Paralelepipedo"
while i < len(palabra):
    if palabra[i] == "a" or palabra[i] =="e" or palabra[i] =="i" or palabra[i] =="o" or palabra[i] =="u":
        i += 1
        continue
    
    print(f"Posicion {i + 1}:",palabra[i])
    i += 1