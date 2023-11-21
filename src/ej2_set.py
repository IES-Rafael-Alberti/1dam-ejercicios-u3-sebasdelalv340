"""Ejercicio 3.3.2
Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
Mostrar si todos los nombres de primaria están incluidos en secundaria.
"""

def pedir_nombres_primaria(primaria: set) -> set:
    nombre_pila = input("Introduce los nombre de pila de los alumnos de primaria:\n")
    primaria.add(nombre_pila)

    while nombre_pila != "x":
        nombre_pila = input()
        if nombre_pila != "x":
            primaria.add(nombre_pila)

    return primaria


def pedir_nombres_secundaria(secundaria: set) -> set:

    nombre_pila = input("Introduce los nombre de pila de los alumnos de secundaria:\n")
    secundaria.add(nombre_pila)

    while nombre_pila != "x":
        nombre_pila = input()
        if nombre_pila != "x":
            secundaria.add(nombre_pila)

    return secundaria


def mostrar_sin_repeticiones(primaria: set, secundaria: set) -> set:
    lista_union = primaria | secundaria
    return print("Los nombres de ambas listas son: " + ", ".join(lista_union))


def mostrar_repetidos(primaria: set, secundaria: set) -> set:
    lista_repetidos = primaria & secundaria
    return print("Los nombres repetidos en ambas listas son: " + ", ".join(lista_repetidos))
    

def mostrar_unicos(primaria: set, secundaria: set) -> set:
    lista_unicos = primaria - secundaria
    return print("Los nombres únicos en primaria son: " + ", ".join(lista_unicos))


def mostrar_incluidos(primaria: set, secundaria: set) -> set:
    if primaria <= secundaria:
        print("Si")
    else:
        print("No")

def main():
    primaria = set()
    secundaria = set()

    pedir_nombres_primaria(primaria)
    pedir_nombres_secundaria(secundaria)

    mostrar_sin_repeticiones(primaria, secundaria)
    
    mostrar_repetidos(primaria, secundaria)

    mostrar_unicos(primaria, secundaria)

    print("¿Están todos los nombres de los alumnos de primaria incluidos en secundaria?: ")
    mostrar_incluidos(primaria, secundaria)


if __name__ == "__main__":
    main()