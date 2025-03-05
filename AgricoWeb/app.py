from flask import Flask
from flask import render_template, redirect, request, Response, session, url_for, g
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

#AGREGAR EL DECORADOR PARA EVITAR EL CACHE
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


#RUTA PRINCIPAL
@app.route('/')
def home():
    return render_template('pagina_inicio.html')

#RUTA PAGINA DE INICIO USUARIO REGISTRADO
@app.route('/admin')
def admin():
    if 'logueado' in session:
        id_usuario = session.get('id_usuario')
        cursor = db.database.cursor()
        cursor.execute("SELECT p.id_pregunta, r.respuesta, r.url_imagen, p.contenido FROM respuesta as r JOIN pregunta as p ON p.id_pregunta = r.id_pregunta")
        myresult = cursor.fetchall()
        insertObject = []
        columnNames = [column[0] for column in cursor.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))
        cursor.close()
        return render_template('admin.html', data = insertObject, id_usuario = id_usuario)
    else:
        return redirect('/acceso-login')

#FUNCIONES PARA HACER PUBLICA EL id_usuario y nombre_usuario
@app.before_request
def before_request():
    if 'logueado' in session:
        g.nombre_usuario = session.get('nombre_usuario')
        g.id_usuario = session.get('id_usuario')

@app.context_processor
def inject_user():
    return dict(
        nombre_usuario=g.get('nombre_usuario', ''),
        id_usuario=g.get('id_usuario', None)
    )

#RUTA PRINCIPAL
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
            session['nombre_usuario'] = account['nombres']
            
            if session['id_rol'] == 2:
                #return render_template("administrador.html", nombre_usuario = session['nombre_usuario'], id_usuario = session['id_usuario'])
                return redirect(url_for('administrador'))
            elif session['id_rol'] == 1:
                #return render_template("inicio_interfaz_usuario.html", nombre_usuario = session['nombre_usuario'], id_usuario = session['id_usuario'])
                return redirect(url_for('inicio_interfaz_usuario'))

        else:
            return render_template('iniciar_sesion.html', mensaje="Usuario incorrecto")
    return render_template('iniciar_sesion.html')


@app.route('/inicio_interfaz_usuario')
def inicio_interfaz_usuario():
    if 'logueado' in session:
        return render_template("inicio_interfaz_usuario.html", nombre_usuario=session['nombre_usuario'], id_usuario=session['id_usuario'])
    else:
        return redirect('/acceso-login')

        
#RUTA A PAGINA DE REGISTRO
@app.route('/registro')
def registro():
    return render_template('registro.html')

#RUTA A PAGINA DE INICIO DE SESION
@app.route('/iniciar_sesion')
def iniciar_sesion():
    return render_template('iniciar_sesion.html')

#RUTA PARA ACCEDER AL INICIO DE INTERFAZ DE USUARIO REGISTRADO
@app.route('/administrador')
def administrador():
    if 'logueado' in session:
        return render_template('administrador.html', nombre_usuario=session['nombre_usuario'])
    else: 
        return redirect(url_for('login'))

#RUTA DE TABLA DE PREGUNTAS RESPONDIDAS
@app.route('/tabla_preguntas_respondidas')
def tabla_preguntas_respondidas():
    if 'logueado' in session:
        nombre_usuario = session.get('nombre_usuario')
        cursor = db.database.cursor()
        cursor.execute("SELECT * FROM respuesta")
        myresult = cursor.fetchall()
        insertObject = []
        columnNames = [column[0] for column in cursor.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))
        cursor.close()
        
        return render_template('tabla_preguntas_respondidas.html' , data=insertObject, nombre_usuario=nombre_usuario)
    else:
        return redirect(url_for('login'))
 
#FUNCION PARA ELIMINAR RESPUESTAS EN LA TABLA DE PREGUNTAS RESPONDIDAS
@app.route('/eliminar_respuesta/<string:id_respuesta>')
def eliminar_respuesta(id_respuesta):
    if 'logueado' in session:
        cursor = db.database.cursor()
        sql = "DELETE FROM respuesta WHERE id_respuesta=%s"
        data = (id_respuesta,)
        cursor.execute(sql, data)
        db.database.commit()
        return redirect(url_for('tabla_preguntas_respondidas'))
    else:
        return redirect(url_for('login'))

#FUNCION PARA EDITAR RESPUESTAS DE LA TABLA DE PREGUNTAS RESPONDIDAS
@app.route('/editar_respuesta/<string:id_respuesta>', methods=["POST"])
def editar_respuesta(id_respuesta):
    if 'logueado' in session:
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
    else:
        return redirect(url_for('login'))




#RUTA PARA LA TABLA DE PREGUNTAS SIN RESPONDER
@app.route('/tabla_preguntas_sin_responder')
def tabla_preguntas_sin_responder():
    if 'logueado' in session:
        nombre_usuario = session.get('nombre_usuario')
        cursor = db.database.cursor()
        cursor.execute("SELECT * FROM pregunta WHERE estado = 'Sin Responder'")
        myresult = cursor.fetchall()
        insertObject = []
        columnNames = [column[0] for column in cursor.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))
        cursor.close()
        return render_template('tabla_preguntas_sin_responder.html', data = insertObject, nombre_usuario = nombre_usuario)
    else:
        return redirect(url_for('login'))

