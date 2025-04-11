# Ejercicio 5 - Puede entrar en el servidor de Discord?¶
# Escribe un programa que pida un rol y una academia de estudios,
# si el rol es "alumno" y la academia es "Prometeo" el programa
# debe darle acceso al servidor de Discord oficial y al de los alumnos,
# donde se critica a los profes. Si el rol es "profesor" y la academia es "Prometeo"
# el programa debe darle acceso al servidor de Discord oficial, pero no al de los alumnos.
# En cualquier otro caso, el programa debe imprimir "No tienes acceso al servidor de Discord".

academia = input("Introduce el nombre de tu academia: ").lower()
rol = input("Introduce tu rol de usuario(alumno o profesor):").lower()


if academia == "prometeo" and rol == "alumno":
    print("Tienes acceso al discord oficial y al discord de los alumnos.")
elif academia == "prometeo" and rol == "profesor":
    print("Tienes acceso al discord oficial.")
else:
    print("No tienes acceso al servidor de discord.")

