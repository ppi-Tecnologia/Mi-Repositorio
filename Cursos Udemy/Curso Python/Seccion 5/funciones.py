def saludar():
    global nombre
    nombre = 'Juan Castrillon'
    print("Hola desde la funcion saludar")
    print('Hola', nombre)
    
saludar()
print(f'Hola {nombre} desde fuera de la funcion saludar')