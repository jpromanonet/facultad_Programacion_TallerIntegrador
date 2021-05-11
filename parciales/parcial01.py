# Validador de passwords en Python

# Importo la libreria de expresiones regulares llamada 're'
import re

# Interfaz de usuario
print("Crea tu usuario y contraseña")
print("")
print("la misma no puede tener menos de 6 caracteres ni mas de 12, al menos una letra minuscula y una mayuscula y un numero")

# Funcion que valida las expresiones regulares de las password
def passwordValidate(password):
    if len(password) >= 6 and len(password) <= 12 and re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]", password):
        return True
    return False


# Logica de validacion de contraseñas
print(
    "Si la contraseña no cumple los parametros, el sistema te indicara que vuelvas a ingresar otra contraseña."
)
print("")
usuario = input("Ingresa un usuario: ")

# Bucle que llama a la funcion para validar la contraseña
while True:
    print("")
    passwordFinal = input("Ingresa la nueva contraseña: ")
    if passwordValidate(passwordFinal):
        print("")
        print("¡Registro exitoso!")
        print("")
        break
    else:
        print("")
        print("Tu contraseña no cumple con los parametros, volve a intentarlo.")
