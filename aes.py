'''
Algunas de las referencias que fueron usadas:

Announcing the ADVANCED ENCRYPTION STANDARD (AES)
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197.pdf

AES Example - Input (128 bit key and message)
https://www.kavaliro.com/wp-content/uploads/2014/03/AES.pdf

How to solve MixColumns
https://crypto.stackexchange.com/questions/2402/how-to-solve-mixcolumns

Rijndael MixColumns
https://en.wikipedia.org/wiki/Rijndael_MixColumns

Understanding AES Mix-Columns Transformation Calculation
https://www.angelfire.com/biz7/atleast/mix_columns.pdf
'''
import random
import codecs

def encriptar(mensaje,clave,caja_S,rc,matrizMult,expansion=128):
 # Cantidad de ciclos y tamano de la matriz por defecto (128 bits)
 ciclo = 10
 nk = 4
 maxCaracter = expansion/4 # Cantidad maxima de caracteres para la clave
 if(expansion == 192):
  ciclo = 12
  nk = 6
 elif(expansion == 256):
  ciclo = 14
  nk = 8
 # Texto a hexadecimal
 mensajeHex = completarBits(mensajeHexadecimal(mensaje),32) # 32 = 128 bits
 #mensajeHex = mensaje # El mensaje ya esta en hexadecimal
 
 #claveHex = mensajeHexadecimal(clave) # La clave ya esta en hexadecimal
 claveHex = clave
 if(len(claveHex) > maxCaracter):
  claveHex = claveHex[0:int(maxCaracter)]
 else:
  if(len(claveHex) != maxCaracter):
   print(len(claveHex))
   print(maxCaracter)
   return NULL
 # Hexadecimal a matriz 4x4
 #mensajeMatriz = matrizFilaInv(crearMatrizHex(mensajeHex)) # Mensaje en una matriz de 4x4
 claveMatriz = crearMatrizHex(claveHex,nk) # Clave en una matriz de 4x4
 matrizClaves = crearClavesTodas(claveMatriz,rc,caja_S,ciclo,nk=nk) # Matriz de matrices clave (128=10)
 
 mensajeEncriptado = ""
 for i in range(0,len(mensajeHex),32):
  mensajeMatriz = crearMatrizHex(mensajeHex[i:i+32])
  mensajeEncriptado = mensajeEncriptado + codificacion(mensajeMatriz, matrizClaves, caja_S, matrizMult)
 
 '''
 print("Matriz claves")
 for m in matrizClaves:
  print(m)
 print("------------------")
 '''
 
 return mensajeEncriptado
 
def desencriptar(mensaje,clave,caja_S,caja_S_inv,rc,matrizMult,expansion=128):
 # Cantidad de ciclos y tamano de la matriz por defecto (128 bits)
 ciclo = 10
 nk = 4
 maxCaracter = expansion/4 # Cantidad maxima de caracteres para la clave
 if(expansion == 192):
  ciclo = 12
  nk = 6
 elif(expansion == 256):
  ciclo = 14
  nk = 8
  
 #claveHex = mensajeHexadecimal(clave) 
 claveHex = clave # La clave ya esta en hexadecimal
 if(len(claveHex) > maxCaracter):
  claveHex = claveHex[0:int(maxCaracter)]
 else:
  if(len(claveHex) != maxCaracter):
   return NULL

 claveMatriz = crearMatrizHex(claveHex,nk) # Clave en una matriz de 4x4
 matrizClaves = crearClavesTodas(claveMatriz,rc,caja_S,ciclo,nk) # Matriz de matrices clave (128=10)
 
 mensajeDesencriptado = ""
 for i in range(0,len(mensaje),32):
  mensajeMatriz = crearMatrizHex(mensaje[i:i+32]) # Mensaje en una matriz de 4x4
  mensajeDesencriptado = mensajeDesencriptado + hexadecimalASCII(decodificacion(mensajeMatriz, matrizClaves, caja_S_inv, matrizMult))
  #mensajeDesencriptado = mensajeDesencriptado + decodificacion(mensajeMatriz, matrizClaves, caja_S_inv, matrizMult)
  
 return mensajeDesencriptado

