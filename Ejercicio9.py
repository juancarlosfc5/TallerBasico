'''
Crea un programa que solicite al usuario
ingresar una serie de números positivos y
luego calcule e imprima el promedio de los
números ingresados utilizando un bucle while.
El programa debe terminar cuando el usuario
ingrese un número negativo.
'''

#Definir la funcion numero
def leerNumero():
    Suma = 0
    Contador = 0
    while True:
        Numero = float(input("Ingrese un numero que desee para calcular el promedio: \nEscribe un numero negativo para cerrar el programa: "))
        if (Numero < 0):
            break
        else:
            Suma += Numero
            Contador += 1
        
    Promedio = round(Suma/Contador,2)
    print(f'El promedio de los numeros ingresados es: {Promedio}')

if (__name__ == '__main__'):
    Numero = 0
    Promedio = 0
    leerNumero()