class Persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def detalle_persona(self):
        print(f'Nombre: {self.nombre} \nEdad: {self.edad}')
        
    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}' 
    
#Creando una clase Cliente que era los metodos y el constructor de la clase Persona 
class Cliente(Persona):
    pass

#Clase Empleado que era de la clase Persona
class Empleado(Persona):    
    
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    def detalle_empleador(self):
        super().detalle_persona(    )
        print(f'Sueldo: {self.sueldo}')
    
    def __str__(self):
        return super().__str__() + f'\nSueldo: {self.sueldo}'