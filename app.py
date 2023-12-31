<<<<<<< HEAD
from flask import Flask,render_template,redirect,url_for,request,session,jsonify 
from werkzeug.security import generate_password_hash, check_password_hash
=======
from flask import Flask,render_template,redirect,url_for,request,session, jsonify
>>>>>>> Salvala
import secrets
import dao, daoUsuario, daoDoctor
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os, glob

from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/imagenes'
#Se Genera de manera random un token para el login
app.secret_key = secrets.token_hex(32 // 2)

@app.route('/')
def index():
    if 'correo' in session:
<<<<<<< HEAD
        return render_template('index.html',title="Inicio2",usuario=session['correo'])
    else:
        return render_template('index.html',title="Inicio")
@app.route('/login/')
def login():
=======
        return "<h1>ya tas logeado </h1>" 
    else:
        return render_template('login.html',title="Inicio-Login")

@app.route('/vistaPacientes')
def vistaPacientes():
    if 'correo' in session:
        listapacientes = dao.buscarPaciente("*")
        #poner codigo para poner los pacientes
        return render_template('vistapacientes.html',title="Pacientes", usuario = session['correo'], pacientes = listapacientes)
    else:
        return redirect(url_for('index'))

@app.route('/verRegistroPaciente/')
def verRegistroPaciente():
    return render_template('registroPaciente.html',title="Registro Paciente",usuario = session["correo"])

@app.route('/verLogin/')
def verLogin():
>>>>>>> Salvala
    return render_template('login.html',title="Login")


@app.route('/verCargarImagen/')
def verCargarImagen():
    print(session)
    return render_template('cargarImagen.html',title="Clasificador",usuario = session["correo"])

@app.route('/clasificarImagen',methods=["POST"])
def clasificarImagen():
    file = request.files['imagen']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
    if file.filename == '':
        print("nelson")
    if file.filename.endswith(('.jpg', '.png', '.jpeg', '.gif')):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        rutaimagen = glob.glob("static/imagenes/"+filename)
        print(rutaimagen)
        np.set_printoptions(suppress=True)
        model = load_model("keras_model.h5", compile=False)
        class_names = open("labels.txt", "r").readlines()
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(rutaimagen[0]).convert("RGB")
        print("Wair please...")
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized_image_array
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        Clase = class_name[2:]
        print(class_name[2:])
        PC = confidence_score*100
        print("Confidence Score (Puntualicion de confianza) : %", confidence_score*100)
        return render_template('resultadoClasificacion.html',title="Clasificador",usuario = session["correo"], clase = Clase, puntaje = PC, imagen = rutaimagen)


@app.route('/registroPaciente',methods=["POST"])
def registroPaciente():
    if request.method == "POST":
        nombre = request.form['nombre']
        genero = request.form['genero']
        telefono = request.form['telefono']
        print(nombre)
        print(genero)
        print(telefono)
        if(len(daoUsuario.registrarUsusarioD(nombre,telefono,genero)) !=0):
            return redirect(url_for('vistaPacientes'))
    

@app.route('/vistaRegistrarUsuarioDoctor/')
def vistaRegistrarUsuarioDoctor():
    return render_template('registroUsuarioDoctor.html',title="Registrar")



@app.route('/vistaRegistrarDoctor')
def vistaRegistrarDoctor():
    print (session['id']) 
    datos = {"id" : session['id']}
    return render_template('registroDoctor.html',title="Registrar", datos = datos)

@app.route('/registroDoctor',methods=["POST"])
def registroDoctor():
    if request.method == "POST":
        print(request.form)
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        fecha = request.form['fecha']
        ubicacion = request.form['ubicacion']
        id = request.form['idUsuario']
        if(len(daoDoctor.registrarDoctor(nombre,cedula,fecha,ubicacion,id)) !=0):
            return "Listo"
        else:
            return "Error"
        


@app.route('/registroUsuarioDoctor',methods=["POST"])
def registro():
    if request.method == "POST":
        correo = request.form['correo']
        telefono = request.form['telefono']
        contraseña = request.form['contraseña']
<<<<<<< HEAD
        #encripto la contraseña para seguridad
        contraseña_encriptada = generate_password_hash(contraseña)
        if(len(dao.registrarUsusarioD(telefono,correo,contraseña_encriptada)) !=0):
            return redirect(url_for('login'))
        
=======
        password = generate_password_hash(contraseña)
        if(len(daoUsuario.registrarUsusarioD(telefono, correo, password)) !=0):
            id = daoUsuario.buscarUsusario(correo)[0]["id"]
            session['id'] = id
            return redirect(url_for('vistaRegistrarDoctor'))        
>>>>>>> Salvala


@app.route('/ingresar',methods=["GET", "POST"])
def ingresar():     
    if request.method == "POST":
<<<<<<< HEAD
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        contraseña_encriptada = generate_password_hash(contraseña)
        if(len(dao.buscarUsusario(correo,contraseña_encriptada)) !=0):
            session['correo'] = correo
            return  render_template('vistapacientes.html',title="Pacientes", nombre="nombre")
        else:
            return redirect(url_for('index'))

@app.route('/login2', methods=['POST'])
def login2():
    correo = request.form.get('username')
    contraseña = request.form.get('password')
    # Simulando la verificación del inicio de sesión en el lado del servidor
    contraseñaBD = dao.buscarUsusario(correo)[0]
    print(contraseñaBD['Contraseña'])
    if(check_password_hash(contraseñaBD['Contraseña'], contraseña)):
        # Enviar una respuesta JSON al cliente para indicar que el inicio de sesión fue exitoso
        session['correo'] = correo
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Credenciales incorrectas'})

=======
        try:
            correo = request.form['correo']
            contraseña = request.form['contraseña']
            contraseñaBD = daoUsuario.buscarUsusario(correo)[0]
            print(contraseñaBD)
            print(type(contraseñaBD))
            if(check_password_hash(contraseñaBD['contraseña'], contraseña)):
                session['correo'] = correo
                print(session)
                return redirect(url_for('vistaPacientes'))
            else:
                print("Error no se encontro el usuario")
                return  render_template('login.html',title="Error")
        except:
            print("Error no se encontro el usuario")
>>>>>>> Salvala

"""
@app.route('/login2/', methods =['POST'])
def login2():
    correo = request.form.get('correo')
    contraseña = request.form.get('contraseña')
    contraseñaBD = daoUsuario.buscarUsusario(correo)[0]
    if(check_password_hash(contraseñaBD['Contraseña'], contraseña)):
        print(contraseñaBD)
        session['Id'] = contraseñaBD['Id']
        session['Correo'] = contraseñaBD['Contraseña']
        session['Tipo'] = contraseñaBD['Tipo']
        print(session)
        #return redirect(url_for('vistaPacientes'))
        return jsonify({'redirect': url_for('vistaPacientes')})
    else:
        print("Error no se encontro el usuario")
        return jsonify ({'mensaje': 'Error, el usuario o contraseña son incorrectas', 'correo': correo, 'contraseña': contraseña})    
"""
if __name__ == "__main__":
    app.run()