"""Ejercicio 3.0.1
Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.
"""

def cadenaInversa(palabra: str):
    indice = -1
    cont = 0
    while cont < len(palabra):
        letra = palabra[indice]
        print(letra)
        indice -= 1
        cont += 1

    return ""

def main():
    try:
        palabra = input("Introduce una palabra: ")
        print(cadenaInversa(palabra))
    except Exception:
        print("La entrada es incorrecta.")
    
if __name__ == "__main__":
    main()



