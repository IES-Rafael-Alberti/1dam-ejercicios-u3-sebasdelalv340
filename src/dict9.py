"""Ejercicio 3.2.9
Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""


def mostrar_menu():
    print("\nMenú:")
    print("1. Añadir factura")
    print("2. Pagar factura")
    print("3. Terminar")


def agregar_factura(diccionario_factura: dict) ->dict:
    clave = int(input("Introduce el número de factura: "))
    valor = float(input("Introduce el coste de la factura: "))

    diccionario_factura[clave] = valor
    return diccionario_factura


def pagar_factura(diccionario_factura: dict, cantidad_cobrada: int) -> dict:
    clave = int(input("Introduce el número de factura: "))
    if clave in diccionario_factura.keys():
        cantidad_cobrada += int(diccionario_factura.pop(clave))

    return cantidad_cobrada


def mostrar_pendiente(diccionario_factura: dict) ->int:
    cantidad_pendiente = 0
    for valor in diccionario_factura.values():
        cantidad_pendiente += int(valor)
    
    return cantidad_pendiente

def main():
    diccionario_factura = {} 
    cantidad_cobrada = 0
    cantidad_pendiente = 0

    n = True
    while n:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_factura(diccionario_factura)
            cantidad_pendiente = mostrar_pendiente(diccionario_factura)
            print(f"Cantidad cobrada: {cantidad_cobrada}")
            print(f"Cantidad pendiente: {cantidad_pendiente}")           
        elif opcion == '2':
            cantidad_cobrada = pagar_factura(diccionario_factura, cantidad_cobrada)
            print(f"Cantidad cobrada: {cantidad_cobrada}")
            cantidad_pendiente = mostrar_pendiente(diccionario_factura)
            print(f"Cantidad pendiente: {cantidad_pendiente}")
        elif opcion == '3':
            print("Programa terminado.")
            n = False
        else:
            print("Opción no válida")
    
    print(diccionario_factura)


if __name__ == "__main__":
    main()