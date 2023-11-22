"""Ejercicio 3.2.8
Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""


def crear_diccionario(diccionario) -> dict:
    return dict((palabra.split(":")) for palabra in diccionario.split(","))


def traducir_frase(diccionario: dict, frase: str) -> str:
    lista_a_traducir = frase.split(" ")
    traduccion = []
    for palabra in lista_a_traducir:   
        traduccion.append(diccionario.get(palabra, palabra))

    traduccion = " ".join(traduccion)

    return print(traduccion)
    
    
def main():
    diccionario = input("Introduce palabras con su traducción con el formato <palabra>:<traducción> y cada par de palabras separadas por comas: ")
    diccionario = crear_diccionario(diccionario)
    frase = input("Introduce una frase a traducir: ")
    traducir_frase(diccionario, frase)
    

if __name__ == "__main__":
    main()