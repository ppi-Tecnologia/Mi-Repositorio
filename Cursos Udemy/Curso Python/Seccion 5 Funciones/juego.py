import random

def jugar(vidas):
    numero_random = random.randint(1,100)
    numero_elegido = None
    
    while numero_elegido != numero_random:
        print('Ingrese un numero entre 1 y 100')
        numero_elegido = int(input())
        
        if numero_elegido > numero_random:
            print("Elige un numero mas pequeño")
            vidas -= 1
        elif numero_elegido < numero_random:
            print('Elije un numero mas alto')
            vidas -= 1
            
        if vidas == 0:
            print('GAME OVER')
            break
    
        print(f'Te quedan {vidas} vidas')
            
        if numero_elegido == numero_random:
            print('FELICIDADES, GANASTE')
            

def main():
    while True:
        menu = '''
        ADIVINA EL NUMERO
        1. Nivel Facil
        2. Nivel Medio
        3. Nivel Dificil
        4. Salir
        '''
        opcion = input(menu)
        
        if opcion == '1':
            jugar(10)
        elif opcion == '2':
            jugar(7)
        elif opcion == '3':
            jugar(5)
        elif opcion == '4':
            print('Cerrando el juego')
            break
        else:
            print('Opcion INCORRECTA, VUELVA A INGRESAR')
    
if __name__ == '__main__':
    main()
    