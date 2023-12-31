import dao, daoUsuario
from werkzeug.security import generate_password_hash, check_password_hash
#print(dao.buscarUsusario("luismasked98@gmail.com","1234"))
<<<<<<< HEAD
x = dao.buscarUsusario("luismasked97@gmail.com")
print(x[0]['Id'])
=======
#password= "1234"
#encript = generate_password_hash(password)
#print(encript)
"""
try:
    resultado = daoUsuario.registrarUsusarioD("7755662233", "casdasd@gmail.com", "password")
    print(resultado)
except Exception as e: 
    print("error", e)
"""
datos = {"dato1" : "hola",
        "dato2" : "hola 2" }
print(datos)
>>>>>>> Salvala
