# Non Playable Character

class Npc():
  def __init__(self,x,y):
    self.posx = x
    self.posy = y
    
personajes = []
numeropersonajes = 50

for i in range(0,numeropersonajes):
	personajes.append(Npc(4,3))

print(personajes)