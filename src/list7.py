"""Ejercicio 3.1.8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""


def pedirPalabra(palabra):
    return input("Introduce una palabra: ")




palabra = "ana"
palabra_original = list(palabra)
palabra_al_reves = list(palabra)
palabra_al_reves.reverse()

if palabra_original == palabra_al_reves:
    print("Es un palídromo.")
else:
    print("No es un palídromo.")