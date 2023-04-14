divi = 0
try:
    a = int(input(f'Ingrese un numero'))
    b = int(input(f'Ingrese otro numero'))
    divi = a / b
except ValueError:
    print('Error: Ingrese solo numeros enteros')
except ZeroDivisionError:
    print('no se puede dividir entre 0')
except Exception as error:
    print(f'Ha ocurrido un error imprevisto :', type(error).__name__)
    
print(f'La division es {divi}') 