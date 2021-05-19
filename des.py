'''
Codigo hecho en base a la explicacion paso por paso publicada en Laissez Faire City Times
Obtenido de: page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
'''

import math
import random
import codecs

def encriptar(mensaje,pc_1,pc_2,k_n,p_i,e_b,s_i,p,p_i_inv):
 mensajeEncriptado = ""
 mensajeH = completar64(mensajeHexadecimal(mensaje))
 #mensajeH = hexadecimalBinario(mensaje)
 #print(len(mensajeH))
 #print("Mensaje Hexadecimal = " + mensajeH)
 for sm in range(0,len(mensajeH),16):
 #for sm in range(0,len(mensaje),16):
  #print(len(mensajeH[sm:(sm+16)]))
  mensajeB = hexadecimalBinario(mensajeH[sm:(sm+16)])
  #mensajeB = hexadecimalBinario(mensaje)
  mensajeEncriptado = mensajeEncriptado + codificarBloques(mensajeB,p_i,e_b,k_n,s_i,p,p_i_inv) # Agregar mensaje codificado al mensaje
 #print("Mensaje Hex = " + mensajeH)
 #mensajeT = hexadecimalASCII(mensajeH)
 #print("Mensaje ASCII = " + mensajeT)
 #mensajeB = hexadecimalBinario(mensajeH)
 #print("Mensaje Bin = " + mensajeB)
 #mensajeH = binarioHexadecimal(mensajeB)
 #print("Mensaje Hex = " + mensajeH)
 #print(len(mensajeB))
 return mensajeEncriptado

def desencriptar(mensaje,p_i,e_b,k_n,s_i,p,p_i_inv):
 mensajeDesencriptado = ""
 #mensajeH = mensajeHexadecimal(mensaje)
 mensajeHDesencriptado = "" # Mensaje de hexadecimal a hexadecimal desencriptado
 
 for sm in range(0,len(mensaje),16):
  mensajeB = hexadecimalBinario(mensaje[sm:(sm+16)])
  mensajeHDesencriptado = mensajeHDesencriptado + decodificarBloques(mensajeB,p_i,e_b,k_n,s_i,p,p_i_inv) # Agregar mensaje decodificado y en ASCII
 
 #print("Mensaje Hexadecimal Desencriptado = " + mensajeHDesencriptado)
 
 mensajeDesencriptado = hexadecimalASCII(mensajeHDesencriptado) # Convertir a ASCII
 
 return mensajeDesencriptado
 
def mensajeHexadecimal(mensaje):
 mensajeH = ""
 for m in mensaje:
  mensajeH = mensajeH + hex(ord(m)).lstrip("0x")
  #print(mensajeH)
 return mensajeH

def completar64(hexadecimal):
 n_hex = 16 # Cantidad de hexadecimales por bloque
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

'''
 hexadecimal = Mensaje en hexadecimal
 tam = Tamano de la cantidad de binarios que se toman al convertir
'''
def hexadecimalBinario(texto, tam = 4):
 formato = "{0:0" + str(tam) +"b}" # Formato de salida
 binario = ""
 for t in texto:
  binario = binario + formato.format(int(t,16)) # Convertir a binario y agregar
 return binario

def enteroBinario(numero, tam = 4):
 formato = "{0:0" + str(tam) +"b}" # Formato de salida
 binario = formato.format(numero) # Convertir a binario
 return binario

def binarioEntero(binario):
 return int(binario,2)
 
def binarioHexadecimal(binario):
 hexadecimal = ""
 formato = "{0:x}"
 for i in range(0,len(binario),4):
  hexadecimal = hexadecimal + formato.format(binarioEntero(binario[i:i+4])) # Convertir binario a hexadecimal y agregar
 return hexadecimal

#def hexadecimalMensaje(hexadecimal):
 #texto = ""
 

