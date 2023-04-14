class OperadorException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

def dividir (a, b):
    if b == 0:
        raise OperadorException("Error: No puedes dividir entre 0")
    else:
        return a / b
    
    
dividir(4, 0)