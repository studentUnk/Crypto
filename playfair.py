'''
tabla = Matriz base para encriptar
mensaje = Texto a encriptar
c_adicional = Caracter para agregar al final si texto es impar o dos letras
 adyacentes son iguales
encriptar = 1 => Encriptar || 0 => Desencriptar
'''
def encriptarDesencriptar(tabla, mensaje, c_adicional, encriptar = 1):
 pos = 0
 mensaje_ed = "" # Mensaje encriptado o desencriptado
 while(pos < len(mensaje)):
  c1 = ""
  c2 = "" # Caracteres par asignacion a mensaje
  c1_pos = [] # Posicion de caracteres [fila,columna]
  c2_pos = []
  c1_esM = False # Variable para verificar mayuscula y convertir
  c2_esM = False
  subString = "" # Variable a insertar si las posiciones no son contiguas

  while(pos < len(mensaje)): # Verificar que es un caracter o digito
   if(validar_caracter(mensaje[pos])):
    break
   else:
    mensaje_ed = mensaje_ed + mensaje[pos] # Copiar caracter sin encriptar
   pos = pos+1

  if(pos >= len(mensaje)):
   break # Terminar ciclo

  if(mensaje[pos].isupper()):
   c = mensaje[pos].lower()
   c1_pos = encontrar_posicion(tabla,c) # Posicion del primer caracter
   c1_esM = True
  else:
   c1_pos = encontrar_posicion(tabla,mensaje[pos]) # Posicion del primer caracter
  if((pos+1) < len(mensaje)): # Posicion del segundo caracter
   pos1 = pos # Variable para validar caracteres iguales en posiciones adyacentes
   pos = pos+1 # Siguiente caracter
   while(pos < len(mensaje)):
    if(validar_caracter(mensaje[pos])):
     break
    else:
     subString = subString + mensaje[pos] # Copiar caracter sin encriptar
    pos = pos+1
   if(pos >= len(mensaje)):
    c2_pos = encontrar_posicion(tabla,c_adicional) # Agregar 'h' al final para completar proceso final
   else:
    if(mensaje[pos].isupper()):
     c = mensaje[pos].lower()
     c2_pos = encontrar_posicion(tabla,c) # Buscar posicion en minuscula
     c2_esM = True
    else:
     c2_pos = encontrar_posicion(tabla,mensaje[pos])
    
   if((c1_pos[0] == c2_pos[0]) and (c1_pos[1] == c2_pos[1]) and (pos1+1) == pos): # Misma Posicion
    c2_pos = encontrar_posicion(tabla,c_adicional) # Intercambiar por 'h'
   else:
    pos = pos+1 # Aumentar una posicion para encriptar en siguiente ciclo
  else:
   c2_pos = encontrar_posicion(tabla,c_adicional) # Agregar 'h' al final si es impar

  if(c1_pos[0] == c2_pos[0]): # Mover derecha
   c1,c2 = mover_derecha(tabla, len(tabla[0]), c1_pos, c2_pos, encriptar)
  elif(c1_pos[1] == c2_pos[1]): # Mover abajo
   c1,c2 = mover_derecha(tabla, len(tabla), c1_pos, c2_pos, encriptar)
  else: # Mover diagonal
   c1,c2 = mover_diagonal(tabla, c1_pos, c2_pos)
   
  if(c1_esM): # Convertir a mayuscula
   c1 = c1.upper()
  if(c2_esM):
   c2 = c2.upper()
   
  if(len(subString) > 0):
   mensaje_ed = mensaje_ed + c1 + subString + c2
  else:
   mensaje_ed = mensaje_ed + c1 + c2

 if(encriptar == 0): # Desencriptar
  mensaje_ed = remover_caracter(mensaje_ed, c_adicional) # Remover caracter adicional
  
 return mensaje_ed
 
def mover_derecha(tabla, columnas, pos1, pos2, encriptar = 0):
 caracter_1 = ''
 caracter_2 = ''
 if(encriptar == 1):
  caracter_1 = tabla[pos1[0]][(pos1[1]+1)%columnas]
  caracter_2 = tabla[pos2[0]][(pos2[1]+1)%columnas]
 else:
  caracter_1 = tabla[pos1[0]][pos1[1]-1]
  caracter_2 = tabla[pos2[0]][pos2[1]-1]
 return caracter_1,caracter_2
 
