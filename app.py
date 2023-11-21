from flask import Flask,render_template,redirect,url_for,request,session
app = Flask(__name__)

app.secret_key = '_5#y2L"F4Q8zxec]/'

@app.route('/')
def index():
    return render_template('index.html',title="Inicio")

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/ingresar',methods=["GET", "POST"])
def ingresar():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        session['email'] = email
        return  render_template('vistapacientes.html')



if __name__ == "__main__":
    app.run(debug=True)