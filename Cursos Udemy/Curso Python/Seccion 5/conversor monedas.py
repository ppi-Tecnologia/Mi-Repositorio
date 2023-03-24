def convertir(valor_dolar, pais):
    print(f'Ingrese la cantidad de {pais}')
    cantidad_moneda = float(input())
    
    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print(f'tienes ${dolares} Dolares')
    
def main():
    convertir(4742.54, 'pesos colombianos')
    
if __name__ == '__main__':
    main()