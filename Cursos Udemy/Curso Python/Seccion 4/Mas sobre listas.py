#list.append()  --> Para agregar un elemento al final
#list.extend()  --> extiende la lista al doble
#list.insert(i, x)  --> Inserta u elemento en la posicion dada
#list.remove()  --> Quita el primer elemento de la lista que sea el valor x
#list.pop()  --> Elimina el elemento de la posicion y lo retorna
#list.clear()  --> Elimina todos los elementos de la lista
#list.count() --> Retorna el numero de veces que aparece el elemento en la lista
#list.sort()  --> Ordena la lista por orden alfabetico
lista = ["Juan", 17, 2005, "Manrique", "Antioquia", "Medellin"]
lista.append("City")
lista.extend(lista)
lista.remove("Manrique")
lista.insert(2, 3003)
lista.pop(6)
a = lista.count("Antioquia")
lista.clear()
print(lista, a)