"""Ejercicio 3.0.4
Hay un método de cadenas llamado count que es similar a find. Lee la documentación de este método en: * Métodos en ingles * Métodos en castellano

y escribe el código necesario para invocar a este método y contar el número de veces que una letra aparece en “banana”.
"""

def contar(palabra, letra):
    return palabra.count(letra)


def main():
    try:
        palabra = input("Introduce una palabra: ")
        letra = input("¿Qué letra quiere contar?: ")
        print(contar(palabra, letra))
    except Exception:
        print("La entrada es incorrecta.")


if __name__ == "__main__":
    main()