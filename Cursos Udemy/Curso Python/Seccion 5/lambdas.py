sumar = lambda a,b: a+b
restar = lambda a,b: a-b
par = lambda n: n % 2 == 0
impar = lambda n: n % 2 != 0
revertir_palabra = lambda cadena: cadena[::-1]

print(sumar(4,5))
print(restar(10,6))
print(par(5))
print(impar(5))
print(revertir_palabra('Castrillon'))