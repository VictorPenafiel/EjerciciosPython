"""
La seguridad en las contraseñas es un tema importante, ya que dependiendo de la
complejidad que tiene dicha contraseña pueden depender datos de extrema sensibilidad.
Una persona le dice que ha generado dos códigos para clasificar las contraseñas, pero no
logra entender cuál es la diferencia entre cada uno y cuál es el que él necesita. Por ello, el
objetivo final de la aplicación es clasificar la contraseña según los siguientes criterios:
● 4 letras o menos será corta.
● 5 a 10 letras será mediana.
● Más de 10 letras será larga.
"""


from getpass import getpass # Importamos la funcion getpass() del modulo getpass.

password = getpass("Ingrese una Contraseña: ")  # Solicita al usuario una contraseña sin mostrarla en la pantalla
largo = len(password) # Funcion len() devuelve el numero de caracteres de un string
if largo <= 2: #Clasifica la contraseña según su longitud
    print("Pequeña")
elif largo <= 4:
    print("Mediana")
elif largo <= 6:
    print("Larga")
else:
    print("Muy Larga")
