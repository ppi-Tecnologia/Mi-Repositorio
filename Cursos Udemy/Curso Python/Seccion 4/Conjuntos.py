'''a = set()  # Definir un conjunto a. Los conjuntos no respetan el orden 
a = {'a', 'b', 'c'}

'''
 # LOS CONJUNTOS NO PERMITEN QUE HAYAN ITEMS IGUALES
a = set('abracadabra')
b = set('alacazaam')

a.add('d') # Añade el elemento 'd'
a.discard('b') # Elimina el elemento 'b'
a.clear() # Elimina todos los elementos del Conjunto
print(a-b) # Muestra elementos de a que no estan en b
print(a|b) # Muestra elementos de a y b
print(a&b) # Muestra elementos que estan en a y b
print(a^b) # Muestra elementos que estan o en a o en b, pero no en ambas