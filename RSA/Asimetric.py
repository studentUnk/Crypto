import Crypto
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#Liberrias y modulos a expotar para realizar el encriptado y conversion

random_generator = Crypto.Random.new().read #Se genera los numeros primos aleatorios

private_key = RSA.generate(2048, random_generator) #Se crea una llave privada con el numero aleatorio
public_key = private_key.publickey() #Se crea la lalve publica debido a la clave privada

private_key = private_key.exportKey(format='DER') #Se exportan las variables es un nuevo formato
public_key = public_key.exportKey(format='DER') 

private_key = binascii.hexlify(private_key).decode('UTF8') #Se codifican las llaves de binario a ascii
public_key = binascii.hexlify(public_key).decode('UTF8')

print ("ESTA ES SU LLAVE PRIVADA GENERADA DE MANERA ALEATORIA") #Se imprimen las dos llaves para observarlas
print (private_key) 
print ("ESTA ES SU LLAVE PUBLICA GENERADA DE MANERA ALEATORIA")
print (public_key)

#Proceso inverso para hacer crear la llave RSA, debido a que antes solo tenemos los llaves pero no son RSA

private_key = RSA.importKey(binascii.unhexlify(private_key)) # Se convierte nuevamente de ascii a binario
public_key = RSA.importKey(binascii.unhexlify(public_key))

message = "Hola mundo desde un string en texto plano"
message = message.encode() #Se codifica el mensaje

cipher = PKCS1_OAEP.new(public_key) #Se usa un objeto cipher para cifrar con la llave publica
encrypted_message = cipher.encrypt(message) #Se encripta

print ("ESTE ES SU MENSAJE ENCRIPTADO")
print (encrypted_message)

cipher = PKCS1_OAEP.new(private_key) #Se usa el objeto cipher para decifrar con la llave privada
message = cipher.decrypt(encrypted_message) #Se desencripta

print ("ESTE ES SU MENSAJE DESENCRIPTADO")
print (message)