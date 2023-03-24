def convertir(valor_dolar, pais):
    print(f'Ingrese la cantidad de {pais}')
    cantidad_moneda = float(input())
    
    dolares = cantidad_moneda / valor_dolar
    dolares = round(dolares, 2)
    print(f'tienes ${dolares} Dolares')
    
def main():
    while True:
        menu = '''
        1. Soles Perunaos a Dolares
        2. Pesos Mexicanos a Dolares
        3. Pesos Colombianos a Dolares
        4. Salir
        INGRESE UNA OPCION: '''
        
        opcion = input(menu)
        
        if opcion == '1':
            convertir(3.77,'soles Peruanos')
        elif opcion == '2':
            convertir(18,48,'pesos Mexicanos')
        elif opcion == '3':
            convertir(4742.54, 'pesos Colombianos')
        elif opcion == '4':
            print('Cerrando el conversor de monedas')
            break
        else:
            print('Opcion INCORRECTA')
            print('Ingrese una opcion entre 1 - 4')
    
if __name__ == '__main__':
    main()