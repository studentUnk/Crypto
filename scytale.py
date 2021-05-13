def encriptar(clave, mensaje):
 mensajeE = ""
 fila = []
 cantidad = 0 # Validar cantidad por mensaje
 tamM = len(mensaje) # Tamano del mensaje
 div = (int)(tamM/clave)
 mod = tamM%clave
 for i in range(0,clave):
  previo = cantidad # Valor previo para obtener substring
  cantidad = cantidad + div
  if(mod > 0):
   cantidad = cantidad + 1
   mod = mod - 1
  fila.append(mensaje[previo:cantidad]) # Agregar substring como fila
  
 columna = 0 # Obtener valor por columnas
 cantidad = 0
 while (cantidad < tamM):
  for i in range(0, len(fila)):
   if(columna < len(fila[i])): # Validar que fila contenga caracter
    cantidad = cantidad + 1 # Contar caracter agregado
    mensajeE = mensajeE + fila[i][columna] # Agregar caracter
  columna = columna + 1 # Siguiente columna
 return mensajeE  

def desencriptar(clave, mensaje):
 mensajeD = ""
 fila = [] # Recrear filas en mensaje encriptado
 for i in range(0,clave):
  fila.append("") # Inicializar filas
 cantidad = 0 # Conteo para caracteres en mensaje
 while(cantidad < len(mensaje)):
  fila[cantidad%clave] = fila[cantidad%clave] + mensaje[cantidad] # Agregar caracter a fila
  cantidad = cantidad + 1 # Sumar caracter agregado
 for f in fila:
  mensajeD = mensajeD + f # Agregar filas al mensaje
 return mensajeD

clave = 5 # cantidad de filas
mensaje = "Encripta este mensaje 123456??"

mensajeE = encriptar(clave,mensaje)
print(mensajeE)

mensajeD = desencriptar(clave, mensajeE)
print(mensajeD)
