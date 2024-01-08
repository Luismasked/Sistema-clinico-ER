from bd import obtener_conexion
import pymysql

def buscarUsusario(correo):
    try:    
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario WHERE correo = %s AND status = '1'",(correo))
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
            cursor.execute("INSERT INTO usuario (telefono, correo, contraseña, tipo) VALUES (%s, %s, %s, %s)",(telefono,correo,contraseña,tipo))
        conexion.commit()
        conexion.close()
        return [1]
    except pymysql.Error as error:
        print("Error al conectar a la base de datos"+ error)
        return error

