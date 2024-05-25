from flask import Flask
from flask import render_template, redirect, request, Response, session, url_for
from flask_mysqldb import MySQL, MySQLdb
import database as db
from datetime import datetime

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
    cursor = db.database.cursor()
    cursor.execute("SELECT p.id_pregunta, r.respuesta, r.url_imagen, p.contenido FROM respuesta as r JOIN pregunta as p ON p.id_pregunta = r.id_pregunta")
    myresult = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('admin.html', data = insertObject)

@app.route('/inicio')
def pagina_inicio():
    return render_template('pagina_inicio.html')

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

@app.route('/tabla_preguntas_respondidas')
def tabla_preguntas_respondidas():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM respuesta")
    myresult = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    
    return render_template('tabla_preguntas_respondidas.html' , data=insertObject)
    
@app.route('/eliminar_respuesta/<string:id_respuesta>')
def eliminar_respuesta(id_respuesta):
    cursor = db.database.cursor()
    sql = "DELETE FROM respuesta WHERE id_respuesta=%s"
    data = (id_respuesta,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('tabla_preguntas_respondidas'))

@app.route('/editar_respuesta/<string:id_respuesta>', methods=["POST"])
def editar_respuesta(id_respuesta):
    respuesta = request.form['respuesta']
    urlImagen = request.form['urlImagen']
    #fecha_edicion = request.form['fecha_edicion']
    fecha_edicion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if respuesta and urlImagen:
        cursor = db.database.cursor()
        sql = "UPDATE respuesta SET respuesta = %s, fecha_edicion = %s, url_imagen = %s WHERE id_respuesta = %s"
        data = (respuesta, fecha_edicion, urlImagen, id_respuesta)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('tabla_preguntas_respondidas'))


@app.route('/tabla_preguntas_sin_responder')
def tabla_preguntas_sin_responder():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM pregunta")
    myresult = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('tabla_preguntas_sin_responder.html', data = insertObject)




@app.route('/eliminar_pregunta/<string:id_pregunta>', methods=["POST"])
def eliminar_pregunta(id_pregunta):
    cursor = db.database.cursor()
    sql = "DELETE FROM pregunta WHERE id_pregunta = %s"
    data = (id_pregunta,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('tabla_preguntas_sin_responder'))

@app.route('/responder_pregunta/<string:id_pregunta>', methods=['POST'])
def responder_pregunta(id_pregunta):
    respuesta = request.form['respuesta']
    cursor = db.database.cursor()
    consulta = "SELECT id_usuario FROM pregunta WHERE id_pregunta = %s"
    data = (id_pregunta,)
    cursor.execute(consulta, data)
    #consulta1 = "SELECT id_usuario FROM pregunta WHERE id_pregunta = %s"
    #cursor.execute(consulta1)
    id_usuario = cursor.fetchone()[0]
    fecha_edicion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if respuesta:
        cursor = db.database.cursor()
        sql = "INSERT INTO respuesta(id_usuario, id_pregunta, respuesta, fecha_publicacion, fecha_edicion) VALUES(%s, %s, %s, %s, 'Sin Editar')"
        data = (id_usuario, id_pregunta, respuesta, fecha_edicion)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('tabla_preguntas_sin_responder'))

@app.route('/pregunta', methods=['POST'])
def añadir_pregunta():
    contenido = request.form['contenido']
    '''cursor = db.database.cursor()
    consulta1 = "SELECT id_usuario FROM pregunta WHERE id_pregunta = %s"
    cursor.execute(consulta1)
    usuario = cursor.fetchone()[0]'''
    fecha_edicion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if contenido:
        cursor = db.database.cursor()
        sql = "INSERT INTO pregunta(id_usuario, contenido, fecha, estado) VALUES ('10000', %s, %s, 'Sin Responder')"
        data = (contenido, fecha_edicion)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('tabla_preguntas_sin_responder'))

    




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

#CREAR REGISTRO EN LA TABLA DE USUARIOS
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

#CREAR UN USUARIO NUEVO EN LA TABLA DE USUARIOS
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

#ELIMINAR UN USUARIO EN LA TABLA DE USUARIOS
@app.route('/eliminar/<string:id_usuario>')
def eliminar(id_usuario):
    cursor = db.database.cursor()
    sql = "DELETE FROM usuario WHERE id_usuario=%s"
    data = (id_usuario,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('tabla_usuarios'))
    
#EDITAR UN USUARIO EN LA TABLA DE USUARIOS
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
