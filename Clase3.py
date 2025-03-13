#1. Longitud de una cadena
from mpmath.libmp import sqrt_fixed

nombre = "Cristian Paños"

print("\nLongitud del nombre:", len(nombre))
print(f"\n{nombre} tiene {len(nombre)} caracteres.")



#2. Convertir texto a mayúsculas y minúsculas

#Upper
print("Mi nombre utilizando upper: ", nombre.upper())

#lower
print("Mi nombre utilizando lower: ", nombre.lower())

#3. Slicing

print("Primeros 3 caracteres: ", nombre[:3])
print("Últimos  4 caracteres: ", nombre[-4:])
print()


#4. Reemplazar palabras en una cadena

frase = "Me gusta Java"
print("Cambio la palabra: ", frase.replace("Java","Python"))
print(frase)


#5. Verificar si una cadena existe en otra

print("\nPython" in frase )

nueva_frase = "Me gusta Python"
print("\nPython" in nueva_frase)

#6. unir variables en una cadena

palabras = ["Hola", "Mundo", "en", "Python"]

print("\nFrase completa con join: "," " .join(palabras))

#7. Split

oracion = "Python es divertido"

palabritas = oracion.split()

print("Listas de palabras de mi grupo: ", palabritas)

#8. Redondear un número decimal

numero = 3.141516

print("Mi número redondeado es: ", round(numero,2))

#9. Formateo de número decimales

precio = 19.99
print("Precio con dos decimales: {:.4f}".format(precio))
print("Precio con dos decimales: {:.1f}".format(precio))
print("Precio con dos decimales: {:.0f}".format(precio))

#10. Obtener el valor ASCII de un carácter

print("Esto es el código ASCII de 'A': ", ord('A'))
print("Esto es el código ASCII de 'a': ", ord('a'))

#11. Elevar al  cuadrado

numero_cuadrado = 5
print("5 al cuadrado es: ", numero_cuadrado ** 2)


#12. Raíz cuadrada

print("La raíz cuadrada de 25 es: ", 25 ** 0.5)

import math
numerito = 100
raiz = math.sqrt(numerito)

print("Raiz cuadrada de 100: ", raiz)

#13. Divisiones enteras y resto

print("Division: ", 10/3)
print("Division entera: ", 10//3)
print("Resto: ", 10%3)


#14. Generar un número aleatorio

import random

print("Numero aleatorio entre 1 y 10: ", random.randint(1,10))

#15. Convertir numeros a cadenas y viceversa

numerajo = 300
texto = str(numerajo)

print("Convertido a texto, soy: ", texto)


cadena = "200"

numerajo = int(cadena)
print("Convertido a numero soy:", numerajo)
##print(numerajo + texto)

#16. Redondear hacia arriba

print("Redondeo hacia arriba del numero 3.6: ", math.ceil(3.6))
print("Redondeo hacia abajo del numero 3.2: ", math.floor(3.2))
print("Redondeo hacia arriba del numero 3.2: ", math.ceil(3.2))

#17. Convertir una lista en un conjunto(eliminar duplicado)

numeroides = [1,2,3,4,5,5,5,5]
sin_duplicados = set(numeroides)

print("Numeroides sin duplicar: ", sin_duplicados)

#18. Repetir una cadena

print("Money!" * 3)

#19. Tipo de dato

dato = 3.14
print("El tipo de dato es: ", type(dato))

#20. Combinar cadenas y cariables en un print

print(f"El {dato} es de tipo {type(dato)}")
