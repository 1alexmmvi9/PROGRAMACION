"""
    Adivina el número - Modo docente
    v1.0 - Alex Sytnyk
    Juego simple para practicar condicionales, bucles y validaciones.
"""

import random

# Generar número secreto
secreto = random.randint(1, 50)
intentos_restantes = 6

# Aserciones
assert 1 <= secreto <= 50
assert intentos_restantes >= 0

print("Bienvenido al juego 'Adivina el número'. Tienes 6 intentos.")

while intentos_restantes > 0:
    print("Intentos restantes:", intentos_restantes)
    entrada = input("Introduce un número entre 1 y 50: ")

    try:
        intento = int(entrada)
    except:
        print("Eso no es un número válido.")
        continue

    if intento < 1 or intento > 50:
        print("El número debe estar entre 1 y 50.")
        continue

    if intento < secreto:
        print("Demasiado bajo.")
    elif intento > secreto:
        print("Demasiado alto.")
    else:
        print("Has acertado el número secreto.")
        break

    if intentos_restantes == 4:
        if secreto % 2 == 0:
            print("Pista: el número secreto es par.")
        else:
            print("Pista: el número secreto es impar.")

    intentos_restantes -= 1
    assert intentos_restantes >= 0

if intentos_restantes == 0:
    print("No te quedan intentos. El número secreto era", secreto)
else:
    print("Ganaste con", intentos_restantes, "intentos restantes.")
