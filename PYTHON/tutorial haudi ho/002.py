'''
    En primer lugar quiro explicar de que se va a tratar el programa que voy a hacer ahora mismo.
    Este programa genrara un numero de 1 al 10, y despues preguntara al jugador un numero , y el jugador tendra que adivinar este numero.
    Y finalemtne el programa tndra que comparar el numero random y el nuemro que ha dicho el jugador. 
'''
import random # Se importa el randomaizer

# Aqui basicamente he creado la variable de un numero random
random_number = random.randint(1,3)

# Aqui he creo la variable con el numer oque nos dira el jugador
user_number = int(input("Introduce un numero, a ver si lo adivinas:"))

# Aqui esta ya propuesta la logica del juego este de randon sitios
if user_number == random_number:
    print("HAS GANADO")
else:
    print("HAS PERDIDO")
    print("El numero randomera: ",random_number)

if user2_number == random2_number: 
    random2_number = random.randint(1,3)

    user2_number = int(input("Introduce el segundo numero, a ver si adivinas este tambien:"))

    if random2_number == user2_number:
        print("Has podido ganar y en la segunda partida tambien")
    else:
        print("Perdiste pero al menos ganaste la primera vez")