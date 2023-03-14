#  ULTIMO EN ENTRAR, PRIMERO EN SALIR

pila = [1, 2 ,3 ,4 ,5]

pila.append(6) #  Agrega el elemento 6 a ultimo en la lista
pila.append(7) #  Agrega el elemento 7 a ultimo de la lista

pila.pop() # Elimina el elemento 7 porque fue el ultimo en entrar de la lista
pila.pop() # Elimina el elemento 6 ya que es el ultimo elemento de la lista

print(pila)