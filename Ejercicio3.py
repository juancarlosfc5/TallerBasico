'''
Escribe un programa que solicite al
usuario ingresar su calificación en un
examen y determine si ha aprobado o
no. Si la calificación es igual o mayor a
60, muestra el mensaje "Has aprobado".
De lo contrario, muestra el mensaje "Has
reprobado".
'''

#Definir la funcion numero
def leerCalificacion():
    #Solicitar dato
    calificacion = int(input("Ingrese su calificación: "))
    #Validar numero entero positivo
    if (calificacion <= 0 or calificacion > 100):
        print("El rango de notas es de 0 a 100")
    #Verificar aprobación
    elif (calificacion >= 60):
        print("Has aprobado")
    else:
        print("Has reprobado")
    return calificacion
    
if (__name__ == '__main__'):
    calificacion = 0
    leerCalificacion()