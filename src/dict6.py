"""Ejercicio 3.2.6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

def pedir_nombre():
    nombre = input("Introduce tu nombre: ")
    return nombre


def pedir_edad():
    return int(input("Introduce tu edad: "))


def pedir_genero():
    return input("Introduce tu sexo: ")


def pedir_telefono():
    return int(input("Introduce tu número de teléfono: "))


def pedir_email():
    return input("Introduce tu email: ")


def crear_diccionario(diccionario):



def main():
    diccionario = dict()

if __name__ == "__main__":
    main()