from setuptools.command.alias import alias

notas_alumnos = {
    "Kenneth" : [6.5, 8, 3],
    "Jorge" : [0, 10, 5],
    "Jose" : [7, 6, 10],
    "Heber" : [7, 8, 9],
    "Victor" : [7, 8, 9],
    "Ander" : [8, 8, 8]
}

def imprimir_menu():
    return("""Escoge una opción:
            1- Consultar media alumno
            2- Añadir nota a alumno
            3- Añadir alumno
            4- Eliminar nota de alumno
            5- Eliminar alumno
            6- Salir\n""")


def consultar_media(alumno):

    if alumno not in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} no existe en el sistema")

    if len(notas_alumnos[alumno]) == 0:
        raise ZeroDivisionError(f"El alumno {alumno} no tiene notas disponibles")

    notas = notas_alumnos[alumno]
    total = 0
    for nota in notas:
        total += nota
    return total/len(notas)


def añadir_nota_alumno(alumno, nota):
    if alumno not in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} no existe en el sistema")

    notas_alumnos[alumno].append(nota)


def añadir_alumno(alumno, notas):

    if alumno in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} ya existe en el sistema")

    notas_alumnos[alumno] = notas


def eliminar_nota_alumno(alumno, nota):
    if nota not in notas_alumnos[alumno]:
        raise ValueError(f"La nota {nota} no existe para {alumno}")

    notas_alumnos[alumno].remove(nota)


def mostrar_notas_alumno(alumno):
    if alumno not in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} no está en el sistema")

    return notas_alumnos[alumno]


def eliminar_alumno(alumno):
    if alumno not in notas_alumnos.keys():
        raise ValueError(f"El alumno {alumno} no está en el sistema")

    notas_alumnos.pop(alumno)


def main ():
    print("Bienvenidos al gestor de notas")


    opcion = input(imprimir_menu())

    while opcion != "6":
        match opcion:
            case "1":
                alumno = input("Que media quieres consultar?\n ")
                try:
                    print(f"La nota media de {alumno} es {consultar_media(alumno)}")
                except Exception as e:
                    print(e)

            case "2":
                try:
                    alumno = input("A que alumno quieres añadirle la nota?\n")
                    nota = float(input("Que nota quieres añadir?\n"))
                    añadir_nota_alumno(alumno,nota)
                except ValueError as e:
                    print(e)

            case "3":
                try:
                    notas = []
                    alumno = input("Nombre del alumno a añadir:\n")
                    añadir_notas = input("Quieres añadir notas del alumno?\n")
                    if añadir_notas.lower() == "si":
                        notas = [float(num) for num in input("Que notas tiene el alumno?\n").split()]

                    añadir_alumno(alumno, notas)
                except ValueError as e:
                    print(e)

            case "4":
                try:

                    alumno = input("Introduce el alumno del que quieres eliminar una nota:\n")
                    print(mostrar_notas_alumno(alumno))
                    nota = float(input("Que nota quieres eliminar?\n"))

                    eliminar_nota_alumno(alumno, nota)
                    print(f"Las notas del alumno ahora son {mostrar_notas_alumno(alumno)}")
                except ValueError as e:
                    print(e)

            case "5":
                try:

                    alumno = input("Introduce el alumno que quieres eliminar:\n")
                    eliminar_alumno(alumno)

                except Exception as e:
                    print(e)
            case _:
                print("El valor enviado debe de ser entre 1 y 6")
        opcion= input(imprimir_menu())
main()