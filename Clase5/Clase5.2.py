# Crea un diccionario
persona = {
    "nombre" : "Mario",
    "edad" : 32,
    "registrado" : True
}

print(persona)

#Accédeme a un valor por su clave
print(persona["edad"], persona["registrado"])

#Añadir una nueva clave-valor
persona["ciudad"] = "Burgos"
persona["Numero de hijos"] = 3
print(persona)

#Cambiar el valor de una clave
persona["ciudad"] = "Albacete"
persona["Numero de hijos"] = 7
print(persona)

#Eliminar una clave
# del persona["registrado"]
# print(persona)

#Comprobar si una clave ya existe
existe_nombre_DAM = "nombre" in persona
existe_mario = "Mario" in persona["nombre"]
print(existe_nombre_DAM)
print(existe_mario)

#Compara dos valores booleanos
es_menor_y_registrado = persona["edad"] > 18 and persona["registrado"]
booleano_convertido = int(es_menor_y_registrado)

print(es_menor_y_registrado)
print(booleano_convertido)

#Usar NOT con un booleano
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#Creame un conjunto a partir de una lista de duplicados
numeritos = [1,2,3,5,6,2,5,3,5,8,9,4]

#convierto a conjunto. Porque así elimino duplicidades
conjuntito = set(numeritos)
print(conjuntito)

#Comparar si dos colecciones tienen los mismo elementos unicos
coleccion_a = set([1,2,2,3,6])
coleccion_b = set([3,2,1,6])

mismos_elementos = coleccion_a == coleccion_b
print(mismos_elementos)




