def dividir (a, b):
    if b == 0:
        raise ZeroDivisionError("Error: No puedes dividir entre 0")
    else:
        return a / b
    
    
dividir(4, 0)