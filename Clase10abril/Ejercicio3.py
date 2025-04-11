

# Ejercicio 3 - Pacman¶
# Escribe un programa que pida al usuario dos números enteros correspondientes
# a la casilla que está Pacman (1er número) y a la que está un fantasma (2o número),
# luego debe recibir un texto con el formato "normal" o "caramelo".
# Si el texto es "normal" y los números son iguales,
# el programa debe imprimir "Pacman ha sido atrapado".
# Si el texto es "caramelo" y los números son iguales, el programa debe imprimir "Pacman ha comido al fantasma".
# En cualquier otro caso, el programa debe imprimir "Pacman ha escapado".

posicion_pacman = int(input("Introduce un número para pacman: "))
posicion_fantasma = int(input("Introduce un número para fantasma:"))



if posicion_pacman == posicion_fantasma:

    estado_pacman = input("Como está pacman?")

    if estado_pacman == "caramelo":
        print("Pacman ha comido al fantasma.")
    elif estado_pacman == "invisible":
        print("Pacman ha escapado.")
    else:
        print("Pacman atrapado.")

else:
    print("Pacman ha escapado.")