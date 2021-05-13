def encriptar(clave, mensaje):
 mensajeE = ""
 clave = abs(clave) # Valor absoluto numeros negativos
 rail = [] # Variable de los rieles
 for i in range(0,clave):
  rail.append("") # Iniciar arreglo con string
 pos = 0
 abajo = True
 for i in range (0, len(mensaje)):
  rail[pos] = rail[pos] + mensaje[i] # Agregar caracter a rail
  if(abajo): # Diagonal izquierda
   pos = pos+1
   if(pos == clave):
    pos = clave-2
    abajo = False
  else: # Diagonal derecha
   pos = pos-1
   if(pos < 0):
    pos = 1
    abajo = True
 for r in rail: # Agregar rail al nuevo mensaje
  mensajeE = mensajeE + r
 return mensajeE
   
def desencriptar(clave, mensaje):
 mensajeD = ""
 clave = abs(clave) # Valor absoluto numeros negativos
 rail = [] # Variable de los rieles
 n_espacios = 0 # El numero por espacio
 caracter_rail = [] # Contar caracter agregado al rail
 
 for i in range(0,clave):
  rail.append("") # Iniciar arreglo con string
  n_espacios = n_espacios + 2 # Numeros impares internos por letra
  caracter_rail.append(0) # Inicializar arreglo con 0
 
 n_espacios = n_espacios - 2 # Ajustar espacios
 rail_0 = [] # Posiciones del primer rail
 pos = 0 # Posicion inicial
 tam_M = len(mensaje) # Tamano del mensaje
 while(pos < tam_M):
  rail_0.append(pos) # Agregar posicion
  pos = pos + n_espacios
 
 pos_i = clave-1 # Tamano de la clave
 cantidad = 0 # Cantidad caracteres por rail
 for i in range(0,clave): # Crear rieles
  previo = cantidad # Posicion previa
  if(i == 0 or i == pos_i):
   cantidad = cantidad + len(rail_0)
  else:
   cantidad = cantidad + ((len(rail_0)-1)*2)
   if((rail_0[-1]+i)<tam_M):
    cantidad = cantidad + 1 # Diagonal izquierda
   if((rail_0[-1]+n_espacios-i)<tam_M):
    cantidad = cantidad + 1 # Diagonal derecha
  rail[i] = rail[i] + mensaje[previo:cantidad] # Agregar substring al rail
 
 pos = 0 # Posicion inicial
 pos_rail = 0 # Variable para obtener caracter del rail
 abajo = True # Incrementar o reducir
 while(pos < tam_M):
  mensajeD = mensajeD + rail[pos_rail][caracter_rail[pos_rail]] # Obtener caracter
  caracter_rail[pos_rail] = caracter_rail[pos_rail]+1 # Incrementar al siguiente caracter
  if(abajo):
   if(pos_rail == pos_i):
    abajo = False #Invertir direccion
    pos_rail = pos_rail-1
   else:
    pos_rail = pos_rail+1 # Incrementar
  else:
   if(pos_rail == 0):
    abajo = True #Invertir direccion
    pos_rail = pos_rail+1
   else:
    pos_rail = pos_rail-1 # Reducir
  pos = pos+1
 return mensajeD 
 
clave = 3 # cantidad de rails debe ser mayor que 1 y menor que el tamano del mensaje
mensaje = "Encripta este mensaje 123456??"

mensajeE = encriptar(clave,mensaje)
print(mensajeE)

mensajeD = desencriptar(clave, mensajeE)
print(mensajeD)
