class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def detalle_persona(self):
        print(f'Nombre: {self.nombre} \nEdad: {self.edad}')
        
    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'
    
class Cliente(Persona):
    pass