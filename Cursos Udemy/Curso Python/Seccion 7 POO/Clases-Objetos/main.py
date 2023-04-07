from persona import Persona

persona1 = Persona()
persona1.nombre = 'Juan'
persona1.edad = 17

persona2 = Persona()
persona2.nombre = 'David'
persona2.edad = 40

persona2.mostrar_datos()
print('='*25)
persona1.mostrar_datos()