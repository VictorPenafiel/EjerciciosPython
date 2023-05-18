import sys

peso = float(sys.argv[1])
altura = float(sys.argv[2])

altura = altura/100
imc = peso/(altura**2)

print (f'Su IMC es {imc:.2f}\nLa clasificación OMS es') 

if imc <18.5:
    print('Bajo de Peso')
elif imc >18.5 and imc<25:
    print('Adecuado')
elif imc >25 and imc<30:
    print('Sobrepeso')
elif imc >30 and imc<35:
    print('Obesidad Grado I')
elif imc >35 and imc<40:
    print('Obesidad Grado II')
else:
    print('Obesidad Grado III')
