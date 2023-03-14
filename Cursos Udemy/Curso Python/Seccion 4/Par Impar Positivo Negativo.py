print("ingrese un numero")
n = int(input())
if(n != 0):
    if (n > 0):
        if(n % 2 == 0):
            print("Es un Par Positivo")
        else:
            print("Es un Impar Positivo")
    else:
        if(n % 2 == 0):
            print("Es un Par Negativo")
        else:
            print("Es un Impar Negativo")
else:
    print("Es un numero neutro")