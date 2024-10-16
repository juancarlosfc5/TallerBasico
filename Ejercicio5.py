'''
Crea un programa que pida al usuario ingresar el nombre de un país y luego
determine en qué continente se encuentra.Utiliza estructuras condicionales para
asociar cada país con su respectivo continente y muestra un mensaje con el
continente correspondiente.
'''

#Definir la funcion paises
def leerPais():
    #Solicitar el pais
    pais = (input("Ingrese el pais a consultar: "))
    #Validar continente
    match (pais):
        case 'Colombia':
            print(f'El pais {pais} se encuentra en el continente America del sur.')
        case 'España':
            print(f'El pais {pais} se encuentra en el continente Europa.')
        case 'Senegal':
            print(f'El pais {pais} se encuentra en el continente Africa.')
        case 'Australia':
            print(f'El pais {pais} se encuentra en el continente Oceanía.')
        case 'Japon':
            print(f'El pais {pais} se encuentra en el continente Asia.')
        case 'Antartida':
            print(f'El pais {pais} se encuentra en el continente Antártida.')
        case 'Estados Unidos':
            print(f'El pais {pais} se encuentra en el continente America del norte.')
        case _:
            print(f'El pais {pais} no se encuentra en la lista.')
    return
    
if (__name__ == '__main__'):
    leerPais()