def hexadecimalASCII(hexadecimal):
 texto = ""
 #print("Hexadecimal = " + hexadecimal)
 #bytes_t = bytes.fromhex(hexadecimal) # Convertir a bytes
 #print(bytes_t)
 #texto = texto + bytes_t.decode("ASCII") # Convertir a ASCII
 texto = codecs.decode(hexadecimal,"hex").decode("ascii")
 '''
 for i in range(0,len(hexadecimal),6):
  bytes_t = bytes.fromhex(hexadecimal[i:i+6]) # Convertir a bytes
  print(bytes_t)
  texto = texto + bytes_t.decode("ASCII") # Convertir a ASCII
  print(texto)
 '''
 return texto
 

'''
tam = Tamano de la clave
minimo,maximo = Rango de numeros aleatorios
'''
def crearClave(tam = 16,minimo = 0, maximo = 15):
 clave = ""
 for i in range(0,tam):
  numero = random.randint(minimo,maximo)
  #clave = clave + hex(random.randint(minimo,maximo)).lstrip("0x")
  clave = clave + "{0:x}".format(numero)
 return clave
 
def crearMatrizOrden(fila,columna,minimo,maximo):
 matriz = []
 numero = minimo
 for f in range(0,fila):
  filaM = []
  for c in range(0,columna):
   filaM.append(-1)
  for c in range(0,columna):
   col = random.randint(0,columna-1)
   if(filaM[col] != -1):
    col = 0 # Buscar primera posicion libre
    while(filaM[col] != -1):
     col = col + 1 # Aumentar posicion
   #filaM.append(random.randint(minimo,maximo)) # Agregar numero a fila
   #print("columna " + str(c))
   #print(filaM)
   #print(numero)
   filaM[col] = numero # Agregar numero en orden
   numero = numero + 1 # Siguiente numero
   
   if(numero > maximo):
    numero = minimo
  #print(filaM)
  matriz.append(filaM) # Agregar fila a la matriz
 return matriz
 
def crearArregloNumeroNoRepetido(tam, minimo, maximo):
 arr_n = [] # Variabla a asignar numeros
 for i in range(0,tam):
  numero = random.randint(minimo,maximo) # Generar numero aleatorio
  if(encontrarNumeroFila(arr_n,numero) != -1): # Buscar si existe
   numero = 0
   while(encontrarNumeroFila(arr_n,numero) != -1):
    numero = numero + 1 # Aumentar hasta encontrar un valor inexistente
  arr_n.append(numero) # Agregar numero
 return arr_n 
  

'''
fila,columna = Matriz mxn
minimo,maximo = Rango de numeros aleatorios
'''
def crearMatrizNumeroAleatorio(fila, columna, minimo, maximo):
 matriz = []
 for f in range(0,fila):
  filaM = [] # Fila a agregar a la matriz
  for c in range(0,columna):
   if(f == 0):
    if(c > 0):
     numero = random.randint(minimo,maximo) # Crear numero aleatorio
     while(encontrarNumeroFila(filaM,numero) != -1):
      numero = random.randint(minimo,maximo) # Crear hasta que numero no exista
     filaM.append(random.randint(minimo,maximo)) # Agregar numero 
    else:
     filaM.append(random.randint(minimo,maximo)) # Agregar numero
   else:
    numero = random.randint(minimo,maximo) # Crear numero aleatorio
    if(encontrarNumeroMatriz(matriz,numero) != -1):
     for i in range(0,maximo):
      numero = i
      if(encontrarNumeroMatriz(matriz,numero) == -1):
       break # Salir del ciclo al encontrar numero no existente en matriz
    if(encontrarNumeroFila(filaM,numero) != -1):
     inicio = numero
     for i in range(inicio, maximo):
      numero = i
      if(encontrarNumeroFila(filaM,numero) == -1):
       break # Salir del ciclo al no encontrar numero en fila
    filaM.append(numero) # Agregar numero
  
  matriz.append(filaM) # Agregar fila a la matriz   
 return matriz

def encontrarNumeroFila(fila, numero):
 pos = 0 # Posicion si encuentra numero
 for columna in fila:
  if(numero == columna):
   #return True
   return pos
  pos = pos + 1
 #return False
 return -1

def encontrarNumeroMatriz(matriz,numero):
 pos = 0 # Posicion si encuentra numero
 for fila in matriz:
  for columna in fila:
   if(numero == columna):
    #return True
    return pos
   pos = pos + 1
 #return False
 return -1
 
