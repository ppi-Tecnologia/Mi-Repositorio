numeros =  {'uno':1,'dos':2,'tres':3,'cuatro':4}

numeros['cinco'] = 5   # Agregar un elemento al diccionario
numeros.get('tres', 'No se encontro') # Me trae el valor de 'tres', Si no existe entonces me devuelve 'No se encontro'. Se debe buscar por clave y no por valor

numeros.keys()  # Devuelve todas las claves del diccinario
numeros.values()  # Devuelve todos los valores del diccionario
numeros.items()  # Me devuelve una lista donde se encuentra la clave y valor
 
numeros.pop('cinco', 'No se encontro') # Elimina el elemento 'cinco', en caso de no encontrarlo le devuelve el 'No se encontro'

print(numeros)