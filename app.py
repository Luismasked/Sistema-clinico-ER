from flask import Flask,render_template,redirect,url_for,request,session,jsonify 
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import dao

app = Flask(__name__)

#Se Genera de manera random un token para el login
app.secret_key = secrets.token_hex(32 // 2)

@app.route('/')
def index():
    if 'correo' in session:
        return render_template('index.html',title="Inicio2",usuario=session['correo'])
    else:
        return render_template('index.html',title="Inicio")
@app.route('/login/')
def login():
    return render_template('login.html',title="Login")

@app.route('/vistaRegistrar/')
def vistaRegistrar():
    return render_template('registroUsuario.html',title="Registrar")

@app.route('/registro',methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        correo = request.form['correo']
        telefono = request.form['telefono']
        contraseña = request.form['contraseña']
        #encripto la contraseña para seguridad
        contraseña_encriptada = generate_password_hash(contraseña)
        if(len(dao.registrarUsusarioD(telefono,correo,contraseña_encriptada)) !=0):
            return redirect(url_for('login'))
        


@app.route('/ingresar',methods=["GET", "POST"])
def ingresar():
    if request.method == "POST":
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


if __name__ == "__main__":
    app.run()