lista_peliculas = list()

opcion = input("introduce una pelicula ('fin' para acabar):\n")

while opcion != "fin":
    lista_peliculas.append(opcion)
    opcion = input("introduce otra pelicula ('fin' para acabar):\n")
print(f"número total de peliculas: {len(lista_peliculas)}")
print(f"La primera película es: {lista_peliculas[0]}")
print(f"La última película es: {lista_peliculas[-1]}")
print(f"Número total de películas sin repetir: {set(lista_peliculas)}")