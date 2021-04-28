import random

def encriptar(clave,mensaje):
 mensajeEncriptado = ""
 for m in mensaje:
  if(m.isalpha()): # El texto es del alfabeto
   mm = ord(m) # Convertir texto a ASCII
   if((mm >= 97 and mm <= 122)or(mm >= 65 and mm <= 90)):
    if(m.islower()):
     # a-z = 97-122 en ASCII
     mm -= 97 # Reducir a 0 para obtener posicion
     mensajeEncriptado += clave[0][mm][1] # Intercambiar letras
    else:
     # A-Z = 65-90 en ASCII
     mm -= 65
     mensajeEncriptado += (clave[0][mm][1]).upper() # Intercambiar letras a mayuscula
  elif(m.isdigit()): # El texto es un numero
   # 0-9 = 48-57 en ASCII
   mm = ord(m)
   mm -= 48
   mensajeEncriptado += (clave[1][mm][1])
  else:
   mensajeEncriptado += m
 return mensajeEncriptado

def desencriptar(clave,mensaje):
 mensajeDesencriptado = ""
 for m in mensaje:
  if(m.isalpha()): # El texto es del alfabeto
   mm = ord(m) # Convertir texto a ASCII
   if((mm >= 97 and mm <= 122)or(mm >= 65 and mm <= 90)):
    if(m.islower()):
     # a-z = 97-122 en ASCII
     mm = encontrar_posicion(clave[0], 1, m)
     mensajeDesencriptado += clave[0][mm][0] # Intercambiar letras
    else:
     # A-Z = 65-90 en ASCII
     mm = encontrar_posicion(clave[0], 1, m.lower())
     mensajeDesencriptado += (clave[0][mm][0]).upper() # Intercambiar letras a mayuscula
  elif(m.isdigit()): # El texto es un numero
   # 0-9 = 48-57 en ASCII
   mm = encontrar_posicion(clave[1], 1, m)
   mensajeDesencriptado += (clave[1][mm][0])
  else:
   mensajeDesencriptado += m
 return mensajeDesencriptado

# La posicion 0 sera igual a la letra 'a' 
def crear_abecedario(abc): 
 abecedario = []
 limite = len(abc)
 
 for n in range(0, limite):
  numero = obtener_numero_aleatorio(0,limite-1) # Crear numero aleatorio
  existe = False # Variable para verificar que el numero no exista
  for a in abecedario:
   if(a == numero): # Verificar que no este en el arreglo
    existe = True
    break
  if(existe): # El numero aleatorio ya existia, se agrega el primer numero ordenado
   for i in range(0,limite): # Numeros ordenados a agregar
    existe2 = False # Verificar numero ordenado no exista
    for a in abecedario: # Verificar variables del arreglo
     if(a == i):
      existe2 = True
      break
    if(not existe2):
     abecedario.append(i) # Agregar primer numero que no exista
     break
  else:
   abecedario.append(numero) # Agregar numero
 
 abecedario_n = [] # Arreglo para agregar caracteres
 i = 0
 for n in abecedario:
  abecedario_n.append([abc[i],abc[n]]) # Enlazar nuevo orden
  i = i+1
 
 return abecedario_n # Retornar arreglo con posiciones aleatorias

def encontrar_posicion(clave, numero, valor):
 i = 0
 for c in clave:
  if(c[numero] == valor): # Buscar valor en el arreglo 
   return i # Retonar posicion
  i = i+1
 return null # Valor no encontrado

def obtener_numero_aleatorio(minimo, maximo):
 return random.randint(minimo, maximo)


abc = ['a','b','c','d','e','f','g',
       'h','i','j','k','l','m','n',
       'o','p','q','r','s','t','u',
       'v','w','x','y','z']
n10 = ['0','1','2','3','4',
       '5','6','7','8','9']

claves = [crear_abecedario(abc),crear_abecedario(n10)]

print ("Clave alfabetica")
print (claves[0])
print ("Clave numerica")
print (claves[1])

mensaje = "Encripta este mensaje 123456??"

mensajeE = encriptar(claves,mensaje)
print (mensajeE)

mensajeD = desencriptar(claves, mensajeE)
print(mensajeD)
