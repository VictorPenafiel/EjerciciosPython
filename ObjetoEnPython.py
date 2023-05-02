class Cliente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
cliente = [
    Cliente("Juan", "Perez", 23),
    Cliente("Maria", "Perez", 33),
    Cliente("Ximena", "Perez", 43),
]

print(cliente[0].nombre)
