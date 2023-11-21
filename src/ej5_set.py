"""Ejercicio 3.3.5
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""


def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    numeros_pares = set()
    numeros_multiplos_de_tres = set()

    for numero in numeros:
        if numero%2 == 0:
            numeros_pares.add(numero)
            if numero%3 == 0:
                numeros_multiplos_de_tres.add(numero)
        elif numero%3 == 0:
            numeros_multiplos_de_tres.add(numero)

    print(numeros_pares)
    print(numeros_multiplos_de_tres)
    pares_y_multiplos_de_tres = numeros_pares & numeros_multiplos_de_tres
    print(pares_y_multiplos_de_tres)
    

if __name__ == "__main__":
    main()