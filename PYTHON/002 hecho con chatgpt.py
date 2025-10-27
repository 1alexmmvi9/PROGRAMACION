import random

# Primera ronda: de 1 a 2
random_number = random.randint(1, 2)
user_number = int(input("Introduce un número del 1 al 2: "))

if user_number == random_number:
    print("HAS GANADO la primera partida 🎉")

    # Segunda ronda: de 1 a 3
    random2_number = random.randint(1, 3)
    user2_number = int(input("Introduce un número del 1 al 3: "))

    if user2_number == random2_number:
        print("¡Has ganado también la segunda partida! 🏆")
    else:
        print("Perdiste la segunda, pero ganaste la primera 😉")
        print("El número era:", random2_number)

else:
    print("HAS PERDIDO 😢")
    print("El número era:", random_number)