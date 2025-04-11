# Ejercicio 2. Escribe un programa que simule el trabajo de un portero de discoteca.
# El programa debe pedir al usuario su edad y determinar si puede entrar o no.
# Si la edad es menor de 18 años, el programa debe imprimir "No puedes entrar".
# Si la edad es mayor o igual a 18 años, el programa debe imprimir "Puedes entrar".

edad = int(input("Introduce tu edad: "))

if (edad >= 18) and (edad <= 60):
    print("Puedes entrar")
elif edad > 60 :
    print("No puedes entrar. Eres muy mayor")
elif (edad >= 0) and (edad < 18):
    print("Eres muy pequeño.")