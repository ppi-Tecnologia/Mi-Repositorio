# pip install mysql-connector-python
import mysql.connector

class CConexion:
    
    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root', password='123456',
                                               host='127.0.0.1',
                                               database='clientesdb',
                                               port='3306')
            print("Conexion Correcta")
            return conexion
            
            
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error))
            return conexion
        
    ConexionBaseDeDatos()