from ingredientes import proteina, vegetales, masa

class Pizza():
    precio = 10000
    tamano = "Familiar"

    @staticmethod
    def validar_elemento(ingresado,posibles):
        return ingresado.lower() in posibles

    def pedir(self):
        self.prot = input(f"Ingrese la proteina deseada.\nLas opciones son: {','.join(proteina)}>")
        self.veg_1 = input(f"Ingrese el primer ingrediente vegetal. Opciones:{','.join(vegetales)}>")
        self.veg_2 = input(f"Ingrese el segundo ingrediente vegetal: {','.join(vegetales)} >")
        self.tipo_masa = input(f"Ingrese el tipo de masa: {','.join(masa)} >")

        self.pedido_valido = self.validar_elemento(self.prot,proteina) and \
            self.validar_elemento(self.veg_1,vegetales) and \
            self.validar_elemento(self.veg_2, vegetales) and \
            self.validar_elemento(self.tipo_masa,masa)


