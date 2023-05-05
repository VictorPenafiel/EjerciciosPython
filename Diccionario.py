claves = ["a", "b", "c"]
valores = [1, 2, 3]
nuevo_diccionario = {}
for i in range(len(claves)):
    nuevo_diccionario[claves[i]] = valores[i]
print(nuevo_diccionario)




claves = ('a', 'b', 'c')
valores = (1, 2, 3)
thisdict = dict(zip(claves, valores))
print(thisdict)