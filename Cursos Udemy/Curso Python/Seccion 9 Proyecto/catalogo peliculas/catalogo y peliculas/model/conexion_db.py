import sqlite3

class ConexionDB:
    def __init__(self):
        self.base_datos = 'C://Users//Castrillon//Documents//GitHub//MiPrimerRepositorio//Cursos Udemy//Curso Python//Seccion 9 Proyecto//catalogo peliculas//catalogo y peliculas//database//peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
        
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()