def decodificacion(mensajeMatriz, clavesMatriz, caja_S, matrizMult):
 # Ronda 0
 
 matrizEstado = []
 #print("Mensaje Matriz")
 mensajeMatriz = matrizFilaInv(mensajeMatriz)
 #print(mensajeMatriz)
 
 #print("Ronda 0")
 #print("Entrada")
 #print(mensajeMatriz)
 #print(clavesMatriz[len(clavesMatriz)-1])
 
 #print("Clave")
 #print(clavesMatriz[len(clavesMatriz)-1])
 
 # Agregar ciclo de llave final
 for f in range(0,len(mensajeMatriz)):
  matrizEstado.append(xorFila(mensajeMatriz[f],clavesMatriz[len(clavesMatriz)-1][f])) # Agregar filas a matriz estado
  
 #print("Inv Round Key Value")
 #print(matrizEstado)
 #print(len(clavesMatriz))
 #print(clavesMatriz[len(clavesMatriz)-1])
 
 # Ciclo de rondas (128 = (9:1))
 for i in range(len(clavesMatriz)-2,0,-1): # La ultima ronda no se aplica multiplicacion
 
  #print("Ronda " + str(10-i))
 
  # Desplazar Filas (0,1,2,3)
  for f in range(1,len(matrizEstado)): # En 0 no hay desplazamiento
   matrizEstado[f] = desplazamientoDerecha(matrizEstado[f],f) # Desplazar 'f' posiciones a la izquierda
   
  #print("Inv ShiftRows")
  #print(matrizEstado)
   
  # Sustitucion por valores en caja_S_inv
  for f in range(0,len(matrizEstado)):
   matrizEstado[f] = sustitucionMatriz(caja_S,matrizEstado[f]) # Sustituir fila
  
  #print("Inv SubBytes")
  #print(matrizEstado)
  
  #print("Clave")
  #print(clavesMatriz[i])
  
  # Agregar ronda de llave del ciclo actual
  for f in range(0,len(matrizEstado)):
   matrizEstado[f] = xorFila(matrizEstado[f],clavesMatriz[i][f]) # Obtener nueva fila
  
  #print("Inv Round Key Value")
  #print(matrizEstado)
  
  # Mezclar columnas (multiplicacion en base a una matriz fija)
  matrizEstadoT = []
  for f in range(0,len(matrizEstado)):
   fila = []
   for c in range(0,len(matrizEstado[f])):
    fila.append("0")
   #matrizEstadoT.append(matrizEstado[f].copy())
   matrizEstadoT.append(fila)
   
  for f in range(0,len(matrizMult)):
   for c in range(0,len(matrizMult[f])):
    mult = multiplicarFilaColumnaHex(matrizMult,c,matrizEstado,f)
    #print(mult)
    xorM = ""
    for x in range(0,len(mult[0])):
     xorT = ""
     for m in range(0,len(mult)):
      if(m == 0):
       xorT = xorT + mult[m][x] # Obtener primer bit
      else:
       xorT = xor(xorT,mult[m][x]) # xor entre los valores de la multiplicacion
     xorM = xorM + xorT
    matrizEstadoT[f][c] = binarioHexadecimal(xorM)
  
  #print(matrizEstadoT)
  matrizEstado = matrizFilaInv(matrizEstadoT)
  #print(matrizEstado)
 
 
 # Desplazar Filas (0,1,2,3)
 for f in range(1,len(matrizEstado)): # En 0 no hay desplazamiento
  matrizEstado[f] = desplazamientoDerecha(matrizEstado[f],f) # Desplazar 'f' posiciones a la izquierda
   
 # Sustitucion por valores en caja_S_inv
 for f in range(0,len(matrizEstado)):
  matrizEstado[f] = sustitucionMatriz(caja_S,matrizEstado[f]) # Sustituir fila
  
 # Agregar ronda de llave del ciclo inicial
 for f in range(0,len(matrizEstado)):
  matrizEstado[f] = xorFila(matrizEstado[f],clavesMatriz[0][f]) # Obtener nueva fila
 
 #print(matrizEstado)
 
 mensajeDecodificado = matrizTexto(matrizFilaInv(matrizEstado))
 
 return mensajeDecodificado

