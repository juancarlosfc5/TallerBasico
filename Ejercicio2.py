'''
Crea un programa que solicite al
usuario un número entero positivo y
luego imprima los números desde ese
número hasta 1 utilizando un
buclewhile.
'''
#Definir la funcion numero
def leerNumero():
    #Solicitar dato
    Numero = int(input("Ingrese un numero entero positivo: "))
    #Validar numero entero positivo
    if (Numero <= 0):
        print("El numero debe ser positivo")
    #Imprimir resultados de iteración hasta 1
    while (Numero >= 1):
        print(f'{Numero}')
        Numero -= 1

if (__name__ == '__main__'):
    Numero = 0
    leerNumero()