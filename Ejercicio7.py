'''
Crea un programa que solicite al usuario ingresar tres
longitudes y determine si esas longitudes pueden formar
un triángulo válido. Utiliza la desigualdad triangular
para realizar la comprobación y muestra un mensaje
indicando si se puede formar un triángulo o no.
La desigualdad triangular es un concepto matemático
que establece una condición necesaria para que tres
segmentos puedan formar un triángulo válido. La
desigualdad triangular establece que la suma de las
longitudes de dos lados de un triángulo siempre debe ser
mayor que la longitud del tercer lado.
En términos más precisos, si tienes tres segmentos con
longitudes a, b y c, donde a, b y c son números
positivos, entonces estos segmentos pueden formar un
triángulo válido si y solo si se cumple la siguiente
condición:
a + b > c
a + c > b
b + c > a
'''

#Definir la desigualdad triangular
def validarTriangulo():
    #Solicitar la longitud de los lados del triangulo
    a = float((input("Ingrese la longitud del lado a del triangulo: ")))
    b = float((input("Ingrese la longitud del lado b del triangulo: ")))
    c = float((input("Ingrese la longitud del lado c del triangulo: ")))
    #Validar triangulo
    if (a+b > c and a+c > b and b+c > a):
        print("Los segmentos pueden formar un triángulo.")
    else:
        print("Los segmentos no pueden formar un triángulo.")
    return
    
if (__name__ == '__main__'):
    a = 0
    b = 0
    c = 0
    validarTriangulo()