# Ejercicio 1 - Capitales y países¶
# Escribe un programa que almacene en un diccionario las capitales de varios países,
# se introducirán los datos con la forma PAIS-CAPITAL. Esto debe ejecutarse indefinidamente
# hasta que el usuario introduzca "FIN INSERCIONES". El programa debe permitir al usuario
# consultar la capital de un país introduciendo su nombre. Si el país no está en el diccionario,
# el programa debe informar al usuario.


paises = {}
entrada = input("Indica un valor de la forma 'Pais-Capital' o escribe FIN INSERCIONES para salir: \n").lower()

while entrada != "fin insercciones":
    pais = entrada.split("-")[0]
    capital = entrada.split("-")[1]
    paises[pais] = capital
    entrada = input("Indica un valor de la forma 'Pais-Capital' o escribe FIN INSERCIONES para salir\n ").lower()

pais_usuario = input("Introduce el nombre del Pais:".lower())

if pais_usuario in paises:
    print(f"La capital de {pais_usuario.capitalize()} es {paises[pais_usuario].capitalize()}")

