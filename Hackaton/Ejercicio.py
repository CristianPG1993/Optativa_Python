palabras = input("introduce una palabra: ")


for i in range(len(palabras)-1, -1, -1):
    if palabras[i].lower() in ('a', 'e', 'i', 'o', 'u'):
        print("*", end= "")
    else:
        print(palabras[i], end="")
print()