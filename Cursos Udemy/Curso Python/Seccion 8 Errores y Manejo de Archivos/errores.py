i = 0
suma = 0
while i < 3:
    try:
        num = int(input(f'Escriba un numero {i + 1} :'))
        suma += num
        i += 1
    # Esto se ejecuta si ocurre un error
    except: 
        print('Error: Ingrese solo numeros enteros')
    # Esto se ejecuta si todo salio bien 
    else:
        print('Todo ha funcionado correctamente')
    # Esto se ejecuta si todo salio no o bien
    finally:
        print('Fin de la Ejecucion')

print(f'La suma total es {suma}')