# Conjuntos para almacenar los nombres de los invitados confirmados y los invitados que han llegado
invitados_confirmados = {"Juan", "Maria", "Pedro", "Ana"}
invitados_asistieron = set()

# Función para agregar un invitado que ha llegado a la fiesta
def agregar_invitado(nombre):
    invitados_asistieron.add(nombre)

# Función para imprimir la cantidad de invitados confirmados y la cantidad de invitados que han asistido
def imprimir_cantidad_invitados():
    print("Invitados confirmados:", len(invitados_confirmados))
    print("Invitados asistieron:", len(invitados_asistieron))

# Función para imprimir los nombres de los invitados que confirmaron pero aún no han llegado
def invitados_pendientes():
    pendientes = invitados_confirmados - invitados_asistieron
    print("Invitados pendientes:", pendientes)

# Ejemplo de uso
agregar_invitado("Juan")
agregar_invitado("Maria")
imprimir_cantidad_invitados()
invitados_pendientes()
