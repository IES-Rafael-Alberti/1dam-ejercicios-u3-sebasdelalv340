"""Ejercicio 3.1.4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""


def pedirNum() -> int:
    n = int(input("Introduce un número: "))
    if n < 1 or n > 49:
        raise ValueError("Error - Los números deben estar entre 1 y 49.")
    else:
        return n
    

def pedirReintegro() ->int:
    r = int(input("Introduce el reintegro: "))
    if r < 1 or r > 9:
        raise ValueError("Error - El reintegro debe ser un número entre 1 y 9:")
    else:
        return r
    

def crearLista() -> list:
    listaLoteria = list(pedirNum() for i in range(6))               
    
    for numero in listaLoteria:
        if listaLoteria.count(numero) >= 2:
            raise ValueError
    
    ordenarLista(listaLoteria)
    listaLoteria.append(pedirReintegro())

    return listaLoteria


def ordenarLista(listaLoteria) -> list:
    return listaLoteria.sort()


def main():

    try:
        listaLoteria = crearLista()   
        print(listaLoteria)
    except ValueError:
        print("El número es incorrecto.")


if __name__ == "__main__":
    main()