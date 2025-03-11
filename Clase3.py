#1. Longitud de una cadena

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