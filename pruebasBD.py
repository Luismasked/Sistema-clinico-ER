import dao
from werkzeug.security import generate_password_hash, check_password_hash
#print(dao.buscarUsusario("luismasked98@gmail.com","1234"))
password= "1234"
encript = generate_password_hash(password)
print(encript)
try:
    dao.registrarUsusarioD("7421130678","luismasked98@gmail.com",encript,"1")
except Exception as e: 
    print("error", e)