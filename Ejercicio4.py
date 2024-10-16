'''
Crea un programa que solicite al
usuario ingresar una contraseña y
verifique si cumple con los siguientes
requisitos: debe tener al menos 8
caracteres y contener al menos un
número. Si la contraseña cumple con
los requisitos, muestra el
mensaje"Contraseña válida". De lo
contrario, muestra el mensaje
"Contraseña inválida".
'''

#Definir la funcion contraseña
def leerContraseña():
    #Solicitar contraseña
    contraseña = (input("Ingrese su contraseña: "))
    #Validar contraseña
    if (len(contraseña) < 8):
        print("Contraseña inválida. Debe tener al menos 8 caracteres.")
    elif (not any(char.isdigit() for char in contraseña)):
        print("Contraseña inválida. Debe contener al menos un número.")
    else:
        print("Contraseña válida.")
    return
    
if (__name__ == '__main__'):
    leerContraseña()