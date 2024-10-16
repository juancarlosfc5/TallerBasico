'''
Escribe un programa que solicite al
usuario ingresar su edad y luego
determine si es mayor de edad o no
utilizando una declaración if. Si la edad
es mayor o igual a 18, muestra el
mensaje "Eres mayor de edad", de lo
contrario, muestra el mensaje "Eres
menor de edad".
'''
#Definir la funcion de edad
def leerEdad():
    edad = int(input("Ingrese su edad: "))
    #Validar de la funcion de edad
    if (edad <= 0):
        print("Edad erronea")
    #Ejecutar de la funcion de edad
    elif (edad >= 18):
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    return leerEdad

if (__name__ == '__main__'):
    edad = 0
    leerEdad()