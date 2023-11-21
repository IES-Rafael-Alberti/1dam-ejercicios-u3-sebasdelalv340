"""Ejercicio 3.1.12
Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""

def multiplicar(matriz_1: tuple, matriz_2: tuple) -> tuple:
    vector = list()
    
    for i in range(3):
        vector_colm = list()
        for j in range(2):    
            vector_colm.append(matriz_1[i][j] * matriz_2[i][j])
        vector.append(vector_colm)

    return tuple(vector)


def main():
    matriz_1 = ([1, 2], [3, 4], [5, 6])
    matriz_2 = ([-1, 0], [0, 1], [1, 1])
    multiplicar(matriz_1, matriz_2)
    print(multiplicar(matriz_1, matriz_2))



if __name__== "__main__":
    main()