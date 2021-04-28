def encriptar(clave, mensaje):
 mensajeEncriptado = ""
 for m in mensaje:
  if(m.isalpha()): # El texto es del alfabeto
   mm = ord(m)
   if((mm >= 97 and mm <= 122)or(mm >= 65 and mm <= 90)):
    if(m.islower()):
     # a-z = 97-122 en ASCII
     mm -= 97 # Reducir a 0 para obtener modulo con facilidad
     mm += clave # Mover espacios en base a la clave
     mm %= 26 # Retornar residuo a base 26
     mm += 97 # Regresar numero a la minima posicion posible
    else:
     # A-Z = 65-90 en ASCII
     mm -= 65
     mm += clave
     mm %= 26
     mm += 65
   mensajeEncriptado += chr(mm) # Covertir ASCII a texto
  elif(m.isdigit()): # El texto es un numero
   # 0-9 = 48-57 en ASCII
   mm = ord(m)
   mm -= 48
   mm += clave
   mm %= 10
   mm += 48
   mensajeEncriptado += chr(mm)
  else:
   mensajeEncriptado += m
 return mensajeEncriptado
	
def desencriptar(clave, mensaje):
 mensajeDesencriptado = ""
 for m in mensaje:
  if(m.isalpha()): # El texto es del alfabeto
   mm = ord(m)
   if((mm >= 97 and mm <= 122)or(mm >= 65 and mm <= 90)):
    if(m.islower()):
     # a-z = 97-122 en ASCII
     mm -= 97 # Reducir a 0 para obtener modulo con facilidad
     mm -= clave # Mover espacios en base a la clave
     mm %= 26 # Retornar residuo a base 26
     if(mm < 0):
      mm = 25+mm # Movimiento de derecha a izquierda
     mm += 97 # Regresar numero a la minima posicion posible
    else:
     # A-Z = 65-90 en ASCII
     mm -= 65
     mm -= clave
     mm %= 26
     if(mm < 0):
      mm = 25+mm
     mm += 65
   mensajeDesencriptado += chr(mm) # Covertir ASCII a texto
  elif(m.isdigit()): # El texto es un numero
   # 0-9 = 48-57 en ASCII
   mm = ord(m)
   mm -= 48
   mm -= clave
   mm %= 10
   if(mm < 0):
    mm = 10+mm
   mm += 48
   mensajeDesencriptado += chr(mm)
  else:
   mensajeDesencriptado += m
 return mensajeDesencriptado
 

clave = 70 ## cantidad de espacios a mover
mensaje = "Encripta este mensaje 123456??"

mensajeE = encriptar(clave,mensaje)
print(mensajeE)

mensajeD = desencriptar(clave, mensajeE)
print(mensajeD)
