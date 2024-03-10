def sumar_posiciones(matriz, valor, indice=0, suma=0):
    # Caso base: si el índice es igual a la longitud de la matriz, regresar la suma acumulada
    if indice == len(matriz):
        return suma
    # Si el elemento en la posición actual es igual al valor, agregar la posición a la suma
    if matriz[indice] == valor:
        suma += indice
    # Llamar recursivamente con el siguiente índice
    return sumar_posiciones(matriz, valor, indice + 1, suma)

# Definir la matriz
matriz = [3, 9, 7, 3, 8, 3]

# Valor a buscar en la matriz
valor_a_buscar = 3

# Invocar la función recursiva
resultado = sumar_posiciones(matriz, valor_a_buscar)

# Imprimir el resultado
print(f"La suma de las posiciones donde se encuentra el número {valor_a_buscar} es: {resultado}")