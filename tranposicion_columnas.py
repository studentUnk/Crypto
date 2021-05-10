def encriptar(clave, mensaje):
 columnas = [] # Mensaje en columnas
 pos = 0 # Variable para dividir el mensaje
 mensajeT = len(mensaje) # Tamano del mensaje
 mensajeE = "" # Nuevo mensaje encriptado
 while(pos < mensajeT):
  if((pos+clave) < mensajeT):
   columnas.append(mensaje[pos:pos+clave]) # Substring hasta el final de la clave
  else:
   columnas.append(mensaje[pos:mensajeT]) # Substring hasta el final del mensaje
  pos = pos+clave # Aumentar posicion segun la clave
 pos = len(columnas) # 
 for i in range(0,clave): # Ordenar segun cantidad de columnas
  for c in range(0,pos): # Obtener todas las filas
   if (i < len(columnas[c])): # Validar caracter existe
    mensajeE = mensajeE + columnas[c][i] # Alterar orden
 
 return mensajeE

def desencriptar(clave, mensaje):
 mensajeD = "" # Mensaje desencriptado
 mensajeT = len(mensaje) # Tamano del mensaje
 div = (int)(mensajeT / clave)  # Cantidad de filas
 mult = div * clave # Minima cantidad de filas
 cantidad = 0 # Caracteres agregados al mensaje
 for i in range(0,div+1):
  pos = i # Posicion de caracter a obtener
  mod = 0 # Validar modulo
  while(pos < mensajeT and cantidad < mensajeT):
   mensajeD = mensajeD + mensaje[pos]
   if(mod < (mensajeT%clave)):
    pos = pos + div + 1 # Incrementar segun cantidad de filas
    mod = mod + 1 # Incrementar modulo agregado
   else:
    pos = pos + div # Sumar minima cantidad de filas
   cantidad = cantidad + 1
 return mensajeD

clave = 7
mensaje = "Encripta este mensaje 123456??"

mensajeE = encriptar(clave,mensaje)
print (mensajeE)

mensajeD = desencriptar(clave,mensajeE)
print (mensajeD)
