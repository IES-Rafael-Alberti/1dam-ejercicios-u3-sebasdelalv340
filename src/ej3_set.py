"""Ejercicio 3.3.3
El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

Por ejemplo, el conjunto potencia de {1,2,3} es:

{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

>>> conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]
"""


def pedir_conjunto(conjunto_potencia: set) -> set:
    
    for i in range(3):
        valor = int(input("Introduce un valor: "))
        conjunto_potencia.add(valor)
    
    return conjunto_potencia


def main():
     conjunto_potencia = set()
     print(pedir_conjunto(conjunto_potencia))
   


if __name__ == "__main__":
    main()