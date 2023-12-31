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
                cursor.execute("SELECT * FROM pacientes WHERE id = %s",(id))
            info = cursor.fetchall()
        conexion.close()
        return info
    except pymysql.Error as error:
        print("Error al conectar a la base de datos"+ error)
        return error


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