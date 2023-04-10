#Polimorfismo es como sobreescribir los metodos bajo un mismo nombre pero que pueden funcionar diferente

class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre
        
    def moverse(self):
        print('Ando caminando')
        
class Atleta(Persona):
    
    def moverse(self):
        print('Ando Corriendo')
        
class Ciclista(Persona):
    
    def moverse(self):
        print('Ando moviendome en mi bicicleta')