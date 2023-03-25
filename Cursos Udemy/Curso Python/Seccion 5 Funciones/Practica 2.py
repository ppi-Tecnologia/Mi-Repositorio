def numero_primo(num):
    contador = 0
    i = 1
    while(i <= num):
        if num % i == 0:
            contador += 1
        i += 1
        if contador > 2:
            break
    if contador <= 2:
        return print('Es un numero Primo', num)
    else:
        return print('No es un numero primo', num)
        
print('Ingreser un numero:')
var = int(input())

numero_primo(var)

