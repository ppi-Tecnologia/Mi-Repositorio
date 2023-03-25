from random import choice
def generar_contraseña():
    global minusculas, mayusculas, numeros, simbolos
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    simbolos= ['!','#','$','%','&','@','¡']
    contraseña = ''
    print('Cuantos caracteres debe tener la contraseña?')
    contador = int(input())
    while len(contraseña) < contador:
        contraseña += choice(minusculas)
        print(contraseña)
        contraseña += choice(mayusculas)
        print(contraseña)
        contraseña += choice(numeros)
        print(contraseña)
        contraseña += choice(simbolos)
        print(contraseña)
    return contraseña

contra = generar_contraseña()
print('Su contraseña es:', contra)
            
        