def mover_abajo(tabla, columnas, pos1, pos2, encriptar = 0):
 caracter_1 = ''
 caracter_2 = ''
 if(encriptar == 1):
  caracter_1 = tabla[(pos1[0]+1)%columnas][pos1[1]]
  caracter_2 = tabla[(pos2[0]+1)%columnas][pos2[1]]
 else:
  caracter_1 = tabla[pos1[1]-1][pos1[0]]
  caracter_2 = tabla[pos2[1]-1][pos2[0]]
 return caracter_1,caracter_2

def mover_diagonal(tabla, pos1, pos2): 
 caracter_1 = ''
 caracter_2 = ''
 caracter_1 = tabla[pos1[0]][pos2[1]]
 caracter_2 = tabla[pos2[0]][pos1[1]]
 return caracter_1,caracter_2
 
def remover_caracter(mensaje, caracter):
 pos = 0
 while(pos < len(mensaje)):
  if(mensaje[pos] == caracter and pos > 0):
   if((pos+1) == len(mensaje)): # Remover caracter al final
    mensaje = mensaje[0:pos]
   else:
    if(mensaje[pos-1] == mensaje[pos+1]): # Caracteres iguales
     if(validar_caracter(mensaje[pos-1]) and validar_caracter(mensaje[pos+1])): #Validar extremos
      mensaje = mensaje[0:pos] + mensaje[pos+1:len(mensaje)] # Remover caracter
   
  pos = pos+1
 return mensaje  
  
def encontrar_posicion(tabla, caracter):
 i = 0 # Posicion fila
 for f in tabla:
  j = 0 # Posicion columna
  for c in f:
   if(c == caracter):
    return [i,j]
   j = j+1
  i = i+1

def validar_caracter(caracter):
 return caracter.isalpha() or caracter.isdigit()
 
def existe_caracter(tabla, fila, caracter):
 for t in tabla:
   for t_n in t: # Ciclo para validar que no exista caracter en la tabla
    if(t_n == caracter):
     return True
 for f in fila: # Ciclo para validar que no exista caracter en la fila actual
  if(f == caracter):
   return True
 return not validar_caracter(caracter)

def completar_tabla(tabla, columnas, fila, base):
 for f in base:
  for c in f:
   if(not existe_caracter(tabla, fila, c)): # Validar que caracter no exista en tabla
    if(len(fila) == columnas):
     tabla.append(fila) # Agregar nueva fila
     fila = []
    fila.append(c) # Agregar caracter a la fila
 if(len(fila) == columnas):
  tabla.append(fila) # Agregar ultima fila
 return tabla

def crear_tabla_clave(clave, columnas, base):
 tabla = []
 fila = []
 for cl in clave:
  if(not existe_caracter(tabla, fila, cl)):
   fila.append(cl) # Agregar caracter a la fila
  if(len(fila) == columnas):
   tabla.append(fila) # Agregar fila a la tabla
   fila = [] # Vaciar fila
 tabla = completar_tabla(tabla, columnas, fila, base)
 return tabla
  
  
clave = "personal35"
tabla_base = [
	['a','b','c','d','e','f'],
	['g','h','i','j','k','l'],
	['m','n','o','p','q','r'],
	['s','t','u','v','w','x'],
	['y','z','0','1','2','3'],
	['4','5','6','7','8','9']
	]
columnas = 6
tabla_clave = crear_tabla_clave(clave, columnas, tabla_base)
print(tabla_clave)

mensaje = "Encripta este mensaje 123456??"

#mensajeE = encriptar(tabla_clave,mensaje)
mensajeE = encriptarDesencriptar(tabla_clave,mensaje,'h',1)
print (mensajeE)

#mensajeD = desencriptar(tabla_clave, mensajeE)
mensajeD = encriptarDesencriptar(tabla_clave, mensajeE,'h',0)
print(mensajeD)