def codificacion(mensajeMatriz, clavesMatriz, caja_S, matrizMult):
 # Ronda 0
 matrizEstado = []
 
 #print("CODIFICAR")
 #print("Clave")
 #print(clavesMatriz[0])
 #print("Inicio")
 mensajeMatriz = matrizFilaInv(mensajeMatriz)
 #print(mensajeMatriz)
 for i in range(0,len(mensajeMatriz)):
  matrizEstado.append(xorFila(mensajeMatriz[i],clavesMatriz[0][i])) # xor entre mensaje y clave sin ninguna ronda
 
 #print(matrizFilaInv(matrizEstado))
 
 #print("Round Key Value")
 #print(clavesMatriz[0])
 
 # Ciclo de rondas (128 = (1:10))
 for i in range(1,len(clavesMatriz)-1): # La ultima ronda no se aplica multiplicacion
  #print("Ronda " + str(i))
  #print(matrizFilaInv(matrizEstado))
  
  # Sustitucion por valores en caja_S
  for f in range(0,len(matrizEstado)):
   matrizEstado[f] = sustitucionMatriz(caja_S,matrizEstado[f]) # Sustituir fila
  
  #print("SubBytes")
  #print(matrizFilaInv(matrizEstado))
  
  # Desplazar Filas (0,1,2,3)
  for f in range(1,len(matrizEstado)): # En 0 no hay desplazamiento
   matrizEstado[f] = desplazamientoIzquierda(matrizEstado[f],f) # Desplazar 'f' posiciones a la izquierda
  
  #print("ShiftRows")
  #print(matrizFilaInv(matrizEstado))
  
  # Mezclar columnas (multiplicacion en base a una matriz fija)
  matrizEstadoT = []
  for f in range(0,len(matrizEstado)):
   fila = []
   for c in range(0,len(matrizEstado[f])):
    fila.append("0")
   #matrizEstadoT.append(matrizEstado[f].copy())
   matrizEstadoT.append(fila)
   
  for f in range(0,len(matrizMult)):
   for c in range(0,len(matrizMult[f])):
    mult = multiplicarFilaColumnaHex(matrizMult,c,matrizEstado,f)
    xorM = ""
    for x in range(0,len(mult[0])):
     xorT = ""
     for m in range(0,len(mult)):
      if(m == 0):
       xorT = xorT + mult[m][x] # Obtener primer bit
      else:
       xorT = xor(xorT,mult[m][x]) # xor entre los valores de la multiplicacion
     xorM = xorM + xorT
    matrizEstadoT[f][c] = binarioHexadecimal(xorM)
  
  matrizEstado = matrizFilaInv(matrizEstadoT)
  
  #print("MixColumns")
  #print(matrizFilaInv(matrizEstado))
  
  #print("Clave")
  #print(clavesMatriz[i])
  
  # Agregar ronda de llave del ciclo actual
  for f in range(0,len(matrizEstado)):
   matrizEstado[f] = xorFila(matrizEstado[f],clavesMatriz[i][f]) # Obtener nueva fila
  
  #print("Round Key Value")
  #print(matrizFilaInv(matrizEstado))
  #print(clavesMatriz[i][f])
 
 # Ronda final
 # Sustitucion por valores en caja_S
 for f in range(0,len(matrizEstado)):
  matrizEstado[f] = sustitucionMatriz(caja_S,matrizEstado[f]) # Sustituir fila
  
 #print("SubBytes")
 #print(matrizEstado)
 
 # Desplazar Filas (0,1,2,3)
 for f in range(1,len(matrizEstado)): # En 0 no hay desplazamiento
  matrizEstado[f] = desplazamientoIzquierda(matrizEstado[f],f) # Desplazar 'f' posiciones a la izquierda
 
 #print("ShiftRows")
 #print(matrizEstado)
  
 #print("MATRIZ FINAL")
 #print(clavesMatriz[len(clavesMatriz)-1])
 #print("Clave")
 #print(clavesMatriz[len(clavesMatriz)-1])
 
 # Agregar ronda de llave del ciclo final
 for f in range(0,len(matrizEstado)):
  matrizEstado[f] = xorFila(matrizEstado[f],clavesMatriz[len(clavesMatriz)-1][f]) # Obtener nueva fila
 
 #print("Salida")
 #print(matrizEstado)
 
 # Convertir matriz a string
 mensajeCodificado = matrizTexto(matrizFilaInv(matrizEstado))
 return mensajeCodificado  

def completarBits(hexadecimal,tam):
 n_hex = tam # Cantidad de hexadecimales por bloque
 mod = len(hexadecimal)%n_hex # Obtener modulo
 if(mod == 0):
  return hexadecimal
 #if(mod == (n_hex-1)):
  #hexadecimal = hexadecimal + "0"
 #hexadecimal = hexadecimal + "0A" # Final de linea
 hexadecimal = hexadecimal + "0D0A"
 mod = len(hexadecimal)%n_hex
 for i in range(mod,n_hex):
   hexadecimal = hexadecimal + "0" # Completar con 0 para obtener 16 hexadecimales
 return hexadecimal

def mensajeHexadecimal(mensaje):
 mensajeH = ""
 for m in mensaje:
  mensajeH = mensajeH + hex(ord(m)).lstrip("0x")
 return mensajeH
 
def enteroBinario(numero, tam = 4):
 formato = "{0:0" + str(tam) +"b}" # Formato de salida
 binario = formato.format(numero) # Convertir a binario
 return binario

def hexadecimalASCII(hexadecimal):
 return codecs.decode(hexadecimal,"hex").decode("ascii")

def hexadecimalBinario(texto, tam = 4):
 formato = "{0:0" + str(tam) +"b}" # Formato de salida
 binario = ""
 for t in texto:
  binario = binario + formato.format(int(t,16)) # Convertir a binario y agregar
 return binario

def hexEntero(hexadecimal):
 return int(hexadecimal,16)
 
def binarioEntero(binario):
 return int(binario,2)

