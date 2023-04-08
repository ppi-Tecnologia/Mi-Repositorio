from persona import Persona

#creando un  objeto, nombre = Juan, edad = 17
persona1 = Persona('Juan', 17)
#Cambiando el nombre a Castrillon
persona1.set_nombre('Castrillon')
#Cambiando edad a 18
persona1.set_edad(18)
# imprimiendo la variable nombre del objeto persona1
print(persona1.get_nombre())
print(persona1)
