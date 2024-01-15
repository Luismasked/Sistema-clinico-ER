from flask import Flask,render_template,redirect,url_for,request,session, jsonify
import secrets
import dao, daoUsuario, daoDoctor, daoPacientes
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
        return "<h1>ya tas logeado </h1>" 
    else:
        return render_template('login.html',title="Inicio-Login")

@app.route('/vistaPacientes')
def vistaPacientes():
    if 'correo' in session:
        listapacientes = daoPacientes.buscarPaciente(session["idDoctor"])
        datos = {
            "listapacientes" : listapacientes,
            "nombre" : session['nombre'],
            "idDoctor" : session['idDoctor']
                }
        #poner codigo para poner los pacientes
        return render_template('vistapacientes.html',title="Pacientes", datos = datos)
    else:
        return redirect(url_for('index'))

@app.route('/verRegistroPaciente/')
def verRegistroPaciente():
    print(session)
    datos = {
            "idDoctor" : session['idDoctor'],
            "nombre" : session['nombre']
                }
    return render_template('registroPaciente.html',title="Registro Paciente",datos = datos)

@app.route('/verLogin/')
def verLogin():
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

@app.route('/vistaEditarPaciente/<idPaciente>')
def vistaEditarPaciente(idPaciente):
    datosPaciente = daoPacientes.buscarPaciente(session['idDoctor'],idPaciente)[0]
    datos ={'idDoctor' : datosPaciente['idDoctor'],'idPaciente' : datosPaciente['id'],'nombre' : datosPaciente['nombre'],
            'genero' : datosPaciente['genero'], 'telefono': datosPaciente['telefono'],'fechaDeNacimiento' : datosPaciente['fechaDeNacimiento']}
    return render_template('editarPaciente.html',title="Editar paciente", datos = datos)

@app.route('/editarPaciente', methods = ["POST"])
def editarPaciente():
    if request.method == "POST":
        nombre = request.form['nombre']
        genero = request.form['genero']
        telefono = request.form['telefono']
        fechaDeNacimiento = request.form['fecha']
        idPaciente = request.form['idPaciente']
        if(daoPacientes.editarPaciente(nombre,telefono,fechaDeNacimiento,genero,idPaciente)):
            return redirect(url_for('vistaPacientes'))
        else:
            return "error al actualizar"


@app.route('/registroPaciente',methods=["POST"])
def registroPaciente():
    if request.method == "POST":
        nombre = request.form['nombre']
        genero = request.form['genero']
        telefono = request.form['telefono']
        fecha = request.form['fecha']
        idDoctor = request.form['idDoctor']
        print(nombre)
        print(genero)
        print(telefono)
        if(daoPacientes.registrarPaciente(nombre,telefono,fecha,genero,idDoctor)):
            return redirect(url_for('vistaPacientes'))
        else:
            return redirect(url_for('verRegistroPaciente'))

@app.route('/vistaRegistrarUsuarioDoctor/')
def vistaRegistrarUsuarioDoctor():
    return render_template('registroUsuarioDoctor.html',title="Registrar")



@app.route('/vistaRegistrarDoctor')
def vistaRegistrarDoctor():
    print(session)
    if 'error' in session:
        datos = {
            "idUsuario" : session['idUsusarioDoctor'],
            "error" : session['error']
                }
    else:
        datos = {"idUsuario" : session['idUsusarioDoctor']}
    return render_template('registroDoctor.html',title="Registrar", datos = datos)

@app.route('/registroDoctor',methods=["POST"])
def registroDoctor():
    if request.method == "POST":
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        fecha = request.form['fecha']
        ubicacion = request.form['ubicacion']
        id = request.form['idUsuario']
        print(id," ",nombre," ",cedula," ",fecha," ",ubicacion)
        if(len(daoDoctor.registrarDoctor(nombre,cedula,fecha,ubicacion,id)) !=0):
            return redirect(url_for('index'))
        else:
            return "Error"
        

@app.route('/cambiarStatusPaciente',methods=["POST"])
def cambiarStatusPaciente():
    if request.method == "POST":
        
        idPaciente = request.form['idPaciente']
        idDoctor = request.form['idDoctor']

        if(len(daoPacientes.cambiarStatusPaciente(idPaciente)) !=0):
            pacientes = daoPacientes.buscarPaciente(idDoctor)
            return jsonify(pacientes)
        else:
            return jsonify("0")
        #if(len(daoUsuario.registrarUsusarioD(telefono, correo, password)) !=0):
        #    id = daoUsuario.buscarUsusario(correo)[0]["id"]
        #    session['idUsusarioDoctor'] = id
        #    return redirect(url_for('vistaRegistrarDoctor')) 


@app.route('/registroUsuarioDoctor',methods=["POST"])
def registro():
    if request.method == "POST":
        correo = request.form['correo']
        telefono = request.form['telefono']
        contraseña = request.form['contraseña']
        password = generate_password_hash(contraseña)
        if(len(daoUsuario.registrarUsusarioD(telefono, correo, password)) !=0):
            id = daoUsuario.buscarUsusario(correo)[0]["id"]
            session['idUsusarioDoctor'] = id
            return redirect(url_for('vistaRegistrarDoctor'))        


@app.route('/ingresarUsuario', methods=["POST"])
def ingresarUsuario():
    
    if request.method == "POST":
        try:
            correo = request.form['email']
            contraseña = request.form['password']
            contraseñaBD = daoUsuario.buscarUsusario(correo)[0]
            print(contraseñaBD)
            print(type(contraseñaBD))
            if(check_password_hash(contraseñaBD['contraseña'], contraseña)):
                doctor = daoDoctor.buscarDoctorPorCorreoUsuario(correo)
                if(len(doctor) !=0):
                    session['correo'] = correo
                    session['idDoctor'] = doctor[0]['id']
                    session['nombre'] = doctor[0]['nombre']
                    return redirect(url_for('vistaPacientes'))
                else:
                    session['idUsusarioDoctor'] = contraseñaBD['id']
                    session['error'] = "Falta registrar los datos del doctor"
                    return redirect(url_for('vistaRegistrarDoctor'))
            else:
                print("IF Error no se encontro el usuario")
                return  render_template('login.html',title="Error")
        except:
            print("Try Error no se encontro el usuario")
            return  render_template('login.html',title="Error")
    else:
        return  render_template('login.html',title="Error")

@app.route("/cerrarSesion")
def cerrarSesion():
    session.clear()
    return redirect(url_for('index'))

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
    app.run(debug=True)