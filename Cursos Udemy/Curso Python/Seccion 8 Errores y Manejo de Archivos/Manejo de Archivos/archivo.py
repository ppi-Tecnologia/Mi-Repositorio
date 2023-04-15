from io import open
from os import path

def escribir_archivo():
    archivo = open('texto.txt','w') #La w es para ponerlo en modo escritura
    archivo.write('Hola Mundo de Python')
    archivo.close()
    
def leer_archivo():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r') #'r' Es para modo lectura
        #textos = archivo.read()
        textos = archivo.readlines() #Mete cada una de las lineas del archivo como elementos individuales de una lista
        archivo.close()
        print(textos)
        
def agregar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'a') #'a' Es el modo actualizaar, es para poner otra linea de texto al archivo 
        archivo.write('\nHola Juan')
        archivo.close()

def modificar_datos():
    if path.isfile('texto.txt'):
        archivo = open('texto.txt', 'r+') # 'r+' Es para Lectura y Escritura
        texto = archivo.readlines()
        print(texto)
        texto[1] = 'Hola Juan Castrillon\n'
        print(texto)
        archivo.seek(0) # Pone el cursor en el caracter 0 del archivo
        archivo.writelines(texto) #Sobreescribe los elementos de la lista
        archivo.close()
        print(texto)
        
def eliminar_datos():
    archivo = open('texto.txt','w') #La w es para ponerlo en modo escritura
    archivo.close()

eliminar_datos()
#modificar_datos()
#agregar_datos()        
#leer_archivo() 
#escribir_archivo()
 