def xor(b1,b2):
 if(b1 != b2):
  return "1"
 return "0"

def desplazarIzquierda(binario,numero):
 binarioN = binario[numero:len(binario)] # Nuevo orden
 binarioN = binarioN + binario[0:numero] # Agregar caracteres iniciales al final
 return binarioN

def tablaPermutacion64(defecto = 1):
 pc_1 = []
 if(defecto == 1):
  pc_1 = [[56,48,40,32,24,16,8],
         [0,57,49,41,33,25,17],
         [9,1,58,50,42,34,26],
         [18,10,2,59,51,43,35],
         [62,54,46,38,30,22,14],
         [6,61,53,45,37,29,21],
         [13,5,60,52,44,36,28],
         [20,12,4,27,19,11,3]]
 else:
  pc_1 = crearMatrizNumeroAleatorio(8,7,0,63) # Matriz permutacion 64 bits mxn = 8x7=56
 return pc_1
 
def tablaPermutacion48(defecto = 1):
 pc_2 = []
 if(defecto == 1):
  pc_2 = [[13,16,10,23,0,4],
         [2,27,14,5,20,9],
         [22,18,11,3,25,7],
         [15,6,26,19,12,1],
         [40,51,30,36,46,54],
         [29,39,50,44,32,47],
         [43,48,38,55,33,52],
         [45,41,49,35,28,31]]
 else:
  pc_2 = crearMatrizNumeroAleatorio(8,6,0,55) # Matriz permutacion 56 bits mxn = 8x6 = 48
 return pc_2
 
def tablaPermutacion32(defecto = 1):
 p = []
 if(defecto == 1):
  p = [[15,6,19,20],
      [28,11,27,16],
      [0,14,22,25],
      [4,17,30,9],
      [1,7,23,13],
      [31,26,2,8],
      [18,12,29,5],
      [21,10,3,24]]
 else:
  p = crearMatrizNumeroAleatorio(8,4,0,31) # Matriz permutacion 32 bits mxn = 8x4 = 32
 return p

def permutacionInicial64(defecto = 1):
 p_i = []
 if(defecto == 1):
  p_i = [[57,49,41,33,25,17,9,1],
        [59,51,43,35,27,19,11,3],
        [61,53,45,37,29,21,13,5],
        [63,55,47,39,31,23,15,7],
        [56,48,40,32,24,16,8,0],
        [58,50,42,34,26,18,10,2],
        [60,52,44,36,28,20,12,4],
        [62,54,46,38,30,22,14,6]]
 else:
  p_i = crearMatrizNumeroAleatorio(8,8,0,63) # Matriz permutacion 64 bits mxn = 8x8 = 64
 return p_i
 
def permutacionInicialInv64(defecto = 1):
 p_i = []
 if(defecto == 1):
  p_i = [[39,7,47,15,55,23,63,31],
        [38,6,46,14,54,22,62,30],
        [37,5,45,13,53,21,61,29],
        [36,4,44,12,52,20,60,28],
        [35,3,43,11,51,19,59,27],
        [34,2,42,10,50,18,58,26],
        [33,1,41,9,49,17,57,25],
        [32,0,40,8,48,16,56,24]]
 else:
  p_i = crearMatrizNumeroAleatorio(8,8,0,63) # Matriz permutacion 64 bits mxn = 8x8 = 64
 return p_i
 
def tablaSeleccionEBit(defecto = 1):
 e_b = []
 if(defecto == 1):
  e_b = [[31,0,1,2,3,4],
         [3,4,5,6,7,8],
         [7,8,9,10,11,12],
         [11,12,13,14,15,16],
         [15,16,17,18,19,20],
         [19,20,21,22,23,24],
         [23,24,25,26,27,28],
         [27,28,29,30,31,0]]
 else:
  e_b = crearMatrizOrden(8,6,0,31) # Matriz con entrada valores de 0-31 (32) y mxn = 8x6 = 48
 #print (e_b)
 return e_b
 
def ordenarPermutacion(binario, permutacion, tam):
 ordenar = ""
 pos = 0
 #tam = len(binario)
 while(pos < tam):
  ordenar = ordenar + binario[encontrarNumeroMatriz(permutacion,pos)]
  pos = pos + 1
 return ordenar

