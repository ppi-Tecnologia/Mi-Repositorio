def sumar(*args, **kwargs):
    for n in args:
        suma = 0
        suma += n
    return suma, kwargs

suma_total, datos = sumar(1,2,3,4,5,6,7,8, nombre = 'Juan', edad = 25)

print('La suma total de datos es: ', suma_total)
print(datos)