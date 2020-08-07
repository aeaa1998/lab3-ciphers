import hmac
import hashlib
from hack import main

def get_signature(secret, message):
    return hmac.new(secret.encode("iso-8859-1"), msg=message.encode("iso-8859-1"),
                    digestmod=hashlib.sha256).hexdigest().upper()


secretKey = 'CC3078'

message = "Cifrado de informacion seccion 10"


print("INCISO 1.a")
print("Mensaje Cifrado de informacion seccion 10 ", get_signature(secretKey, message))
print("\n\n")
print("INCISO 1.b")
secretKey = 'MAC'

message = "La implementacion de este ejercicio fue sencilla"

print("La implementacion de este ejercicio fue sencilla ", get_signature(secretKey, message))

print("INCISO 2")
main()

