c = 0
while c < 10:
    c += 1
    print(c)
    if c == 5:
        #print('Termina el bucle')
        print('Salta a la siguiente iteracion')
        #break
        continue #El "continue" es para no seguir las instrucciones que siguen despues del continue y que pase al inicio del buclek, en etse caso al [while (c<10)]
    print('Despues de continue')
else:
    print('Fin del bucle')