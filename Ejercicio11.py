'''
Construya un algoritmo en Python, que
permita ingresar la información de un
empleado e imprima el nombre, los apellidos
y la antigüedad. Los datos que se deben
solicitar son los siguientes:
*Nombre
*Teléfono
*Año de ingreso a la empresa
*Apellidos
*Edad
'''

#Definir la funcion numero
def calcularConsumo():
    añoIngreso = 0
    nombre = input('Ingrese los nombres del trabajador: ')
    apellidos = input('Ingrese los apellidos del trabajador: ')
    añoIngreso = int(input('Ingrese el año de ingreso del trabajador: '))
    edad = int(input('Ingrese la edad del trabajador: '))
    telefono = input('Ingrese el telefono del trabajador: ')
    if (añoIngreso <= 0 or edad <= 0):
        print('Datos incorrectos')
    else:
        antiguedad = 2024-añoIngreso
        print(f'***Datos del trabajador***\nNombre: {nombre}\nApellidos: {apellidos}\nAntigüedad: {antiguedad} años')

if (__name__ == '__main__'):
   calcularConsumo()