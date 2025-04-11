# Ejercicio 5¶
# Escribe un programa que pida el nombre de un día de la semana
# y muestre si es "laborable" o "fin de semana".

dia = input("Escribe el nombre de un día de la semana: ").lower()

laborable = {"lunes", "martes", "miércoles", "jueves", "viernes"}

if dia in laborable:
    print(f"El {dia.capitalize()} es laborable.")
else:
    print(f"El {dia.capitalize()} es fin de semana. ")