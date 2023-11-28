import pymysql.cursors

def obtener_conexion():
    try:    
        return pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='bdsistemaclinico',
                                    cursorclass=pymysql.cursors.DictCursor)
    except pymysql.Error as error:
        print("Error al conectar a la base de datos"+ error)
        return None