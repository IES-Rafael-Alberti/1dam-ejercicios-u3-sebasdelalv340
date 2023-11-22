"""Ejercicio 3.1.1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""


def numAsignaturas(num):
    num = int(input("Introduce el número de asignaturas: "))
    if num is float:
        raise ValueError("Error")
    else:
        return num


def crearAsignatura(asignatura) -> str:
    asignatura = input("Introduce una asignatura: ")
    return asignatura


def crearLista(listaAsignaturas, asignatura, num):
    for i in range(numAsignaturas(num)):
        listaAsignaturas.append(crearAsignatura(asignatura))

    return listaAsignaturas


def main():
    listaAsignaturas = []
    asignatura = ""
    num = ""
    try:
        crearLista(listaAsignaturas, asignatura, num)
        print(listaAsignaturas)
    except ValueError:
        print("Entrada incorrecta.")
    


if __name__ == "__main__":
    main()