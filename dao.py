from bd import obtener_conexion
import pymysql

def buscarPaciente(id):
    try:    
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            if id == "*":
                print(id)
                cursor.execute("SELECT * FROM pacientes")
            else:
                cursor.execute("SELECT * FROM pacientes WHERE Id = %s",(id))
            info = cursor.fetchall()
        conexion.close()
        return info
    except pymysql.Error as error:
        print("Error al conectar a la base de datos"+ error)
        return error

def buscarUsusario(correo):
    try:    
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario WHERE correo = %s",(correo))
            info = cursor.fetchall()
        conexion.close()
        return info
    except pymysql.Error as error:
        print("Error al conectar a la base de datos"+ error)
        return None

def registrarUsusarioD(telefono,correo,contraseña,tipo = 1):
    try:    
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO usuario (Telefono, Correo, Contraseña, Tipo) VALUES (%s, %s, %s, %s)",(telefono,correo,contraseña,tipo))
        conexion.commit()
        conexion.close()
        return [1]
    except pymysql.Error as error:
        print("Error al conectar a la base de datos"+ error)
        return error

def registrarPaciente(nombre,telefono,genero):
    try: 
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO pacientes (`Nombre`, `Genero`, `Telefono`) VALUES (%s, %s, %s)"
            cursor.execute(sql,(nombre,genero,telefono))
            conexion.commit()
        conexion.close()
        return ['1']
    except:
        return []