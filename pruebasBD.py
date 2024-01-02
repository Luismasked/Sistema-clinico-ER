import dao, daoUsuario, daoDoctor
from werkzeug.security import generate_password_hash, check_password_hash
#print(dao.buscarUsusario("luismasked98@gmail.com","1234"))
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

resultado = daoDoctor.buscarDoctorPorCorreoUsuario("luismasked98@gmail.com")

if(len(resultado) !=0):
    print(resultado[0])
else:
    print("No hay usuario")
#print(check_password_hash(resultado[0]['contraseña'], "1234"))
