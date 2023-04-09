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
        #super es para heredar los atributos del metodo nombrado
        #super().__init__(nombre, edad)
        Persona.__init__(self, edad, nombre)
        self.sueldo = sueldo
        
    def detalle_empleador(self):
        #super().detalle_persona(    )
        Persona.detalle_persona(self)
        print(f'Sueldo: {self.sueldo}')
    
    def __str__(self):
        #super().__str__() + f'\nSueldo: {self.sueldo}'
        return Persona.__str__(self) + f'\nSueldo: {self.sueldo}'