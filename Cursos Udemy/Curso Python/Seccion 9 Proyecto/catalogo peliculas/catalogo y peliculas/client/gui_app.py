import tkinter as tk
from tkinter import ttk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff = 0) # Creando la barra menu 
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio) #Añadiendo un apartado en el menu
    
    menu_inicio.add_command(label = 'Crear un registro en BD') # Añadiendo opciones al boton "Inicio"
    menu_inicio.add_command(label = 'Eliminar un registro en BD') # Añadiendo opciones al boton "Inicio"
    menu_inicio.add_command(label = 'Salir', command = root.destroy) # Añadiendo opciones al boton "Inicio"
    
    barra_menu.add_cascade(label = 'Consultas',) # Añadiendo un apartado en el menu
    barra_menu.add_cascade(label = 'Configuracion') # Añadiendo un apartado en el menu
    barra_menu.add_cascade(label = 'Ayuda') # Añadiendo un apartado en el menu

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 480, height = 320)
        self.root = root
        self.pack() # Empaquetar
        #self.config(bg = 'green') # Tamaño ventana, color de fondo
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
        
    def campos_pelicula(self):
        #Labels de cada campo
        self.label_nombre = tk.Label(self, text = 'Nombre: ') # Nombre del Label
        self.label_nombre.config(font = ('Cascadia Code', 12, 'bold')) #Tipo de letra, tamaño y estilo
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10) #Posicio
        
        self.label_duracion = tk.Label(self, text = 'Duracion: ') # Nombre del Label
        self.label_duracion.config(font = ('Cascadia Code', 12, 'bold')) #Tipo de letra, tamaño y estilo
        self.label_duracion.grid(row = 1, column = 0, padx = 10, pady = 10) #Posicio
        
        self.label_genero = tk.Label(self, text = 'Genero: ') # Nombre del Label
        self.label_genero.config(font = ('Cascadia Code', 12, 'bold')) #Tipo de letra, tamaño y estilo
        self.label_genero.grid(row = 2, column = 0, padx = 10, pady = 10) #Posicio
        
        #Entrys de cada campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre) #Para meterlo al paquete
        self.entry_nombre.config(width = 50, font = ('Cascadia Code', 12)) # ancho, desactivado y tipo de letra con tamaño
        self.entry_nombre.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 2) # Fila, Columna, Paddingx, Paddingy, cuantas columnas ocupara
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable = self.mi_duracion) #Para meterlo al paquete
        self.entry_duracion.config(width = 50, font = ('Cascadia Code', 12))# ancho, desactivado y tipo de letra con tamaño
        self.entry_duracion.grid(row = 1, column = 1, padx = 10, pady = 10, columnspan = 2) #Posicion
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable = self.mi_genero) #Para meterlo al paquete
        self.entry_genero.config(width = 50, font = ('Cascadia Code', 12))# ancho, desactivado y tipo de letra con tamaño
        self.entry_genero.grid(row = 2, column = 1, padx = 10, pady = 10, columnspan = 2) #Posicion

        #Botones
        self.boton_nuevo = tk.Button(self, text = 'Nuevo', command = self.habilitar_campos)
        self.boton_nuevo.config(width = 20, font = ('Cascadia Code', 12, 'bold'), fg = '#DAD5D6', bg = 'green', cursor = 'hand2', activebackground = '#35BD6F') # Anchura, Tipo de letra, tamaño, estilo, color de letra, color fondo, cursor, color cuando se active el boton
        self.boton_nuevo.grid(row = 3, column = 0, padx = 10, pady = 10) 
        
        self.boton_guardar = tk.Button(self, text = 'Guardar', command = self.guardar_datos)
        self.boton_guardar.config(width = 20, font = ('Cascadia Code', 12, 'bold'), fg = '#DAD5D6', bg = '#1658A2', cursor = 'hand2', activebackground = '#3586DF')
        self.boton_guardar.grid(row = 3, column = 1, padx = 10, pady = 10)
        
        self.boton_cancelar = tk.Button(self, text = 'Cancelar', command = self.deshabilitar_campos)
        self.boton_cancelar.config(width = 20, font = ('Cascadia Code', 12, 'bold'), fg = '#DAD5D6', bg = '#BD152E', cursor = 'hand2', activebackground = '#E15370')
        self.boton_cancelar.grid(row = 3, column = 2, padx = 10, pady = 10)
        
    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state = 'normal')
        self.entry_duracion.config(state = 'normal')
        self.entry_genero.config(state = 'normal')
            
        self.boton_cancelar.config(state = 'normal')
        self.boton_guardar.config(state = 'normal')
        
    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        self.entry_nombre.config(state = 'disabled')
        self.entry_duracion.config(state = 'disabled')
        self.entry_genero.config(state = 'disabled')
            
        self.boton_cancelar.config(state = 'disabled')
        self.boton_guardar.config(state = 'disabled')
        
    def guardar_datos(self):
        self.deshabilitar_campos()
   
    def tabla_peliculas(self):
        self.tabla = ttk.Treeview(self, columns = ('Nombre, Duracion, Genero'))
        self.tabla.grid(column = 0, row = 4, columnspan = 4)
        
        self.tabla.heading('#0', text = 'ID')
        self.tabla.heading('#1', text = 'NOMBRE')
        self.tabla.heading('#2', text = 'DURACION')
        self.tabla.heading('#3', text = 'GENERO')
        
        self.tabla.insert('', 0, text = '1', values = ('Los Vengadores', '2:35', 'Accion'))
        
        #Boton Editar
        self.boton_editar = tk.Button(self, text = 'Editar')
        self.boton_editar.config(width = 20, font = ('Cascadia Code', 12, 'bold'), fg = '#DAD5D6', bg = 'green', cursor = 'hand2', activebackground = '#35BD6F') # Anchura, Tipo de letra, tamaño, estilo, color de letra, color fondo, cursor, color cuando se active el boton
        self.boton_editar.grid(row = 5, column = 0, padx = 10, pady = 10)
        
        #Boton Eliminar
        self.boton_eliminar = tk.Button(self, text = 'Eliminar')
        self.boton_eliminar.config(width = 20, font = ('Cascadia Code', 12, 'bold'), fg = '#DAD5D6', bg = '#BD152E', cursor = 'hand2', activebackground = '#E15370')
        self.boton_eliminar.grid(row = 5, column = 1, padx = 10, pady = 10)