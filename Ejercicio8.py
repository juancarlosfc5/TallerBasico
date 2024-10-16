'''
Escribe un programa que solicite al usuario
ingresar un número y luego muestre la tabla
de multiplicar de ese número del 1 al 10
'''

#Definir la funcion numero
def leerNumero():
    #Solicitar dato
    Numero = int(input("Ingrese un numero para el que desea crear la tabla de multiplicar: "))
    #Validar numero entero positivo
    if (Numero <= 0):
        print("El numero debe ser positivo")
    else:
        Contador = 1
        #Imprimir resultados de iteración hasta 10
        while (Contador <= 10):
            Tabla = Numero * Contador
            print(f'El numero {Numero} x {Contador} es igual a: {Tabla}')
            Contador += 1

if (__name__ == '__main__'):
    Numero = 0
    Tabla = 0    
    leerNumero()