"""Ejercicio 3.1.11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
"""


def multiplicar(lista1, lista2):
    vector = list()
    for i in range(3):
        vector += str(lista1[i] * lista2[i]) + ", "
        
    return vector


def main():
    lista1 = (1,2,3)
    lista2 = (-1,0,2)
    multiplicar(lista1, lista2)

if __name__ == "__main__":
    main()