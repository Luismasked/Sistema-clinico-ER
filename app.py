from flask import Flask,render_template,redirect,url_for,request,session
import secrets
import dao

app = Flask(__name__)

#Se Genera de manera random un token para el login
app.secret_key = secrets.token_hex(32 // 2)

@app.route('/')
def index():
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
        if(len(dao.registrarUsusarioD(telefono,correo,contraseña)) !=0):
            return redirect(url_for('login'))
        


@app.route('/ingresar',methods=["GET", "POST"])
def ingresar():
    if request.method == "POST":
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        if(len(dao.buscarUsusario(correo,contraseña)) !=0):
            session['correo'] = correo
        return  render_template('vistapacientes.html',title="Pacientes", nombre="nombre")



if __name__ == "__main__":
    app.run(debug=True)