#FUNCION PARA ELIMINAR PREGUNTAS DE LA TABLA DE PREGUNTAS SIN RESPONDER
@app.route('/eliminar_pregunta/<string:id_pregunta>', methods=["POST"])
def eliminar_pregunta(id_pregunta):
    if 'logueado' in session:
        cursor = db.database.cursor()
        sql = "DELETE FROM pregunta WHERE id_pregunta = %s"
        data = (id_pregunta,)
        cursor.execute(sql, data)
        db.database.commit()
        return redirect(url_for('tabla_preguntas_sin_responder'))
    else: 
        return redirect(url_for('login'))

#FUNCION PARA RESPONDER PREGUNTAS DE LA TABLA PREGUNTAS SIN RESPONDER
@app.route('/responder_pregunta/', methods=['POST'])
def responder_pregunta():
    if 'logueado' in session:
        id_usuario = session['id_usuario']
        id_pregunta = request.form['id_pregunta']
        respuesta = request.form['respuesta']
        urlImagen = request.form['UrlImagen']
        fecha_publicacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if respuesta and urlImagen:
            cursor = db.database.cursor()
            sql = "INSERT INTO respuesta(id_usuario, id_pregunta, respuesta, url_imagen, fecha_publicacion) VALUES(%s, %s, %s, %s, %s)"
            data = (id_usuario, id_pregunta, respuesta, urlImagen, fecha_publicacion)
            cursor.execute(sql, data)
            sql1 = ("UPDATE pregunta SET estado = 'Respondida' WHERE id_pregunta = %s")
            data1 = (id_pregunta,)
            cursor.execute(sql1, data1)
            db.database.commit()
        return redirect(url_for('tabla_preguntas_sin_responder'))
    else:
        return redirect(url_for('login'))

#FUNCION PARA AÑADIR UNA PREGUNTA NUEVA A LA TABLA DE PREGUNTAS SIN RESPONDER
@app.route('/pregunta', methods=['POST'])
def añadir_pregunta():
    if 'logueado' in session:
        contenido = request.form['contenido']
        fecha_edicion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if contenido:
            id_usuario = session['id_usuario']
            cursor = db.database.cursor()
            sql = "INSERT INTO pregunta(id_usuario, contenido, fecha, estado) VALUES (%s, %s, %s, 'Sin Responder')"
            data = (id_usuario, contenido, fecha_edicion)
            cursor.execute(sql, data)
            db.database.commit()
        return redirect(url_for('tabla_preguntas_sin_responder'))
    else:
        return redirect(url_for('login'))

#RUTA PARA LA TABLA DE USUARIOS
@app.route('/tabla_usuarios')
def tabla_usuarios():
    if 'logueado' in session:
        nombre_usuario = session.get('nombre_usuario')
        cursor = db.database.cursor()
        cursor.execute("SELECT * FROM usuario")
        myresult = cursor.fetchall()
        #Convertir los datos a diccionario
        insertObject = []
        columnNames = [column[0] for column in cursor.description]
        for record in myresult:
            insertObject.append(dict(zip(columnNames, record)))
        cursor.close()
        
        return render_template('tabla_usuarios.html', data=insertObject, nombre_usuario = nombre_usuario)
    else:
        return redirect(url_for('login'))

#CREAR REGISTRO EN LA TABLA DE USUARIOS
@app.route('/crear-registro', methods = ["GET", "POST"])
def crear_registro():
    if 'logueado' in session:
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
    else:
        return redirect(url_for('login'))

#CREAR UN USUARIO NUEVO EN LA TABLA DE USUARIOS
@app.route('/usuario', methods=['POST'])
def addUser():
    if 'logueado' in session:
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
    else:
        return redirect(url_for('login'))

#ELIMINAR UN USUARIO EN LA TABLA DE USUARIOS
@app.route('/eliminar/<string:id_usuario>')
def eliminar(id_usuario):
    if 'logueado' in session:
        cursor = db.database.cursor()
        sql = "DELETE FROM usuario WHERE id_usuario=%s"
        data = (id_usuario,)
        cursor.execute(sql, data)
        db.database.commit()
        return redirect(url_for('tabla_usuarios'))
    else:
        return redirect(url_for('login'))
    
#EDITAR UN USUARIO EN LA TABLA DE USUARIOS
@app.route('/editar/<string:id_usuario>', methods=['POST'])
def editar(id_usuario):
    if 'logueado' in session:
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
    else:
        return redirect(url_for('login'))

#GUARDAR LA PREGUNTA HECHA POR EL USUARIO REGISTRADO
@app.route('/guardar_pregunta/', methods = ['POST'])
def guardar_pregunta():
    if 'logueado' in session:
        pregunta = request.form['pregunta']
        id_usuario = session['id_usuario']
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if pregunta and id_usuario and fecha:
            cursor = db.database.cursor()
            sql = "INSERT INTO pregunta (id_usuario, contenido, fecha, estado) VALUES(%s, %s, %s, 'Sin Responder')"
            data = (id_usuario, pregunta, fecha)
            cursor.execute(sql, data)
            db.database.commit()
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('login'))
    
    
@app.route("/cerrar-sesion")
def cerrar_sesion():
    session.pop('logueado', False)
    session.pop('id_usuario', None)
    session.pop('id_rol', None)
    session.pop('nombre_usuario', None)
    
    '''
    response = redirect(url_for('login'))
    response.headers['Cache-control'] = 'no store'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    '''
    
    #return response
    return redirect(url_for('login'))





if __name__ == '__main__':
    app.secret_key = "gabriel_hds"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
