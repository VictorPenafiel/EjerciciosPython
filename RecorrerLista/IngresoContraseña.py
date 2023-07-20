contrasena_predefinida = "12345"

contrasena_usuario = input("Ingrese su contraseña: ")

while contrasena_usuario != contrasena_predefinida:
    contrasena_usuario = input("Contraseña incorrecta. Intente nuevamente: ")

print("Contraseña correcta. Bienvenido.")