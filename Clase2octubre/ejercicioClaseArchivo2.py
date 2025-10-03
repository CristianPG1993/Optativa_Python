'''
Vamos a realizar un programa que lea el archivo sistema_log_extenso
y copie en otro archivo errores.txt imprima todos los mensajes del tipo ERR
'''

log = open('sistema_log_extenso.txt', 'r') #Referencia al archivo

log_errores = open('usuario.txt', 'w')


log_data = log.readlines()


for line in log_data:
    if "Usuario" in line.split():
        log_errores.write(line)


