'''
Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
indicando si la fecha es válida o no.
'''
#Definir la funcion fecha
def fecha():
    dia = int((input("Ingrese el dia: ")))
    mes = int((input("Ingrese el mes: ")))
    año = int((input("Ingrese el año: ")))
    if validarFecha(dia, mes, año):
        print("La fecha es válida.")
    else:
        print("La fecha no es válida.")
    return

#Validar fecha
def validarFecha(dia, mes, año):
    if mes < 1 or mes > 12:
        return False
    elif dia < 1 or dia > validarMes(mes, año):
        return False
    else:
        return True
    
#Validar mes
def validarMes(mes, año):
    match mes:
        #Meses con 31 días
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        #Meses con 30 días
        case 4 | 6 | 9 | 11:
            return 30
        #Febrero
        case 2:
            return 29 if bisiesto(año) else 28
        case _:
            return 0
        
#Validar año bisiesto
def bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

if (__name__ == '__main__'):
    dia = 0
    mes = 0
    año = 0
    fecha()
    bisiesto(año)
    validarMes(mes, año)
    validarFecha(dia, mes, año)