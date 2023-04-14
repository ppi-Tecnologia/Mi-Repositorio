i = 0
suma = 0
while i < 3:
    try:
        num = int(input(f'Escriba un numero {i + 1} :'))
        suma += num
        i += 1
    except:
        print('Error: Ingrese solo numeros enteros')
    else:
        print('Todo ha funcionado correctamente')
    finally:
        print('Fin de la Ejecucion')

print(f'La suma total es {suma}')