def binarioHexadecimal(binario):
 hexadecimal = ""
 formato = "{0:x}"
 for i in range(0,len(binario),4):
  hexadecimal = hexadecimal + formato.format(binarioEntero(binario[i:i+4])) # Convertir binario a hexadecimal y agregar
 return hexadecimal
 
# Devuelve multiplicacion en un string binario
def multiplicarFilaColumnaHex(matriz1,fila,matriz2,columna):
 mult = []
 for i in range(0,len(matriz1[fila])):
  m1 = hexEntero(matriz1[fila][i]) # Convertir hexadecimal a entero
  m2 = hexEntero(matriz2[i][columna]) # Convertir hexadecimal a entero
  mr = enteroBinario(m1*m2,8)
  
  if(m1 > 1):
   if(m1==2 or m1==3): # Operacion matematica en G(8)
    m2bin = hexadecimalBinario(matriz2[i][columna])
    xorMult = "00011011" # Operacion xor en multiplicacion
   
    if(m1 == 2):
     # Desplazar izquierda
     izbin = m2bin[1:len(m2bin)] + '0' # Agregar 0 al final
     if(m2bin[0] == '1'):
      xorT = ""
      for j in range(0,len(izbin)):
       xorT = xorT + xor(izbin[j],xorMult[j])
      mr = xorT
     else:
      mr = izbin
    if(m1 == 3):
     # 3*x = (2 xor 1) * x = (2 * x) xor x
     # Desplazar izquierda
     izbin = m2bin[1:len(m2bin)] + '0' # Agregar 0 al final
     bin2 = ""
     if(m2bin[0] == '1'):
      for j in range(0,len(izbin)):
       bin2 = bin2 + xor(izbin[j],xorMult[j])
     else:
      bin2 = izbin
     #print(bin2)
     #print(m2bin)
     res = ""
     for j in range(0,len(m2bin)):
      res = res + xor(bin2[j],m2bin[j])
     mr = res
   else: # Reemplazo en base a tabla de sustitucion para G(8)
    # tablaGalois es usada como matriz global
    for j in range(2,len(tablasGalois)): # Tabla 0 = 2 | Tabla 1 = 3
     if(m1 == tablasGalois[j][0]): # Comparar si la tabla es la correcta
      mr = hexadecimalBinario(tablasGalois[j][1][hexEntero(matriz2[i][columna][0])][hexEntero(matriz2[i][columna][1])],4) # Agregar valor segun fila y columna
      #print(tablasGalois[j][1][hexEntero(matriz2[i][columna][0])][hexEntero(matriz2[i][columna][1])])
      break
         
  mult.append(mr)
  #print(matriz2[i][columna])
  
 #print(mult)
 return mult

def matrizTexto(matriz):
 texto = ""
 for f in matriz:
  for c in f:
   texto = texto + c # Copiar texto
 return texto
 
def xor(b1,b2):
 if(b1 != b2):
  return "1"
 return "0" 
 
def crearClavesTodas(matrizClave,rc,caja_S,ciclo=10,nk=4):
 matriz = [] # Todos los ciclos de la clave
 filasMatriz = [] # Todas las filas
 for f in matrizClave:
  filasMatriz.append(f) # Agregar fila
 for i in range(1,ciclo+1):
  filaT = []
  for c in filasMatriz[-1]:
   filaT.append(c) # Agregar columna
   
  filaT = desplazamientoIzquierda(filaT,1)
  filaT = sustitucionMatriz(caja_S, filaT)
  filaT[0] = agregar_rc(filaT[0], rc[i-1])
  
  matrizS = []
  matrizS.append(xorFila(filasMatriz[(i-1)*nk],filaT)) # Primera fila
  filasMatriz.append(matrizS[0]) # Agregar primera fila

  if(nk != 8): # 128 - 192 bits
   for j in range(1,nk):
    matrizS.append(xorFila(matrizS[j-1],filasMatriz[((i-1)*nk)+j])) # Fila n
    filasMatriz.append(matrizS[j]) # N filas siguientes
  else: # 256 bits   
   for j in range(1,int(nk/2)): # Primeros 3 ciclos
    matrizS.append(xorFila(matrizS[j-1],filasMatriz[((i-1)*nk)+j])) # Fila n
    filasMatriz.append(matrizS[j]) # N filas siguientes
    
   matrizS = [] # Vaciar elemento
   # Sustitucion por matriz a la fila inmediatamente anterior
   filaT = sustitucionMatriz(caja_S, filasMatriz[-1])
   matrizS.append(xorFila(filasMatriz[((i-1)*nk)+(int(nk/2))],filaT)) # Primera fila
   filasMatriz.append(matrizS[0])
   
   # Se mantiene la misma logica que en ciclo anterior
   for j in range(1,int(nk/2)): # Finales 3 ciclos
    matrizS.append(xorFila(matrizS[j-1],filasMatriz[((i-1)*nk)+j+int(nk/2)])) # Segunda fila
    filasMatriz.append(matrizS[j]) # N filas siguientes
  
 posF = 0 # Fila actual a agregar
 for i in range(0,ciclo+1):
  matrizTemp = [] # Matriz temporal
  for j in range(0,4):
   matrizTemp.append(filasMatriz[posF]) # Agregar fila a matriz
   posF = posF + 1 # Siguiente fila
  matriz.append(matrizTemp) # Agregar matriz de ciclo a conjunto matricial
 
 '''
 pos = 0
 for m in matriz:
  for f in m:
   print (pos)
   print (f)
   pos = pos + 1
 '''
 
 for i in range(0,len(matriz)): # Invertir filas a columnas
  matriz[i] = matrizFilaInv(matriz[i])
 #matriz[0] = matrizFilaInv(matrizClave) # Ajustar
 
   
 return matriz # Matriz con todas las claves

