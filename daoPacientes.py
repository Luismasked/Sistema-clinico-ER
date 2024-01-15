from bd import obtener_conexion
import pymysql

def buscarPaciente(idDoctor,idPaciente = "*" ):
    try:    
        conexion = obtener_conexion()
        info = []
        with conexion.cursor() as cursor:
            
            if idPaciente == "*":
                print(idDoctor)
                cursor.execute("SELECT * FROM pacientes WHERE idDoctor = %s AND status = '1' ",(idDoctor))
            else:
                cursor.execute("SELECT * FROM pacientes WHERE idDoctor = %s AND id = %s AND status = '1' ",(idDoctor, idPaciente))
            info = cursor.fetchall()
        conexion.close()
        return info
    except pymysql.Error as error:
        print("Error al conectar a la base de datos")
        return []


def registrarPaciente(nombre,telefono,fechaDeNacimiento,genero,idDoctor):
    try: 
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "INSERT INTO pacientes (`nombre`, `genero`,`fechaDeNacimiento`, `telefono`,`idDoctor`) VALUES (%s, %s, %s,%s,%s)"
            cursor.execute(sql,(nombre,genero,fechaDeNacimiento,telefono,idDoctor))
            conexion.commit()
        conexion.close()
        return True
    except:
        return False

def editarPaciente(nombre,telefono,fechaDeNacimiento,genero,idPaciente):
    try: 
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "UPDATE pacientes SET `nombre`= %s,`genero`= %s,`telefono`= %s, `fechaDeNacimiento`= %s WHERE id =%s"
            cursor.execute(sql,(nombre,genero,telefono,fechaDeNacimiento,idPaciente))
            conexion.commit()
        conexion.close()
        return True
    except:
        return False




def cambiarStatusPaciente(idPaciente):
    try: 
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            sql = "UPDATE pacientes SET `status`='0' WHERE id =%s"
            cursor.execute(sql,(idPaciente))
            conexion.commit()
        conexion.close()
        return ['1']
    except:
        return []