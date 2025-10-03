# Ejercicio 1 - Contador¶
# Escribe un programa que pida al usuario un número entero positivo e
# imprima los números desde el 0 hasta ese número (incluido).
# El programa debe imprimir los números en cada iteración.

# numero = int(input("Introduce un numero positivo: "))
#
# for i in range(0,numero+1):
#     print(i)


# Ejercicio 2 - Contador de números pares¶
# Escribe un programa que pida al usuario un número entero positivo y
# cuente cuántos números pares hay desde 0 hasta ese número (incluido). El programa debe imprimir el resultado.

# numero = int(input("introduce un numero positivo: "))
# pares = 0
#
# for  i in range(0,numero+1):
#     if (i % 2 == 0):
#         pares = pares + 1
#         print(i)
#
# print(f"Numero de pares: {pares}")

# Ejercicio 3 - Cuenta atrás¶
# Escribe un programa que pida al usuario un número entero positivo y realice una cuenta atrás desde ese número
# hasta 0. El programa debe imprimir cada número en la cuenta atrás.

# numero = int(input("Introduce un numero positivo: "))
#
# for i in range(numero,-1, -1):
#     print(f"Numero: {i}")

# Ejercicio 4 - Factorial¶
# Escribe un programa que pida al usuario un número entero positivo y calcule su factorial. El programa debe imprimir
# el resultado. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.

# numero = int(input("Introduce un numero positivo: "))
# factorial = 1
#
# for i in range(1,numero+1):
#     factorial *= i
#
#
# print(f"El factorial de {numero} es: {factorial}")

# Ejercicio 5 - Múltiple de 3 o 5¶
# Escribe un programa que pida al usuario un número entero positivo e imprima solamente los
# números múltiplos de 3 o de 5 dentro de ese rango.
#
# Si el número es múltiplo de 3, imprime el número seguido de el mensaje "es múltiplo de 3".
# Si el número es múltiplo de 5, imprime el número seguido del mensaje "es múltiplo de 5".
# Si el número es múltiplo de ambos no debes imprimir nada.

# numero = int(input("Introduce un numero positivo: "))
#
# for i in range(0, numero+1):
#     if i % 5 == 0 and i % 3 == 0:
#         continue
#     elif i % 5 == 0:
#         print(f"Numero {i}: es múltiplo de 5")
#     elif i % 3 == 0:
#         print(f"Numero {i}: es múltiplo de 3")
#
#     else:
#         print(f"Numero {i}: no es múltiplo de ninguno")

# Ejercicio 6 - Triángulo de asteriscos¶
# Escribe un programa que pida al usuario un número entero positivo y dibuje un triángulo de asteriscos con
# la altura especificada. Por ejemplo, si el usuario ingresa 5, el triángulo debe verse así:
# *
# **
# ***
# ****
# *****
#
# numero = int(input("Introduce un numero positivo: "))
#
# for i in range(1, numero+1):
#
#     print("*"*i)

# Ejercicio 7 - Tabla de multiplicar¶
# Escribe un programa que pida al usuario un número entero positivo y
# muestre la tabla de multiplicar de ese número. Por ejemplo, si el usuario ingresa 3, el programa debe imprimir:

numero = int(input("Introduce un numero positivo: "))

for i in range(1, 11):

    print(f"{numero} X {i} = {numero*i}")

# Ejercicio 8 - Cuadrado con cruz¶
# Escribe un programa que pida al usuario un número entero positivo impar y dibuje un cuadrado de x con una cruz
# en el medio. Por ejemplo, si el usuario ingresa 5, el cuadrado debe verse así:
# xxxxx
# xx xx
# x x x
# xx xx
# xxxxx

# numero = int(input("Introduce un numero positivo impar: "))
#
# for i in range(numero):
#     for j in range(numero):
#
#         if i == 0 or i == numero:
#             print("x"*numero)
#             break









