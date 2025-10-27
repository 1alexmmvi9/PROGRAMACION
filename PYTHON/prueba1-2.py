archivo = open("clientes.txt",'r')  # R = Read

contenido = archivo.readline()  # Tambien existe archivo.readlines()

print(contenido)

archivo.close