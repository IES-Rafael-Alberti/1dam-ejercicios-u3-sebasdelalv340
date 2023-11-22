"""Ejercicio 3.1.9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""


def pedirPalabra() -> tuple:
    palabra = tuple(input("Introduce una palabra: "))
    return palabra

def contarVocales(palabra: tuple) -> tuple:
    vocales = (["a", 0], ["e", 0], ["i", 0], ["o", 0], ["u", 0])
    for vocal in vocales:
        vocal[1] = palabra.count(vocal[0])
    return vocales


def mostrarVocales(vocales):
    for vocal in vocales:
        print(vocal[0]+ "=" + str(vocal[1]))


def main():
   palabra = pedirPalabra()
   vocales = contarVocales(palabra)
   mostrarVocales(vocales)
   

if __name__ == "__main__":
    main()