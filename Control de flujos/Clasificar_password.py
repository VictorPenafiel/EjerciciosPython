""" Crear un programa donde el usuario debe ingresar un password en la plataforma. Si el password tiene menos de 6 letras, se debe mostrar el aviso “El password es demasiado corto”. """


password = input('Ingrese un Password: ')

if len(password) < 6:
    print('El password ingresado es demasiado corto')
    
# También es posible resolver esto con getpass como sigue
#       import getpass
#       password = getpass.getpass('Ingrese un Password: ')