def saludar():
    global nombre # Estoy volviendo global la variable nombre
    nombre = 'Juan Castrillon'
    edad = 25
    return 'Hola desde la funcion saludar', nombre, edad
    
valor = saludar()
saludo, nombre, edad = saludar()
print(valor)
print(saludo)
print(nombre, edad)
print(type(edad))

#print(f'Hola {nombre} desde fuera de la funcion saludar')