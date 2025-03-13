#1️⃣ Generador de nombres de usuario
#Pide al usuario su nombre y apellido.
#Genera un nombre de usuario en minúsculas, sin espacios.
#Añade un número aleatorio al final.
#Muestra el nombre de usuario generado.
import random

print("\n 1️⃣ Generador de nombres de usuario")
print("Bienvenido al creador de nombres de Usuario")
nombre = input("Introduce el nombre: ")
apellido = input("Introduce el apellido: ")

nombre_usuario = (nombre +apellido).lower()
num = random.randint(0,9)

usuario_final = f"{nombre_usuario}{num}"


print(f"Tu nombre de usuario es: {usuario_final}")


#2️⃣ Analizador de frases
#Pide al usuario que ingrese una frase.
#Muestra la cantidad de caracteres de la frase.
#Indica si la frase contiene la palabra "Python".
#Convierte la frase a mayúsculas.
#Muestra la frase invertida.

print("\n 2️⃣ Analizador de frases ")
frase = input("Introduce una frase: ")

print(f"La frase tiene {len(frase)} caracteres.")
print("¿Contiene Python?", "Python" in frase)
print("Frase en mayúsculas: ", frase.upper())
print("Frase invertida: ", frase[::-1])

