from figuras2 import Circulo, Rectangulo, probar_figura

def main():
    while True:
        menu = '''
            CALCULADOR DE AREA Y PERIMETRO
        
            1. Rectangulo
            2. Circulo
            4. Salir
        '''
        opcion = input(menu)

        if opcion == '1':
            print('Ingrese la base')
            base = float(input())
            print('Ingrese la altura')
            altura = float(input())
            rectangulo1 = Rectangulo('Rectangulo', base, altura)
            print(f'{rectangulo1.get_nombre()}, Base: {rectangulo1.get_base()}, Altura: {rectangulo1.get_altura()}')
            probar_figura(rectangulo1)                    
        elif opcion == '2':
            print('Ingrese el radio')
            radio = float(input())
            circulo1 = Circulo('Circulo', radio)
            print(f'{circulo1.get_nombre()}, Radio: {circulo1.get_radio()}')
            probar_figura(circulo1)
            #print(f'Area: {circulo1.calcular_area()} \nPerimetro: {circulo1.calcular_perimetro()}')
        elif opcion == '4':
            print('Saliendo del programa')
            break
        else:
            print('opcion incorrecta')
        
if __name__ == '__main__':
    main()