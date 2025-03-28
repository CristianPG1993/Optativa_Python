#Ejercicio 1: Operaciones numéricas complejas
#Defina cinco variables numéricas distintas(int, float, complex) y
#realiza diversas operaciones matemáticas(potenciación, división entera, módulo)
#Imprime los resultados formateados en una cadena clara y descriptiva

#num1, num2, num3, num4, num5 = 10, 3, 2.5, 7.2, 4+2j


#resultado = (f"Potencia: {num1 ** num2}, División entera: {num1 // num2},"
#            f"Módulo: {num1 % num2}, Multiplicación: {num3 * num4}, Complejo: {num5}")

#print(resultado)


#Ejercicio 2: Combinación de cadenas y números
#Define dos variables numéricas (int, float) y tres cadenas diferentes.
#Genera una nueva cadena combinando texto con el resultado de operaciones aritméticas entre estas variables.
#Usa conversión explícita (str()) para insertar valores numéricos en la cadena final.


#num_int, num_float = 8, 3.5

#cadena1, cadena2, cadena3 = "Resultado: ", "La suma es ", " y la división es "

#resultado = cadena1 +  cadena2  + str(num_int + num_float) +  cadena3  + str(num_int/num_float)

#print(resultado)

#Ejercicio 3: Manipulación avanzada de cadenas
#Crea una cadena larga que contenga espacios en blanco al inicio, final, y en medio.
#Realiza varias operaciones encadenadas como eliminar espacios extremos, convertir
# a mayúsculas, y dividir la cadena en varias subcadenas usando un separador específico.



#cadena = "   Esto es una cadena   para manipular   "
#nueva_cadena = cadena.strip().upper().split()

#print(nueva_cadena)


#Ejercicio 4: Índices y subcadenas
#Define una cadena extensa (mínimo 50 caracteres).
#Obtén varias subcadenas usando la indexación por rangos (slicing)
# y genera una nueva cadena combinando estas subcadenas en orden inverso.
# Imprime la nueva cadena resultante.


#cadena_extensa = "Esto es una cada de más de 50 caracteres para aprender sobre python"
#subcadena = cadena_extensa[0:6] + "" + cadena_extensa[11:20]
#resultado = subcadena [::-1]

#print(resultado)

#Ejercicio 5: Formato y conversión numérica
#Define variables numéricas (entero, flotante, complejo).
# Crea una cadena con formato avanzado (f-strings) que muestre estos números
# con precisión definida (dos decimales, notación científica, etc.).
# Evita concatenar directamente números y texto.

# entero, flotante, complejo = 12, 3234.54535234, 5+3j
# formato = (f"Entero: {entero}, Flotante: {flotante:.2f}, "
#            f"Notación científica: {flotante:.2e}, Complejo: {complejo}")
#
# print(formato)

#Ejercicio 6: Operaciones combinadas entre números y cadenas
#Define dos variables numéricas enteras y dos cadenas.
# Realiza cálculos matemáticos diversos y genera una cadena formateada
# que explique cada operación (sumas, restas, multiplicaciones, módulo)
# claramente utilizando métodos de cadenas.

# num_a, num_b = 15, 4
# cad_a, cad_b = "La multiplicación es: ", " y el resto es: "
# resultado = f"{cad_a}{num_a * num_b}{cad_b}{num_a % num_b}"
#
# print(resultado)

#Ejercicio 7: Cálculo del área y perímetro
# Define variables numéricas que representen dimensiones (largo, ancho, radio, altura).
# Calcula el área y perímetro de distintas figuras geométricas (rectángulo, círculo, triángulo rectángulo)
# y presenta todos los resultados claramente en una sola cadena formateada usando conversiones explícitas.

# largo, ancho, radio, altura = 34, 10, 5, 34
#
# area_rectangulo = largo * ancho
# perimetro_rectangulo = 2*(largo + ancho)
# area_circulo = 3.14 * radio ** 2
# perimetro_ciruclo = 2*3.14*radio
# area_triangulo = (largo*altura)/2
# resultado = (f"Area de un rectángulo: {area_rectangulo}, "
#              f"Perimetro del rectangulo: {perimetro_rectangulo},"
#              f"\nArea del Circulo: {area_circulo}, Perimetro del Circulo: {perimetro_ciruclo},"
#              f"\nArea del triangulo: {area_triangulo}")
#
# print(resultado)


#Ejercicio 8: Análisis de texto complejo
# Define una cadena extensa que represente un párrafo completo.
# Utilizando únicamente métodos de cadenas y funciones integradas (len, upper, split),
# obtén el número total de caracteres, palabras y el resultado de transformar el texto
# completamente a mayúsculas, presentándolo claramente en una cadena nueva.



# cadena = "Soy una cadena extensa a la que le quieren cambiar el formato "
# caracteres = len(cadena)
# palabras = len(cadena.split())
# mayusculas = cadena.upper()
#
# resultado = (f"Número de caracteres: {caracteres}, Número de palabras: {palabras},"
#              f"\nParrafo en mayúsculas: {mayusculas}")
#
# print(resultado)



