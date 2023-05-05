#CICLO WHILE:

i = 0
while i < 15:
	#Aquí se ejecutan las instrucciones que deseamos iterar.
	print(i)
	i = i + 1

print("Salí del while")


##----------------------------
#Iterador Genérico
# Si queremos que mi ciclo while se ejecute "n" veces:

i = 0
n = 3
while i < n:
	#Aquí se ejecutan las instrucciones que deseamos iterar.
	print(i)
	i = i + 1

###-------------------

band = ""

while band != "d":
	print("Menú de opciones:")
	print("a. Completo")
	print("b. Hamburguesa")
	print("c. Tequeño")
	print("d. Salir")
	band = input("Introduzca la opción deseada: ")

##-------------------------	


# while como acumulador

lista_notas = [5.2,6,4.8,6.1,7]
n = len(lista_notas)

i = 0
sumatoria = 0

while i < n:
	#Aquí se ejecutan las instrucciones que deseamos iterar.
	sumatoria = sumatoria + lista_notas[i]
	i = i + 1

prom = sumatoria/n
