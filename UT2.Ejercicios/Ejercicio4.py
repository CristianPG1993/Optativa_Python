# Escribe un programa que pida una nota (0-10) y muestre:
#
# "Suspenso" si es menor de 5
# "Aprobado" si es entre 5 y 6
# "Notable" si es entre 7 y 8
# "Sobresaliente" si es 9 o 10


nota = int(input("Introduce la nota (0-10): "))

if 0 <= nota < 5:
    print("Suspenso.")
elif 5 <= nota <= 6:
    print("Aprobado.")
elif 7 <= nota <= 8:
    print("Notable.")
elif 9 <= nota <=10:
    print("Sobresaliente")
else:
    print("No has introducido una nota válida.")
