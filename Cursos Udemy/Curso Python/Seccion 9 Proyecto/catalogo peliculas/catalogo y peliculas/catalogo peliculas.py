import tkinter as tk
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Catalogo de Peliculas') #titulo de la ventana
    root.iconbitmap('C://Users//Castrillon//Desktop//Cosas//Visual Studio Code archivos//Cursos Udemy//Curso Python//Seccion 9 Proyecto//catalogo peliculas//catalogo y peliculas//img//icono.ico') #icono
    root.resizable(0,0) # (horizontal, vertical) # Si se puede modificar la ventana
    barra_menu(root)
    
    app = Frame(root = root)
    
    app.mainloop()

if __name__ == '__main__':
    main()
    