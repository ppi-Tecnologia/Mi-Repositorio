""" Crear un sistema que detecte si un carácter es vocal o no
Enunciado: dado un carácter determinar si es una vocal.

Análisis: para la solución de este problema, se requiere que el usuario ingrese un carácter y el sistema verifique si es una vocal."""

vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

print('ingrese una letra')
letra = str(input())


if (letra in vocales):
    print(letra, "Es una vocal")
else:
    print(letra , "No es una vocal")