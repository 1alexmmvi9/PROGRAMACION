import random 
# La piedra y las tijeras serian dos numeros, y el pael un simbolo

player = input("Elige (2 = piedra, 1 = tijeras, a = papel): ")

options = ['1','2','a']
computer = random.choice(options)

print("El ordenador eligió: ",computer)

# Asi es como se elige al ganador
if player == computer:
    print("Empate")
# Par 1
elif player == '2' and computer == '1': 
    print("Has ganado, piedra rompe a las tijeras")
elif player == '1' and computer == '2': 
    print("Has perdido, piedra rompe a las tijeras!!!")
# Par 2
elif player == 'a' and computer == '2': 
    print("Has ganado, porque papel tapa a la piedra ")
elif player == '2' and computer == 'a': 
    print("Has perdido, porque el maldito papel tapa a la piedra!!!")
# Par 3
elif player == '1' and computer == 'a': 
    print("Has ganado, porque las tijeras cortan el papel")
elif player == 'a' and computer == '1': 
    print("Has perdido, cuantas veces hay que explicarte uqe las tijeras cortan papel!!!")

else: print("No sabes jugar o que?")