def cajasS(defecto = 1):
 si = [] # Arreglo de cajas S
 if(defecto == 1):
  s_i = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
         [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
         [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
         [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]
  si.append(s_i) # Agregar caja 1
  s_i = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
         [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
         [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
         [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]
  si.append(s_i) # Agregar caja 2
  s_i = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
         [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
         [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
         [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]
  si.append(s_i) # Agregar caja 3
  s_i = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
         [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
         [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
         [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]
  si.append(s_i) # Agregar caja 4
  s_i = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
         [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
         [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
         [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]
  si.append(s_i) # Agregar caja 5
  s_i = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
         [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
         [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
         [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]
  si.append(s_i) # Agregar caja 6
  s_i = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
         [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
         [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
         [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]
  si.append(s_i) # Agregar caja 7
  s_i = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
         [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
         [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
         [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]
  si.append(s_i) # Agregar caja 8
 else:
  fila = 4
  columna = 16
  minimo = 0
  maximo = 15
  cajas = 8
  for i in range(0,cajas):
   s_i = []
   for f in range(0,fila):
    s_i.append(crearArregloNumeroNoRepetido(columna,minimo,maximo)) # Agregar fila
   si.append(s_i) # Agregar caja
   #print(s_i)
 return si

def crearSubClaves(clave,pc_1,pc_2):
 claveB = hexadecimalBinario(clave) # Clave en binario
 # En pc_1 solo 56 bits son tomados en cuenta
 clave_pc_1 = ""
 #print("Tam de claveB " + str(len(clave)))
 #print("Clave " + clave)
 #print("Tam de claveB " + str(len(claveB)))
 for f in pc_1: # Filas
  for c in f: # Columnas
   clave_pc_1 = clave_pc_1 + claveB[c] # Establecer nuevo orden binario
 
 # Desplazamiento de bits hacia la izquierda
 n_desp_izq = [1,1,2,2,2,2,2,2,
               1,2,2,2,2,2,2,1] # Ultima posicion igual a la primera
 mitad = int(len(clave_pc_1)/2)
 c_0 = clave_pc_1[0:mitad] # Mitad izquierda
 d_0 = clave_pc_1[mitad:len(clave_pc_1)] # Mitad derecha
 
 #print("Clave Binario: " + claveB)
 #print("C_0 = " + c_0)
 #print(len(c_0))
 #print("D_0 = " + d_0)
 
 c_n = [] # Arreglo de desplazamientos mitad izquierda
 d_n = [] # Arreglo de desplazamientos mitad derecha
 c_n.append(c_0) # Base
 d_n.append(d_0) # Base
 
 for i in range(0,16):
  c_n.append(desplazarIzquierda(c_n[i],n_desp_izq[i])) # Agregar al arreglo izquierda el desplazamiento en base al anterior
  d_n.append(desplazarIzquierda(d_n[i],n_desp_izq[i])) # Agregar al arreglo derecha el desplazamiento en base al anterior
  #print("C_" + str(i+1) + " = " + c_n[i+1])
  #print("D_" + str(i+1) + " = " + d_n[i+1])
 
 k_n = [] # Arreglo con nuevo orden en base a pc_2 y la union de las dos mitades binarias
 #pc_2)
 for i in range(1,17):
  c_d = c_n[i] + d_n[i] # Union de mitades binarias
  #print("C_D = " + c_d)
  k_t = "" # Fila a agregar a k_n
  for f in pc_2:
   for c in f:
    k_t = k_t + c_d[c] # Agregar caracter segun la posicion en tabla pc_2
  #for n in pc_2:
  # k_t = k_t + c_d[n]
  
  k_n.append(k_t) # Agregar fila a k_n
  #print("K_"+str(i)+" = " + k_n[i-1])
 
 return k_n
 
'''
binario = Mensaje en binario
'''
def codificarBloques(binario,p_i,e_b,k_n,s_i,p,p_i_inv): 
 binario_p_i = ""
 for f in p_i:
  for c in f:
   binario_p_i = binario_p_i + binario[c] # Reordenar binario
 #print("P_I = " + binario_p_i)
 
 l_0 = binario_p_i[0:int(len(binario_p_i)/2)]
 r_0 = binario_p_i[int(len(binario_p_i)/2):len(binario_p_i)]
 #print("L_0 = " + l_0)
 #print("R_0 = " + r_0)
 l_n = [] # Mitad izquierda
 r_n = [] # Mitad derecha
 r_n.append(r_0) # Agregar primer bloque de la derecha para iniciar ciclo
 l_n.append(l_0) # Agregar primer bloque a la izquierda para iniciar ciclo
 
 for i in range(0,16):
  r_e_b = "" # Expansion de r_0 de 32 a 48 bits en base a e_b
  for f in e_b:
   for c in f:
    r_e_b = r_e_b + r_n[i][c] # Reordenar en base a e_b
  #print("E(R0) = " + r_e_b)
  #print("K_n = " + k_n[i])
  xor_k_e = ""
  for j in range(0,len(k_n[i])):
   xor_k_e = xor_k_e + xor(r_e_b[j],k_n[i][j])
  #print("XOR_K1_E = " + xor_k_e)
  s_b = "" # Nuevo valor en base a cajas S
  for s in range(0,len(s_i)):
   pos_i = s*6 # Posicion izquierda
   b_n = xor_k_e[pos_i:pos_i+6] # Dividir binario en subgrupos de tamano 6
   pos_f = binarioEntero(b_n[0] + b_n[5]) # Obtener primer y ultimo caracter y convertir a entero para la fila
   pos_c = binarioEntero(b_n[1:5]) # Obtener valor del medio para la columna
   #print(pos_f)
   #print(pos_c)
   #print(s_i[pos_f])
   s_b = s_b + enteroBinario(s_i[s][pos_f][pos_c]) # Agregar nuevo valor
  #print("S_B = " + s_b)
  #print("Tam S_B = " + str(len(s_b)))
  f_s_b = "" # Nueva permutacion de 32 bits
  for f in p:
   for c in f:
    f_s_b = f_s_b + s_b[c] # Reordenar s_b en base a matriz permutacion p
  #print("F_S_B = " + f_s_b)
  
  l_n.append(r_n[i]) # Agregar bloque derecha a la izquierda sin modificar
  r_siguiente = "" # Nuevo bloque derecha
  for j in range(0,len(f_s_b)):
   r_siguiente = r_siguiente + xor(l_n[i][j],f_s_b[j]) # Calculo xor entre posicion anterior izquierda y funcion actual 
  #print("R_"+str(i+1)+" = " + r_siguiente)
  #print("L_"+str(i+1)+" = " + l_n[i+1])
  r_n.append(r_siguiente) # Agregar bloque derecha
 
 binario_p_i_inv = "" # Variable a agregar nueva permutacion
 '''
 for i in range(1,17):
  reverso = r_n[i]+l_n[i] # Invertir orden de las mitades
  print("R_L = " + reverso)
 '''
 reverso = r_n[16]+l_n[16]
 #print("R_L_16 = " + reverso)
 for f in p_i_inv:
  for c in f:
   binario_p_i_inv = binario_p_i_inv + reverso[c] # Establecer nuevo orden
 #print("IP_Inv = " + binario_p_i_inv)
 #print("Ordnear Inv = " + ordenarPermutacion(binario_p_i_inv,p_i_inv))
 m_hexa = binarioHexadecimal(binario_p_i_inv) # Obtener hexadecimal
 #print("Hexadecimal = " + m_hexa)
 return m_hexa
  
def decodificarBloques(binario,p_i,e_b,k_n,s_i,p,p_i_inv):
 binario_p_i_inv = ordenarPermutacion(binario,p_i_inv,len(binario)) # Reordenar en base a permutacion p_i_inv
 #print ("R_L_16 = " + binario_p_i_inv)
 izquierda = binario_p_i_inv[int(len(binario_p_i_inv)/2):len(binario_p_i_inv)] # Mitad izquierda
 derecha = binario_p_i_inv[0:int(len(binario_p_i_inv)/2)] # Mitad derecha
 #print("L_16 = " + izquierda)
 #print("R_16 = " + derecha)
 l_n = [] # Mitad izquierda
 r_n = [] # Mitad derecha
 l_n.append(izquierda) # Agregar ultimo valor de la izquierda
 r_n.append(derecha) # Agregar ultimo valor de la derecha
 pos_l = 0 # Posicion actual inversa de mitad izquierda (0=>15|1=>14|...|15=>0)
 
 for i in range(15,-1,-1):
  r_e_b = "" # Expansion de r_0 de 32 a 48 bits en base a e_b
  for f in e_b:
   for c in f:
    #print(c)
    r_e_b = r_e_b + l_n[pos_l][c] # Reordenar en base a e_b
  
  xor_k_e = ""
  for j in range(0,len(k_n[i])):
   xor_k_e = xor_k_e + xor(r_e_b[j],k_n[i][j])
  
  s_b = "" # Nuevo valor en base a cajas S
  for s in range(0,len(s_i)):
   pos_i = s*6 # Posicion izquierda
   b_n = xor_k_e[pos_i:pos_i+6] # Dividir binario en subgrupos de tamano 6
   pos_f = binarioEntero(b_n[0] + b_n[5]) # Obtener primer y ultimo caracter y convertir a entero para la fila
   pos_c = binarioEntero(b_n[1:5]) # Obtener valor del medio para la columna
   s_b = s_b + enteroBinario(s_i[s][pos_f][pos_c]) # Agregar nuevo valor
  
  f_s_b = "" # Nueva permutacion de 32 bits
  for f in p:
   for c in f:
    f_s_b = f_s_b + s_b[c] # Reordenar s_b en base a matriz permutacion p
  #print("F_S_B = " + f_s_b)
  
  l_previo = "" # Variabla a asignar mitad izquierda previa
  for j in range(0,len(r_n[pos_l])):
   l_previo = l_previo + xor(r_n[pos_l][j],f_s_b[j])  
  #print("L_" + str(i) + " = " + l_previo)
  
  l_n.append(l_previo) # Agregar nuevo valor a mitad izquierda
  r_n.append(l_n[pos_l]) # Agregar arreglo anterior ubicado en mitad izquierda
  
  pos_l = pos_l + 1
 #print("R_0 = " + l_n[15])
 #print("L_0 = " + l_n[16])
 
 binario_p_i = l_n[16] + l_n[15] # Unir mitad izquierda y derecha iniciales
 m_binario = ordenarPermutacion(binario_p_i, p_i, len(binario_p_i)) # Reordenar en base a permutacion p_i
 m_hexa = binarioHexadecimal(m_binario) # Obtener hexadecimal
 
 #print(m_hexa)
 
 return m_hexa

  

#mensaje = "Your lips are smoother than vaseline"
mensaje = "Encripta este mensaje 123456??"
#print(mensajeHexadecimal(mensaje))
#print(completar64(mensajeHexadecimal(mensaje)))
#m = "0123456789ABCDEF"
#print(hexadecimalBinario(m))
clave = crearClave()
claveBinaria = hexadecimalBinario(clave)
#print(clave)
#print(claveBinaria)
matriz1 = crearMatrizNumeroAleatorio(8,7,0,64)
#print(matriz1)
#crearSubClaves(clave)
#k = "133457799BBCDFF1"

# ------------------------------------------------
pc_1 = tablaPermutacion64(0)
pc_2 = tablaPermutacion48(0)
k_n = crearSubClaves(clave,pc_1,pc_2)
p_i = permutacionInicial64()
e_b = tablaSeleccionEBit(0)
s_i = cajasS(0)
p = tablaPermutacion32(0)
p_i_inv = permutacionInicialInv64()
#codificarBloques(hexadecimalBinario(m),p_i,e_b,k_n,s_i,p,p_i_inv)
# ------------------------------------------------
mensajeE = encriptar(mensaje,pc_1,pc_2,k_n,p_i,e_b,s_i,p,p_i_inv)
print(mensajeE)

mensajeD = desencriptar(mensajeE,p_i,e_b,k_n,s_i,p,p_i_inv)
print(mensajeD)

#decodificarBloques(hexadecimalBinario(mensajeE),p_i,e_b,k_n,s_i,p,p_i_inv)
