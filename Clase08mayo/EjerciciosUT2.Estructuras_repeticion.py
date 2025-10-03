# Ejercicio 9 - Suma acumulativa¶
# Escribe un programa que pida al usuario una serie de números enteros y calcule la suma acumulativa
# de esos números. El programa debe seguir pidiendo números hasta que el usuario ingrese un 0.
# Al final, imprime la suma total.

import random
from sys import hash_info



# suma = 0
# numero = int(input("Introduce un número: "))
#
#
# while numero != 0:
#     suma += numero
#     numero = int(input("Introduce un número (para salir pulse 0): "))
#
# print(f"El resultado total ha sido: {suma}")

# Ejercicio 10 - Akinator numérico¶
# Escribe un programa que escoja un número aleatorio entre 1 y 100 y le pida al usuario que adivine el número.
# El programa debe dar pistas al usuario si el número es mayor o menor que el número elegido.
# El programa debe seguir pidiendo números hasta que el usuario adivine el número correcto.

# numero_aleatorio = random.randint(1,100)
# numero_usuario = int(input("Introduce un número: "))
#
# while numero_usuario != numero_aleatorio:
#     if numero_usuario > numero_aleatorio:
#         print(f"El número {numero_usuario} es mayor.")
#
#     else:
#         print(f"El número {numero_usuario} es menor.")
#
#     numero_usuario = int(input("Introduce otro número: "))
#
# print("Has acertado el número!")

# Ejercicio 11 - Media de notas¶
# Escribe un programa que pida al usuario cuantas evaluaciones hay que cualificar.
# Seguidamente se recibirán ese número de series de notas (números decimales entre 0 y 10) y
# calcule la media de esas notas. El programa debe seguir pidiendo notas hasta que el usuario ingrese un -1.
# Al final, imprime la media.

# evaluaciones = (int(input("Introduce el número de evaluaciones: ")))
#
#
# for i in range(evaluaciones):
#
#     nota = float(input("Introduce la siguiente nota: "))
#     num_notas = 0
#     suma_notas = 0
#     while nota != -1:
#         num_notas += 1
#         suma_notas += nota
#         nota = float(input("Introduce la siguiente nota: "))
#     print(f"La media de la evaluación {i}: {suma_notas/num_notas}")

# Ejercicio 12 - Mayor y menor¶
# Escribe un programa que pida al usuario una serie de números enteros y determine cuál es el mayor y
# cuál es el menor. El programa debe seguir pidiendo números hasta que el usuario ingrese un 0.
# Al final, imprime el mayor y el menor.
#
# numero_usuario = int(input("Introduce un número entero: "))
# num_mayor = -hash_info.inf
# num_menor = hash_info.inf
#
# while numero_usuario != 0:
#     if numero_usuario > num_mayor:
#         num_mayor = numero_usuario
#     elif numero_usuario < num_menor:
#         num_menor = numero_usuario
#
#     numero_usuario = int(input("Introduce un número entero: "))
#
#
# print(f"El número mayor es {num_mayor} y el menor es {num_menor}.")

# Ejercicio 13 - Número de cifras¶
# Escribe un programa que pida al usuario una serie de números enteros positivos hasta la introducción de un valor
# -1 para cada número debe contar cuántas cifras tiene. El programa debe imprimir la longitud de cada número.
# No podéis usar la función len() para contar las cifras ni convertir el número a cadena.

# numero = int(input("Introduce un numero entero: "))
#
# while numero != -1:
#     cifras = 1
#     copia_num = numero
#     while numero > 9:
#         cifras += 1
#         numero //= 10
#     print(f"EL número de dígitos de {copia_num} es {cifras}.")
#     numero = int(input("Introduce un numero entero: "))
#
# # Ejercicio 14 - Números primos¶
# # Escribe un programa que pida al usuario un número entero positivo y determine si es primo o no.
# # Un número primo es aquel que solo es divisible por 1 y por sí mismo. El programa debe imprimir el resultad0.
#
# numero = int(input("Introduce un numero entero positivo: "))
#
# if numero % 1 == 0 and numero %


# Ejercicio 15 - Banca online¶
# Escribe un programa que simule una cuenta bancaria.
# El programa debe permitir al usuario realizar las siguientes operaciones:
#
# Ingresar dinero
# Retirar dinero
# Consultar saldo
# Salir
# Inicializa el saldo en 0 y permite al usuario realizar operaciones hasta que decida salir.

saldo = 0
opcion = -1
while opcion != 4:
    print("Escoge una opción: ")
    print("1. Ingresar dinero: ")
    print("2. Retirar dinero: ")
    print("3. Consultar dinero: ")
    print("4. Salir ")

    opcion = (int(input("Introduce un número(1-4):")))

    if opcion == 1:
        ingreso = int(input("Introduce el importe a ingresar:"))
        saldo += ingreso
    elif opcion == 2:
        retiro = int(input("Introduce el importe a retirar: "))

        saldo -= retiro
        print(f"El importe de tu cuenta es {saldo} €.")
    elif opcion == 3:
        print(f"El saldo de su cuenta es {saldo} €.")
    elif opcion == 4:
        print(f"Sesión cerrada.")











