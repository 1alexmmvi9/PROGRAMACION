class Gato():
    def __init__(self,nombre,edad,raza):
        self.edad = edad
        self.nombre = nombre
        self.raza = raza

    def maulla(self):
        return "El gato está maullando"
    
gato1 = Gato(6,Garfield,típico)
