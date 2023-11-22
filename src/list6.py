"""Ejercicio 3.1.6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""
from ej1_list import crearLista
from ej1_list import crearAsignatura
from ej1_list import numAsignaturas

def crear_nota():
    nota = int(input("Introduce la nota: "))
    return nota


def crearLista(listaAsignaturas, asignatura, num):
    for i in range(numAsignaturas(num)):
        lista_nota = []
        lista_nota.append(crearAsignatura(asignatura))
        lista_nota.append(crear_nota())
        listaAsignaturas.append(lista_nota)
    
    return listaAsignaturas


def comprobar_notas(listaAsignaturas):
    for i in range(len(listaAsignaturas)):
        for j in range(2):
            if j < 5:      
                return print("Las asignaturas a repetir son: " + str(i))

def main():
    listaAsignaturas = []
    asignatura = ""
    num = 0
    try:
        crearLista(listaAsignaturas, asignatura, num)
        comprobar_notas(listaAsignaturas) 
    except ValueError:
        print("Entrada incorrecta.")


if __name__ == "__main__":
    main()