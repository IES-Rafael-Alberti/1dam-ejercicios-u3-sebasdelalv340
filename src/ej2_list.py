"""Ejercicio 3.1.2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
"""


def numAsignaturas(num):
    num = int(input("Introduce el número de asignaturas: "))
    if num is float:
        raise ValueError("Error - Debe ser un número entero.")
    else:
        return num


def crearAsignatura(asignatura):
    asignatura = input("Introduce la asignatura: ")
    return asignatura


def crearLista(listaAsignaturas, asignatura, num):
    for i in range(0, numAsignaturas(num)):
        listaAsignaturas.append(crearAsignatura(asignatura))

    return listaAsignaturas


def main():
    listaAsignaturas = []
    asignatura = ""
    num = 0
    try:
        listaAsignaturas = crearLista(listaAsignaturas, asignatura, num)
        for asignatura in listaAsignaturas:
            print(f"Yo estudio {asignatura}.")
    except ValueError:
        print("Entrada no válida.")       


if __name__ == "__main__":
    main()