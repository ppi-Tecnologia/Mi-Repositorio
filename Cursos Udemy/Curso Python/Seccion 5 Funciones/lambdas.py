sumar = lambda a,b: a+b # Suma dos numeros
restar = lambda a,b: a-b # resta dos numeros
par = lambda n: n % 2 == 0 # devuelve True si el nuermo es par
impar = lambda n: n % 2 != 0 # Devuelve True si el numero es impar
revertir_palabra = lambda cadena: cadena[::-1]  # Devuelve la misma cadena pero escrita al reves

print(sumar(4,5))
print(restar(10,6))
print(par(5))
print(impar(5))
print(revertir_palabra('Castrillon'))