"""Ejercicio 3.3.4
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
"""


def mostrar_comunes(set_frutas1: set, set_frutas2: set) -> set:
    frustas_comunes = set_frutas1 & set_frutas2
    return print("Las frutas comunes son: " + ", ".join(frustas_comunes))


def mostrar_unicos1(set_frutas1: set, set_frutas2: set) -> set:
    frustas_solo_en_frutas1 = set_frutas1 - set_frutas2
    return print("Las frutas únicas en frutas1 son: " + ", ".join(frustas_solo_en_frutas1))


def mostrar_unicos2(set_frutas1: set, set_frutas2: set) -> set:
    frustas_solo_en_frutas2 = set_frutas2 - set_frutas1
    return print("Las frutas únicas en frutas2 son: " + ", ".join(frustas_solo_en_frutas2))


def main():
    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}

    mostrar_comunes(set_frutas1, set_frutas2)
    mostrar_unicos1(set_frutas1, set_frutas2)
    mostrar_unicos2(set_frutas1, set_frutas2)

if __name__ == "__main__":
    main()