def xorFila(fila1, fila2):
 filaR = []
 for i in range(0,len(fila1)):
  bin1 = hexadecimalBinario(fila1[i]) #Convertir a binarios para operacion xor
  bin2 = hexadecimalBinario(fila2[i])
  binR = ""
  for j in range(0,len(bin1)):
   binR = binR + xor(bin1[j],bin2[j]) # Operacion xor
  filaR.append(binarioHexadecimal(binR)) #Convertir a hexadecimal y agregar
 return filaR

# Funcion para invertir la posicion de las columnas por las filas
def matrizFilaInv(matriz):
 matrizN = []
 for c in range(0,len(matriz[0])):
  columna = []
  for f in range(0,len(matriz)):
   columna.append(matriz[f][c]) # Agregar valor de la columna
  matrizN.append(columna) # Agregar columna como fila
 #print(matrizN)
 return matrizN

def crearMatrizHex(claveHex,nk=4):
 matrizByte = []
 pos = 0 # Posicion de copia de caracteres
 maximo = len(claveHex)
 while(pos < maximo): # Crear matriz segun el maximo de caracteres
  fila = []
  for j in range(0, 4):
   fila.append(claveHex[pos:pos+2]) # Agregar hexadecimal
   pos = pos + 2 # Siguiente valor de caracteres
  matrizByte.append(fila) # Agregar fila
 #print (matrizByte) 
 return matrizByte

def crearClave(tam = 16,minimo = 0, maximo = 15):
 clave = ""
 for i in range(0,tam):
  numero = random.randint(minimo,maximo)
  #clave = clave + hex(random.randint(minimo,maximo)).lstrip("0x")
  clave = clave + "{0:x}".format(numero)
 return clave

def sustitucionMatriz(caja_S, fila):
 sus = [] # Nueva fila a agregar
 for f in fila:
  pos_f = int(f[0],16) # Convertir a entero la primera posicion
  pos_c = int(f[1],16) # Convertir a entero la segunda posicion
  sus.append(caja_S[pos_f][pos_c]) # Agregar valores segun caja s
 #print(sus)
 return sus
 
def agregar_rc(hexadecimal, rc):
 binarioH = hexadecimalBinario(hexadecimal,4)
 binarioR = hexadecimalBinario(rc,4)
 #print(binarioH + " " + binarioR)
 resultado = ""
 for i in range(0,len(binarioH)):
  resultado = resultado + xor(binarioH[i],binarioR[i])
 #print(resultado)
 return binarioHexadecimal(resultado)

def desplazamientoDerecha(fila,desp):
 for i in range(0,desp): # Cantidad de desplazamientos a realizar
  ultimo = fila[-1] # Agregar ultimo elemento
  for j in range(len(fila)-1,0,-1): # Cantidad de elementos en fila menos uno
   fila[j] = fila[j-1] # Desplazar posiciones
  fila[0] = ultimo # Agregar elemento eliminado
 return fila  

def desplazamientoIzquierda(fila, desp):
 for i in range(0,desp): # Cantidad de desplazamientos a realizar
  primer = fila[0] # Primer elemento
  for j in range(0,len(fila)-1): # Cantidad de elementos en fila menos uno
   fila[j] = fila[j+1] # Desplazar posiciones
  fila[len(fila)-1] = primer # Agregar elemento eliminado
 return fila


