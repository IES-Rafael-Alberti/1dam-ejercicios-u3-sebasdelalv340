"""Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)

Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.
"""

def cuenta(palabra, busqueda):
    cont = 0
    for letra in palabra:
        if letra == busqueda:
            cont += 1

    return cont


def main():
    try:
        palabra = input("Introduce una palabra: ")
        busqueda = input("¿Qué letra quiere contar?: ")
        print(cuenta(palabra, busqueda))
    except Exception:
        print("La entrada es incorrecta")

if __name__ == "__main__":
    main()