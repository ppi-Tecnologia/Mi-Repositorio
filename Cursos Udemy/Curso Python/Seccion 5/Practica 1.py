def palindromo(palabra):
    termino = palabra
    termino = termino.replace(',', '')
    alreves = palabra[::-1]
    alreves = alreves.replace(',', '')
    termino = termino.lower()
    alreves = alreves.lower()
    if termino.replace(' ', '') == alreves.replace(' ', ''):
        return True
    else: 
        return False
    
print('Ingrese una frase:')
cadena = str(input())

verificacion = palindromo(cadena)
print(verificacion)

