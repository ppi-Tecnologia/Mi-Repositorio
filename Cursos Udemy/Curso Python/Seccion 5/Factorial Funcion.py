def factorial(n):
    resultado = 1
    i = 1
    while i <= n:
        resultado*=i
        i+=1
    return resultado

print('Ingrese un numero para realizar el factorial')
num = int(input())
result = factorial(num)
print('Resultado del factorial: ', result)
