'''
Ejemplo basico de RSA encriptando en base a codigo ASCII (este sera el rango de opciones para el mensaje).
Este ejemplo no es comparable a un codigo real RSA que sea seguro, ya que el calculo
de primos no es lo suficientemente grande (p>1024(bits))

El codigo esta basado principalmente en la informacion suministrada en "RSA Algorithm"
https://www.di-mgt.com.au/rsa_alg.html

'''
import random

def encriptar(mensaje,n,llave_publica):
 mensajeE = ""
 for m in mensaje:
  num = ord(m) # Convertir a entero
  c = pow(num,llave_publica)%n # Encriptar
  formato = "{0:0" + str(4) +"x}" # Formato de salida en hexadecimal
  mensajeE = mensajeE + formato.format(c) # Convertir valor encriptado entero a hexadecimal
 return mensajeE
 
def desencriptar(mensaje,n,llave_privada):
 mensajeD = ""
 for i in range(0,len(mensaje),4):
  num = int(mensaje[i:i+4],16) # Convertir hexadecimal a entero
  m = pow(num,llave_privada)%n # Desencriptar
  mensajeD = mensajeD + chr(m) # Convertir numero a ASCII
 return mensajeD

def encontrar_e_Fermat(numerosFermat,p,q):
 for nF in numerosFermat:
  if(p%nF != 1 and q%nF != 1): # Determinar si es multiplo del numero fermat
   return nF # Si no es multiplo devolver numero e elegido

def encontrar_exponente_bruta(e,phi):
 d = 2 # d > 1
 while (d < phi):
  if((e*d)%phi == 1):
   return d
  d = d+1
 return 0

'''
'minimo' es el valor minimo para el rango de valores del mensaje,
por lo tanto, si R(0,minimo) -> n>=minimo
'''
def crear_claves(minimo):
 n = 0
 p = 0
 q = 0
 while(n < minimo):
  p = primos_30[random.randint(0,len(primos_30)-1)]
  q = primos_30[random.randint(0,len(primos_30)-1)]
  n = p*q # clave publica
 phi = (p-1)*(q-1) # Funcion Euler (eulier totient function)
 e = encontrar_e_Fermat(numerosFermat,p,q) # clave para encriptar 
 d = encontrar_exponente_bruta(e,phi) # clave privada para desencriptar  
 return [n,e,d]
 

# ------------------------------------------------
# Datos iniciales para encriptar y desencriptar
numerosFermat = [3,5,17,257,65537]
primos_30 = [2,3,5,11,13,17,19,23,29,31,
             37,41,43,47,53,59,61,67,71,73,
             79,83,89,97,101,103,107,109,113,127]
claves = crear_claves(255)
mensaje = "Encripta este mensaje 123456??"
# ------------------------------------------------

print("Mensaje= " + mensaje)

mensajeEncriptado = encriptar(mensaje,claves[0],claves[1])
print("Mensaje encriptado= " + mensajeEncriptado)

mensajeDesencriptado = desencriptar(mensajeEncriptado,claves[0],claves[2])
print("Mensaje desencriptado=  " + mensajeDesencriptado)
