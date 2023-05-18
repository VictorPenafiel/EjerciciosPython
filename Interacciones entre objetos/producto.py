class Producto():
    def __init__(self, nombre: str, precio: int, stock: int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock if stock > 0 else 0

    #Creamos getters para todos, pero setter solo para stock (se interpreta en el problema)
    @property
    def nombre(self) -> str:
        return self.__nombre
        
    @property
    def precio(self) -> int:
        return self.__precio
        
    @property
    def stock(self) -> int:
        return self.__stock
        
    @stock.setter
    def stock(self, stock):
        self.__stock = stock if stock > 0 else 0
    
    #Aquí aprovechamos de sobrecargar los operadores +, - y ==
    def __add__(self, other) -> bool:
        return self.stock + other.stock

    def __sub__(self, other) -> bool:
        return self.stock - other.stock
        
    def __eq__(self, other) -> bool:
        return self.nombre == other.nombre