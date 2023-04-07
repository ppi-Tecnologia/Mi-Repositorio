
class Persona:
    #nombre = None
    #edad = None
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    
    def mostrar_datos(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        
    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'
        
