"""Ejercicio 3.1.5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas."""


def crearLista(lista):
    for i in reversed(range(1, 11)):
        lista.append(i)

    return lista


def main():
    lista = []
    try:
        print(crearLista(lista))
    except Exception:
        print("Error")
    

if __name__ == "__main__":
    main()