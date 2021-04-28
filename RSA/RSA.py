#En primer lugar se importan los recursos
from cryptography.fernet import Fernet

#Esta funcion permite guardar la clave

def key_generate():
    clave = Fernet.generate_key()
    with open("clave.key","wb") as archivo_clave:
        archivo_clave.write(clave)

#Esta funcion permite cargar la clave

def cargar_clave():
    return open("clave.key","rb").read()

#_________________proceso de encriptado_________________

#se crea y se guarda la clave
key_generate()

#cargamos la clave 
clave = cargar_clave()

#Aqui se escribe el mensaje a encriptar
print("Escriba el mensaje que desea encriptar")
mensaje = input().encode()

#iniciamos "fernet"
f = Fernet(clave)

#Encriptamos el mensaje
encriptado = f.encrypt(mensaje)

#muestra del mensaje encriptado
print ("Este es el mensaje encriptado, espero nadie lo pueda leer :) ")
print (encriptado)

#_______________Proceso de desencriptado________________

#Desencriptar mensaje 
desencriptado = f.decrypt(encriptado)

#Se debe imprimir el mensaje original
print("Este es el mensaje luego de desencriptar, funciona?")
print(desencriptado)