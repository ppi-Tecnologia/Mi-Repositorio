from random import randint,random,uniform
'''Crea 2 listas y una tupla que tendrá números de 1 a 9. La primera lista se llamará pares y el segundo impar, ambos estarán vacíos. Después multiplica cada uno de los números de la tupla por un número aleatorio entre 1 y 100, si el resultado es par guarda ese número en la lista de pares y si es impar en la lista  de impares. Muestra por consola: -la multiplicación que se produce junto con su resultado con el formato 2 x 3 = 6 y la lista de pares e impares

'''


pares = []
impares = []
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

for numero in tupla:
    a=randint(0,100)
    resultado = numero * a
    print(numero,"x",a,"=",resultado)
    if resultado % 2 == 0:
        pares.append(resultado)
    else:
        impares.append(resultado)
        
print(pares)
print(impares)
print(tupla)
