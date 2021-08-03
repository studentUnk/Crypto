'''
Codigo basado en "ElGamal Encryption Algorithm"
https://www.geeksforgeeks.org/elgamal-encryption-algorithm/

Applied Cryptography - Bruce Schneir -> Exponenciacion modular
'''

import random
import math

def encriptar(mensaje,q,h,g):
 mensajeEncriptado = []
 
 k = generar_clave(q) # Clave privada -> en base a numero aleatorio que sea primo
 s = potencia(h,k,q)  # Secreto compartido
 p = potencia(g,k,q) 
 
 for i in range(0, len(mensaje)):
  mensajeEncriptado.append(mensaje[i])
 
 for i in range(0,len(mensajeEncriptado)):
  mensajeEncriptado[i] = s*ord(mensajeEncriptado[i]) # Encriptar mensaje
 
 return mensajeEncriptado, p

def desencriptar(mensaje,p,clave,q):
 mensajeDesencriptado = []
 
 h = potencia(p,clave,q)
 for i in range(0,len(mensaje)):
  mensajeDesencriptado.append(chr(int(mensaje[i]/h)))
 
 return mensajeDesencriptado

def gcd(a,b):
 if(a < b): # Ajustar orden de comparacion
  return gcd(b,a)
 elif(a%b == 0): # Es divisor mas grande -> g.c.d
  return b
 else:
  return gcd(b,a%b) # 'b' no es divisor de 'a' se obtiene modulo y se invierte orden

# Exponenciacion modular -> Applied Cryptography - Bruce Schneir
def potencia(base,exponente,modulo):
 resultado = 1
 y = base
 while(exponente>0):
  if(exponente & 1 > 0):
   resultado = (resultado*y)%modulo
  exponente = exponente >> 1  
  y = (y*y)%modulo
 return resultado

def generar_clave(q):
 clave = random.randint(pow(10,20),q)
 while(gcd(q,clave)!=1): # Hallar numero que sea coprimo
  clave = random.randint(pow(10,20),q)
 return clave

# -------------------------------------------
# Generacion de claves
q = random.randint(pow(10,20),pow(10,50)) # Numero q perteneciente al grupo Fq
g = random.randint(2,q) # Numero aleatorio del grupo Fq -> Clave privada
clave = generar_clave(q) # Clave privada
h = potencia(g,clave,q) # Clave publica
# -------------------------------------------

mensaje = "Encripta este mensaje 123456??"
print ("Mensaje= " + mensaje)

mensajeEncriptado,p = encriptar(mensaje,q,h,g)
print ("Mensaje encriptado=" , end=" ")
for m in mensajeEncriptado:
 print (m,end="")
print()
mensajeDesencriptado = desencriptar(mensajeEncriptado,p,clave,q)
print ("Mensaje desencriptado=", end=" ")
print (''.join(mensajeDesencriptado))
