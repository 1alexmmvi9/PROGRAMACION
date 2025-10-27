import json

archivo = open("despues.json",'r')

contenido = json.load(archivo)

for line in contenido:
    print("########## ARTIICULO ##########")
    print(line['titulo'])
    print(line['fecha'])
    print(line['autor'])
    print(line['contenido'])
    print("###############################")
    