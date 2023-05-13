from modelo.persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, rut, descuento):
        super().__init__(nombre, apellido, rut)
        self._descuento = descuento
        
    @property
    def descuento(self):
        return self.descuento
    
    @descuento.setter
    def descuento(self, descuento):
        self._descuento = descuento
        
    def __str__(self):
        return f'Cliente(nombre={self.nombre}, apellido={self.apellido}, rut={self._rut}, descuento{self._descuento})'
    
        