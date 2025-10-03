# Ejercicio 3 - Inventario de productos¶
# Escribe un programa que gestione un inventario de productos utilizando un diccionario.
# El programa debe permitir al usuario añadir productos con su nombre y cantidad, eliminar productos,
# y consultar la cantidad de un producto específico. El programa debe ejecutarse indefinidamente hasta
# que el usuario introduzca "SALIR".

inventario = {}

opcion = -1

while opcion != 4:
    print("Escoge una opción: ")
    print("1. Añadir un producto")
    print("2. Eliminar producto")
    print("3. Consultar precio")
    print("4. Salir")
    opcion = int(input("Introduce una opcion:"))

    if opcion == 1:
        nombre = input("introduce un producto:")
        cantidad = input("Introduce una cantidad:")
        inventario[nombre] = cantidad
    if opcion == 2:
        producto_eliminado  = input("Introduce el nombre del producto: ")

        if producto_eliminado in inventario:
            del inventario[producto_eliminado]
            print(f"Producto {producto_eliminado} eliminado del inventario.")
        else:
            print(f"No existe el producto {producto_eliminado} en el inventario.")
    if opcion == 3:
        nombre = input("Introduce el nombre a consultar: ")
        if nombre in inventario:
            print(f"El producto {nombre} tiene una cantidad de {inventario[nombre]} unidades")
        else:
            print(f"No existe el producto {nombre} en el inventario.")

    elif opcion > 4 or opcion > 1:
        print(f"La opcion {opcion} no existe en la lista de comandos")

print("Saliendo...")




