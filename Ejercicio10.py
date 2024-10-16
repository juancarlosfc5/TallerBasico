'''
En su casa le solicitan que
realice un algoritmo en Python,
que permita calcular el valor a
pagar por concepto de energía
eléctrica. Los datos que se
conocen son los siguientes:
-Mes de consumo
-Valorkw
-Totalkwconsumido en el mes
-estrato
'''

#Definir la funcion numero
def calcularConsumo():
    estrato = int(input('Ingrese su estrato (1 al 6): '))
    valorKw = float(input('Ingrese el valor del Kw de su estrato: '))
    mes = input('Ingrese el mes del consumo: ')
    TotalKw = float(input('Ingrese el total Kw consumido en el mes: '))
    if (estrato <= 2 and TotalKw <= 100):
        print(f'El valor del consumo de energia en el {mes} es 0 pesos, estas subsidiado')
    elif (estrato <= 2 and TotalKw > 100):
        costo = round((TotalKw-100)*valorKw,2)
        print(f'El valor del consumo de energia en el {mes} es {costo} pesos, el subsidio solo aplica para consumos de menos de 100 Kw')
    else:
        print(valorKw)
        costo = round(TotalKw*valorKw,2)
        print(f'El valor del consumo de energia en el {mes} es {costo} pesos para un costo de Kw {valorKw} para el estrato {estrato}')

if (__name__ == '__main__'):
    valorKw = 0
    TotalKw = 0
    costo = 0
    mes = ""
    calcularConsumo()