'''
Vamos a realizar un programa que lea el archivo sistema_log_extenso
e imprima por pantalla todos los mensajes del tipo ERR
'''


log = open('sistema_log_extenso.txt', 'r') #Referencia al archivo

log_data = log.readlines()


for line in log_data:
    if "ERROR" in line.split():
        print(line, end="")





