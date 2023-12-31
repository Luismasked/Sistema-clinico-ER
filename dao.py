from bd import obtener_conexion
import pymysql

<<<<<<< HEAD
def buscarUsusario(correo):
=======
def buscarPaciente(id):
>>>>>>> Salvala
    try:    
        conexion = obtener_conexion()
        info = []
        with conexion.cursor() as cursor:
<<<<<<< HEAD
            cursor.execute("SELECT * FROM usuario WHERE correo = %s",(correo))
=======
            if id == "*":
                print(id)
                cursor.execute("SELECT * FROM pacientes")
            else:
                cursor.execute("SELECT * FROM pacientes WHERE id = %s",(id))
>>>>>>> Salvala
            info = cursor.fetchall()
        conexion.close()
        return info
    except pymysql.Error as error:
        print("Error al conectar a la base de datos"+ error)
<<<<<<< HEAD
        return info
=======
        return error
>>>>>>> Salvala


def registrarPaciente(nombre,telefono,genero):
    try: 
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO pacientes (`nombre`, `genero`, `telefono`) VALUES (%s, %s, %s)"
            cursor.execute(sql,(nombre,genero,telefono))
            conexion.commit()
        conexion.close()
        return ['1']
    except:
        return []