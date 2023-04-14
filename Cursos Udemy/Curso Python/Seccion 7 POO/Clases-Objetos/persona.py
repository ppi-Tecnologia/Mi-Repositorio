
class Persona:
    #nombre = None
    #edad = None
    
    #self siempre debe ir como parametro y al referirnos a una variable del metodo
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print('Nombre:', self.nombre)
        print('Edad:', self.edad)
        
    #Este metodo __str__ lo que hace es un metodo como si fuera mostrar datos
    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'
        
