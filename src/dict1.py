"""Ejercicio 3.2.1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""


def preguntar_divisa():
    return input("Introduce una divisa: ")


def comprobar_divisa(diccionario):
    divisa = preguntar_divisa()       
    if divisa not in diccionario:
        print(f"La divisa {divisa} no está en el diccionario.")
    else:
        print(f"Su símbolo es {diccionario[divisa]}")

def main():
    diccionario = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
    
    print(comprobar_divisa(diccionario))


if __name__ == "__main__":
    main()