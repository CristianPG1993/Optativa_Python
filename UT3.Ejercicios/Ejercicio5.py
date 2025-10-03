# Ejercicio 5 - Biblioteca digital¶
# Escribe un programa que gestione una biblioteca digital utilizando un diccionario.
# El programa debe permitir al usuario añadir libros con su título, autor y año de publicación.
# El usuario debe poder consultar los libros por autor o por año de publicación.
# El programa debe ejecutarse indefinidamente hasta que el usuario introduzca "SALIR".

libros = {}

entrada = input("Introduce el título del libro, autor y año de publicación separados por comas(titulo,autor,año) o escribe salir: \n").lower()

while entrada != "salir":
    titulo = entrada.split(",")[0]
    autor = entrada.split(",")[1]
    anio_publicacion = entrada.split(",")[2]
    libros[titulo] = (autor, anio_publicacion)
    entrada = input("Introduce el título del libro, autor y año de publicación separados por comas(titulo,autor,año) o escribe salir: ").lower()



consulta = input("Indique si desea consultar por autor o por año: ").lower()

if consulta == "autor":
    autor = input("Introduce el nombre del autor: ")
    if autor in libros:
        print(f"Los libros escritos por {autor} son: {libros[titulo]}")
elif consulta == "año":
    anio = int(input("Introduce el año de publicación:" ))
    if anio in libros:
        print(f"Los libros publicados en {anio} son: {libros[titulo]}")


