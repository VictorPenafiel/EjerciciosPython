"""Crear un programa donde el usuario debe ingresar un password. Si el password es 12345, entonces se debe informar que el password es incorrecto."""

password = input('Ingrese un Password: ')
# También es posible resolver con getpass 
# import getpass
# password = getpass.getpass('Ingrese un Password: ')
if password == '12345':
    print('El password es incorrecto')