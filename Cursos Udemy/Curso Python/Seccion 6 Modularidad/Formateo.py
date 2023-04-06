from sys import argv

if len(argv) == 4 :
    nombre = argv[1]
    edad = int(argv[2])
    altura = float(argv[3])
    
    #print(f'Nombre: {nombre} \nEdad: {edad} \nAltura: {altura}')
    #print('Nombre: {} \nEdad: {} \nAltura: {}'.format(nombre, edad, altura))
    #print('Nombre: {n} \nEdad: {e} \nAltura: {a}'.format(n = nombre, e = edad, a = altura))
    print('Nombre: %s \nEdad: %i \nAltura: %f'%(nombre, edad, altura))

else:
    print('Error, Ingrese los argumentos correctamente')
    print('Ejemplo: entrada script.py "Texto" 5')