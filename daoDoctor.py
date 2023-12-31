from bd import obtener_conexion
import pymysql

def registrarDoctor(nombre, cedula, fecha, ubicacion, idUsuario):
    try:    
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO doctores (nombre, cedula, fechaDeNacimiento, ubicacion, idUsuario) VALUES (%s, %s, %s, %s, %s)",(nombre,cedula,fecha,ubicacion,idUsuario))
        conexion.commit()
        conexion.close()
        return [1]
    except pymysql.Error as error:
        print("Error al conectar a la base de datos"+ error)
        return error