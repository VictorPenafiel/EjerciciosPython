from abc import ABC, abstractmethod
from producto import Producto


class Tienda(ABC):
    @abstractmethod
    def ingresar_producto(self, nombre: str, precio: int, stock: int):
        pass
        
    @abstractmethod
    def listar_productos(self) -> str:
        pass
        
    @abstractmethod
    def realizar_venta(self, nombre_producto: str, cantidad: int):
        pass


# Aquí comienzo a crear a los hijos
class TiendaRestaurante(Tienda):
    tipo = "Restaurante"
    
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []
    
    def ingresar_producto(self, nombre, precio, stock):
        p = Producto(nombre, precio)    ## aquí está la composición
        
        encontrados = list(filter(lambda x: x == p, self.__productos))
        ## la comprehension anterior se puede implementar de manera "clásica" así:
        ##
        ##  encontrados = []
        ##  for item in productos:
        ##      if item == p:
        ##          encontrados.append(p)
        ##
        
        
        if len(encontrados) == 0:
            self.__productos.append(p)
    
    def listar_productos(self):
        if len(self.__productos):
            retorno = ""
            for p in self.__productos:
                retorno += f"NOMBRE: {p.nombre}\t" + \
                    f"PRECIO: ${p.precio}\t"

            return retorno
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto, cantidad):
        pass


class TiendaFarmacia(Tienda):
    tipo = "Farmacia"

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, nombre, precio, stock):
        p = Producto(nombre, precio, stock)
        encontrados = list(filter(lambda x: x == p, self.__productos))
        ## aquí pueden ocupar la alternativa comentada en TiendaRestaurante, en vez de la línea anterior
        
        if len(encontrados) == 0:
            self.__productos.append(p)
        else:
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[indice]

    def listar_productos(self):
        if len(self.__productos):
            retorno = ""
            for p in self.__productos:
                m = "" 
                if p.precio > 15000:
                    m = " (Envío gratis al solicitar este producto)" 
                retorno += f"NOMBRE: {p.nombre}\t" + \
                    f"PRECIO: ${p.precio}{m}\t"

            return retorno
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad <= 3:
            p = Producto(nombre_producto, 0, cantidad)
            encontrados = list(filter(lambda x: x == p, self.__productos))

            if len(encontrados) and encontrados[0].stock:
                tmp = encontrados[0] - p
                nuevo_stock = tmp if tmp > 0 else 0
                indice = self.__productos.index(p)
                self.__productos[indice].stock = nuevo_stock


class TiendaSupermercado(Tienda):
    tipo = "Supermercado"

    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    def ingresar_producto(self, nombre, precio, stock):
        p = Producto(nombre, precio, stock)
        encontrados = list(filter(lambda x: x == p, self.__productos))
        ## aquí pueden ocupar la alternativa comentada en TiendaRestaurante, en vez de la línea anterior
        
        if len(encontrados) == 0:
            self.__productos.append(p)
        else:
            indice = self.__productos.index(p)
            self.__productos[indice].stock = p + self.__productos[indice]

    def listar_productos(self):
        if len(self.__productos):
            retorno = ""
            for p in self.__productos:
                m = "" 
                if p.stock < 10:
                    m = " (Pocos productos disponibles)" 
                retorno += f"NOMBRE: {p.nombre}\t" + \
                    f"PRECIO: ${p.precio}\t" + \
                        f"STOCK: {p.stock}{m}"

            return retorno
        else:
            return "No hay productos para esta tienda"

    def realizar_venta(self, nombre_producto, cantidad):
        p = Producto(nombre_producto, 0, cantidad)
        encontrados = list(filter(lambda x: x == p, self.__productos))

        if len(encontrados) and encontrados[0].stock:
            tmp = encontrados[0] - p
            nuevo_stock = tmp if tmp > 0 else 0
            indice = self.__productos.index(p)
            self.__productos[indice].stock = nuevo_stock
