from flask import Flask
from flask import render_template, redirect, request, Response, session, url_for
from flask_mysqldb import MySQL, MySQLdb
import database as db

app = Flask(__name__, template_folder='template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456' 
app.config['MYSQL_DB'] = 'agricoweb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('pagina_inicio.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

#FUNCION DE LOGIN
@app.route('/acceso-login', methods = ["GET", "POST"])
def login():
    
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword':
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']
    
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE correo = %s AND contraseña = %s',(_correo,_password,))
        account = cur.fetchone()
        
        if account:
            session['logueado'] = True
            session['id_usuario'] = account['id_usuario']
            session['id_rol'] = account['id_rol']
            
            if session['id_rol'] == 2:
                return render_template("administrador.html")
            elif session['id_rol'] == 1:
                return render_template("admin.html")
            
        else:
            return render_template('iniciar_sesion.html', mensaje="Usuario incorrecto")
        
# REGISTRO ---
@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')

@app.route('/administrador')
def administrador():
    return render_template('administrador.html')

@app.route('/tabla_usuarios')
def tabla_usuarios():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM usuario")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    
    return render_template('tabla_usuarios.html', data=insertObject)

@app.route('/crear-registro', methods = ["GET", "POST"])
def crear_registro():
    nombre = request.form['txtNombre']
    apellido = request.form['txtApellido']
    correo = request.form['txtCorreo']
    contrasena = request.form['txtContrasena']
    telefono = request.form['txtTelefono']
    fecha_nacimiento = request.form['txtFechaNacimiento']
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuario(nombres, apellidos, correo, contraseña, telefono, id_rol, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, '1', %s)",(nombre, apellido, correo, contrasena, telefono, fecha_nacimiento))
    mysql.connection.commit()
    
    return render_template("iniciar_sesion.html", mensaje2="Usuario registrado correctamente")
    
@app.route('/usuario', methods=['POST'])
def addUser():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    telefono = request.form['telefono']
    id_rol = request.form['id_rol']
    fecha_nacimiento = request.form['fecha_nacimiento']
    
    if nombres and apellidos and correo and contrasena and telefono and id_rol and fecha_nacimiento:
        cursor = db.database.cursor()
        sql = "INSERT INTO usuario(nombres, apellidos, correo, contraseña, telefono, id_rol, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (nombres, apellidos, correo, contrasena, telefono, id_rol, fecha_nacimiento)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('tabla_usuarios'))

@app.route('/eliminar/<string:id_usuario>')
def eliminar(id_usuario):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuario WHERE id_usuario=%s"
    data = (id_usuario,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('tabla_usuarios'))
    
@app.route('/editar/<string:id_usuario>', methods=['POST'])
def editar(id_usuario):
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    correo = request.form['correo']
    contrasena = request.form['contrasena']
    telefono = request.form['telefono']
    id_rol = request.form['id_rol']
    fecha_nacimiento = request.form['fecha_nacimiento']
    
    if nombres and apellidos and correo and contrasena and telefono and id_rol and fecha_nacimiento:
        cursor = db.database.cursor()
        sql = "UPDATE usuario SET nombres = %s, apellidos = %s, correo = %s, contraseña = %s, telefono = %s, id_rol = %s, fecha_nacimiento = %s WHERE id_usuario = %s"
        data = (nombres, apellidos, correo, contrasena, telefono, id_rol, fecha_nacimiento, id_usuario)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('tabla_usuarios'))



if __name__ == '__main__':
    app.secret_key = "gabriel_hds"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