# ------------------------------------------------
# Datos iniciales para encriptar y desencriptar
caja_S_sustitucion = [
['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76'],
['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0'],
['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15'],
['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75'],
['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84'],
['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf'],
['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8'],
['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2'],
['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73'],
['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db'],
['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79'],
['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],
['ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a'],
['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e'],
['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df'],
['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']
]
# conteo circular (round count)
rc = ['01','02','04','08','10','20','40','80','1b','36', # 128 bits
      '6c','d8','ab','4d','9a','2f','5e','bc','63','c6','97','35','6a','d4','b3','7d','fa','ef','c5'] # 256 bits

matrizMult = [
['02','03','01','01'],
['01','02','03','01'],
['01','01','02','03'],
['03','01','01','02']
]

caja_S_sustitucion_inv = [
['52','09','6a','d5','30','36','a5','38','bf','40','a3','9e','81','f3','d7','fb'],
['7c','e3','39','82','9b','2f','ff','87','34','8e','43','44','c4','de','e9','cb'],
['54','7b','94','32','a6','c2','23','3d','ee','4c','95','0b','42','fa','c3','4e'],
['08','2e','a1','66','28','d9','24','b2','76','5b','a2','49','6d','8b','d1','25'],
['72','f8','f6','64','86','68','98','16','d4','a4','5c','cc','5d','65','b6','92'],
['6c','70','48','50','fd','ed','b9','da','5e','15','46','57','a7','8d','9d','84'],
['90','d8','ab','00','8c','bc','d3','0a','f7','e4','58','05','b8','b3','45','06'],
['d0','2c','1e','8f','ca','3f','0f','02','c1','af','bd','03','01','13','8a','6b'],
['3a','91','11','41','4f','67','dc','ea','97','f2','cf','ce','f0','b4','e6','73'],
['96','ac','74','22','e7','ad','35','85','e2','f9','37','e8','1c','75','df','6e'],
['47','f1','1a','71','1d','29','c5','89','6f','b7','62','0e','aa','18','be','1b'],
['fc','56','3e','4b','c6','d2','79','20','9a','db','c0','fe','78','cd','5a','f4'],
['1f','dd','a8','33','88','07','c7','31','b1','12','10','59','27','80','ec','5f'],
['60','51','7f','a9','19','b5','4a','0d','2d','e5','7a','9f','93','c9','9c','ef'],
['a0','e0','3b','4d','ae','2a','f5','b0','c8','eb','bb','3c','83','53','99','61'],
['17','2b','04','7e','ba','77','d6','26','e1','69','14','63','55','21','0c','7d']
]

matrizMultInv = [
['0e','0b','0d','09'],
['09','0e','0b','0d'],
['0d','09','0e','0b'],
['0b','0d','09','0e']
]

tablasGalois = [
[2,[
['00','02','04','06','08','0a','0c','0e','10','12','14','16','18','1a','1c','1e'],
['20','22','24','26','28','2a','2c','2e','30','32','34','36','38','3a','3c','3e'],
['40','42','44','46','48','4a','4c','4e','50','52','54','56','58','5a','5c','5e'],
['60','62','64','66','68','6a','6c','6e','70','72','74','76','78','7a','7c','7e'],
['80','82','84','86','88','8a','8c','8e','90','92','94','96','98','9a','9c','9e'],
['a0','a2','a4','a6','a8','aa','ac','ae','b0','b2','b4','b6','b8','ba','bc','be'],
['c0','c2','c4','c6','c8','ca','cc','ce','d0','d2','d4','d6','d8','da','dc','de'],
['e0','e2','e4','e6','e8','ea','ec','ee','f0','f2','f4','f6','f8','fa','fc','fe'],
['1b','19','1f','1d','13','11','17','15','0b','09','0f','0d','03','01','07','05'],
['3b','39','3f','3d','33','31','37','35','2b','29','2f','2d','23','21','27','25'],
['5b','59','5f','5d','53','51','57','55','4b','49','4f','4d','43','41','47','45'],
['7b','79','7f','7d','73','71','77','75','6b','69','6f','6d','63','61','67','65'],
['9b','99','9f','9d','93','91','97','95','8b','89','8f','8d','83','81','87','85'],
['bb','b9','bf','bd','b3','b1','b7','b5','ab','a9','af','ad','a3','a1','a7','a5'],
['db','d9','df','dd','d3','d1','d7','d5','cb','c9','cf','cd','c3','c1','c7','c5'],
['fb','f9','ff','fd','f3','f1','f7','f5','eb','e9','ef','ed','e3','e1','e7','e5']]]
,
[3,[
['00','03','06','05','0c','0f','0a','09','18','1b','1e','1d','14','17','12','11'],
['30','33','36','35','3c','3f','3a','39','28','2b','2e','2d','24','27','22','21'],
['60','63','66','65','6c','6f','6a','69','78','7b','7e','7d','74','77','72','71'],
['50','53','56','55','5c','5f','5a','59','48','4b','4e','4d','44','47','42','41'],
['c0','c3','c6','c5','cc','cf','ca','c9','d8','db','de','dd','d4','d7','d2','d1'],
['f0','f3','f6','f5','fc','ff','fa','f9','e8','eb','ee','ed','e4','e7','e2','e1'],
['a0','a3','a6','a5','ac','af','aa','a9','b8','bb','be','bd','b4','b7','b2','b1'],
['90','93','96','95','9c','9f','9a','99','88','8b','8e','8d','84','87','82','81'],
['9b','98','9d','9e','97','94','91','92','83','80','85','86','8f','8c','89','8a'],
['ab','a8','ad','ae','a7','a4','a1','a2','b3','b0','b5','b6','bf','bc','b9','ba'],
['fb','f8','fd','fe','f7','f4','f1','f2','e3','e0','e5','e6','ef','ec','e9','ea'],
['cb','c8','cd','ce','c7','c4','c1','c2','d3','d0','d5','d6','df','dc','d9','da'],
['5b','58','5d','5e','57','54','51','52','43','40','45','46','4f','4c','49','4a'],
['6b','68','6d','6e','67','64','61','62','73','70','75','76','7f','7c','79','7a'],
['3b','38','3d','3e','37','34','31','32','23','20','25','26','2f','2c','29','2a'],
['0b','08','0d','0e','07','04','01','02','13','10','15','16','1f','1c','19','1a']
]], 
[9, [
['00','09','12','1b','24','2d','36','3f','48','41','5a','53','6c','65','7e','77'],
['90','99','82','8b','b4','bd','a6','af','d8','d1','ca','c3','fc','f5','ee','e7'],
['3b','32','29','20','1f','16','0d','04','73','7a','61','68','57','5e','45','4c'],
['ab','a2','b9','b0','8f','86','9d','94','e3','ea','f1','f8','c7','ce','d5','dc'],
['76','7f','64','6d','52','5b','40','49','3e','37','2c','25','1a','13','08','01'],
['e6','ef','f4','fd','c2','cb','d0','d9','ae','a7','bc','b5','8a','83','98','91'],
['4d','44','5f','56','69','60','7b','72','05','0c','17','1e','21','28','33','3a'],
['dd','d4','cf','c6','f9','f0','eb','e2','95','9c','87','8e','b1','b8','a3','aa'],
['ec','e5','fe','f7','c8','c1','da','d3','a4','ad','b6','bf','80','89','92','9b'],
['7c','75','6e','67','58','51','4a','43','34','3d','26','2f','10','19','02','0b'],
['d7','de','c5','cc','f3','fa','e1','e8','9f','96','8d','84','bb','b2','a9','a0'],
['47','4e','55','5c','63','6a','71','78','0f','06','1d','14','2b','22','39','30'],
['9a','93','88','81','be','b7','ac','a5','d2','db','c0','c9','f6','ff','e4','ed'],
['0a','03','18','11','2e','27','3c','35','42','4b','50','59','66','6f','74','7d'],
['a1','a8','b3','ba','85','8c','97','9e','e9','e0','fb','f2','cd','c4','df','d6'],
['31','38','23','2a','15','1c','07','0e','79','70','6b','62','5d','54','4f','46']
]],
[11,[
['00','0b','16','1d','2c','27','3a','31','58','53','4e','45','74','7f','62','69'],
['b0','bb','a6','ad','9c','97','8a','81','e8','e3','fe','f5','c4','cf','d2','d9'],
['7b','70','6d','66','57','5c','41','4a','23','28','35','3e','0f','04','19','12'],
['cb','c0','dd','d6','e7','ec','f1','fa','93','98','85','8e','bf','b4','a9','a2'],
['f6','fd','e0','eb','da','d1','cc','c7','ae','a5','b8','b3','82','89','94','9f'],
['46','4d','50','5b','6a','61','7c','77','1e','15','08','03','32','39','24','2f'],
['8d','86','9b','90','a1','aa','b7','bc','d5','de','c3','c8','f9','f2','ef','e4'],
['3d','36','2b','20','11','1a','07','0c','65','6e','73','78','49','42','5f','54'],
['f7','fc','e1','ea','db','d0','cd','c6','af','a4','b9','b2','83','88','95','9e'],
['47','4c','51','5a','6b','60','7d','76','1f','14','09','02','33','38','25','2e'],
['8c','87','9a','91','a0','ab','b6','bd','d4','df','c2','c9','f8','f3','ee','e5'],
['3c','37','2a','21','10','1b','06','0d','64','6f','72','79','48','43','5e','55'],
['01','0a','17','1c','2d','26','3b','30','59','52','4f','44','75','7e','63','68'],
['b1','ba','a7','ac','9d','96','8b','80','e9','e2','ff','f4','c5','ce','d3','d8'],
['7a','71','6c','67','56','5d','40','4b','22','29','34','3f','0e','05','18','13'],
['ca','c1','dc','d7','e6','ed','f0','fb','92','99','84','8f','be','b5','a8','a3']
]],
[13,[
['00','0d','1a','17','34','39','2e','23','68','65','72','7f','5c','51','46','4b'],
['d0','dd','ca','c7','e4','e9','fe','f3','b8','b5','a2','af','8c','81','96','9b'],
['bb','b6','a1','ac','8f','82','95','98','d3','de','c9','c4','e7','ea','fd','f0'],
['6b','66','71','7c','5f','52','45','48','03','0e','19','14','37','3a','2d','20'],
['6d','60','77','7a','59','54','43','4e','05','08','1f','12','31','3c','2b','26'],
['bd','b0','a7','aa','89','84','93','9e','d5','d8','cf','c2','e1','ec','fb','f6'],
['d6','db','cc','c1','e2','ef','f8','f5','be','b3','a4','a9','8a','87','90','9d'],
['06','0b','1c','11','32','3f','28','25','6e','63','74','79','5a','57','40','4d'],
['da','d7','c0','cd','ee','e3','f4','f9','b2','bf','a8','a5','86','8b','9c','91'],
['0a','07','10','1d','3e','33','24','29','62','6f','78','75','56','5b','4c','41'],
['61','6c','7b','76','55','58','4f','42','09','04','13','1e','3d','30','27','2a'],
['b1','bc','ab','a6','85','88','9f','92','d9','d4','c3','ce','ed','e0','f7','fa'],
['b7','ba','ad','a0','83','8e','99','94','df','d2','c5','c8','eb','e6','f1','fc'],
['67','6a','7d','70','53','5e','49','44','0f','02','15','18','3b','36','21','2c'],
['0c','01','16','1b','38','35','22','2f','64','69','7e','73','50','5d','4a','47'],
['dc','d1','c6','cb','e8','e5','f2','ff','b4','b9','ae','a3','80','8d','9a','97']
]],
[14,[
['00','0e','1c','12','38','36','24','2a','70','7e','6c','62','48','46','54','5a'],
['e0','ee','fc','f2','d8','d6','c4','ca','90','9e','8c','82','a8','a6','b4','ba'],
['db','d5','c7','c9','e3','ed','ff','f1','ab','a5','b7','b9','93','9d','8f','81'],
['3b','35','27','29','03','0d','1f','11','4b','45','57','59','73','7d','6f','61'],
['ad','a3','b1','bf','95','9b','89','87','dd','d3','c1','cf','e5','eb','f9','f7'],
['4d','43','51','5f','75','7b','69','67','3d','33','21','2f','05','0b','19','17'],
['76','78','6a','64','4e','40','52','5c','06','08','1a','14','3e','30','22','2c'],
['96','98','8a','84','ae','a0','b2','bc','e6','e8','fa','f4','de','d0','c2','cc'],
['41','4f','5d','53','79','77','65','6b','31','3f','2d','23','09','07','15','1b'],
['a1','af','bd','b3','99','97','85','8b','d1','df','cd','c3','e9','e7','f5','fb'],
['9a','94','86','88','a2','ac','be','b0','ea','e4','f6','f8','d2','dc','ce','c0'],
['7a','74','66','68','42','4c','5e','50','0a','04','16','18','32','3c','2e','20'],
['ec','e2','f0','fe','d4','da','c8','c6','9c','92','80','8e','a4','aa','b8','b6'],
['0c','02','10','1e','34','3a','28','26','7c','72','60','6e','44','4a','58','56'],
['37','39','2b','25','0f','01','13','1d','47','49','5b','55','7f','71','63','6d'],
['d7','d9','cb','c5','ef','e1','f3','fd','a7','a9','bb','b5','9f','91','83','8d']
]]]

expansion = 256
if(expansion == 128):
 clave = crearClave(32) # 128 bits
elif(expansion == 192):
 clave = crearClave(48) # 192 bits
elif(expansion == 256):
 clave = crearClave(64) # 256 bits

#clave = "2b7e151628aed2a6abf7158809cf4f3c"
#clave = "8e73b0f7da0e6452c810f32b809079e562f8ead2522c6b7b"
#clave = "000102030405060708090a0b0c0d0e0f1011121314151617"
#clave = "603deb1015ca71be2b73aef0857d77811f352c073b6108d72d9810a30914dff4"
#clave = "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f"
mensaje = "Encripta este mensaje 123456??"
#mensaje = "00112233445566778899aabbccddeeff"

# ------------------------------------------------

print("Mensaje en texto plano = " + mensaje)
print("Clave = " + clave)

mensajeEncriptado = encriptar(mensaje,clave,caja_S_sustitucion,rc,matrizMult,expansion)
print("Mensaje encriptado = " + mensajeEncriptado)

mensajeDesencriptado = desencriptar(mensajeEncriptado,clave,caja_S_sustitucion,caja_S_sustitucion_inv,rc,matrizMultInv,expansion)
print("Mensaje desencriptado = " + mensajeDesencriptado)

