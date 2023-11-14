"""Ejercicio 3.1.4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
"""
n = ""
r = ""
listaLoteria = []

def pedirNum(n: int):
    n = int(input())
    if n < 1 or n > 49:
        raise ValueError("Error - Los números deben estar entre 1 y 49.")
    else:
        return n
    

def pedirReintegro(r: int):
    r = int(input("Introduce el reintegro: "))
    if r < 1 or r > 9:
        raise ValueError("Error - El reintegro debe ser un número entre 1 y 9:")
    else:
        return r
    

def crearLista(listaLoteria: list):
    numero = 0
    for i in range(0, 6):        
        numero = listaLoteria.append(pedirNum(n))           
        if listaLoteria.count(numero) == 2:
            raise ValueError("Error - No se puede repetir los números.") 

    listaLoteria.append(pedirReintegro(r))

    return listaLoteria

def main():
    
    try:
        print("Introduce los números ganadores: ")
        print(crearLista(listaLoteria))
    except ValueError:
        print("El número es incorrecto.")


if __name__ == "__main__":
    main()