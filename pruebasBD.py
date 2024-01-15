import dao, daoUsuario, daoDoctor,daoPacientes
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

#resultado = daoPacientes.registrarPaciente("Luis Jose Mejia Ramos","7372448796","1998-01-07","hombre","1")
resultado = daoPacientes.buscarPaciente(4,8)

print(resultado)
#print(check_password_hash(resultado[0]['contraseña'], "1234"))
