def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a=None, b=None):
    if a==None or b==None:
        print('Juan Daniel')
        return 
    return a*b    

def dividir(a, b):
    return a//b
        
suma = sumar(70,80)
print(suma)

resta = restar(90,80)
print(resta)

multiplicacion = multiplicar()
print(multiplicacion)

division = dividir(40,2)
print(division)