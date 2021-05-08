'''
alfabeto = Alfabeto para encriptar
clave = Texto para realizar desplazamientos
mensaje = Texto a encriptar
encriptar = 1 => Encriptar || 0 => Desencriptar
'''
def encriptarDesencriptar(alfabeto, clave, mensaje, encriptar = 1):
 mensaje_ed = ""
 pos_clave = 0 # Posicion actual en la clave para desplazar
 tam = len(alfabeto) # Tamano del alfabeto
 tam_c = len(clave) # Tamano de la clave
 for m in mensaje:
  mMayuscula = False # Validar si caracter en mensaje es mayuscula
  if(validar_caracter(m)):
   if(m.isupper()):
    mMayuscula = True
    m = m.lower()
   sum_clave = 0 # Evitar ciclo infinito en clave
   while(sum_clave <= tam_c): # Validar caracter en clave
    sum_clave = sum_clave + 1
    if(validar_caracter(clave[pos_clave])):
     break
    else:
     pos_clave = pos_clave + 1
     if(pos_clave == tam_c):
      pos_clave = 0
   if(sum_clave > tam_c):
    mensaje_ed = mensaje_ed + m # No se pudo encriptar
   c = ""
   if(c.isupper()):
    c = clave[pos_clave].lower()
   else:
    c = clave[pos_clave]
   n_desplazar = encontrar_posicion(alfabeto, c) # Numero de desplazamientos
   n_actual = encontrar_posicion(alfabeto, m) # Posicion actual del caracter
   
   mm = "" # Caracter a agregar al mensaje

   if(mMayuscula):
    #mensaje_ed = mensaje_ed + alfabeto[(n_actual+n_desplazar)%tam].upper()
    if(encriptar == 1):
     mm = alfabeto[(n_actual+n_desplazar)%tam].upper()
    else:
     mm = alfabeto[(n_actual-n_desplazar)%tam].upper()
   else: 
    #mensaje_ed = mensaje_ed + alfabeto[(n_actual+n_desplazar)%tam] # Nuevo caracter
    if(encriptar == 1):
     mm = alfabeto[(n_actual+n_desplazar)%tam]
    else:
     mm = alfabeto[(n_actual-n_desplazar)%tam]
   
   mensaje_ed = mensaje_ed + mm # Agregar caracter al nuevo mensaje
   
   pos_clave = pos_clave + 1 # Sumar uno para el siguiente ciclo
   if(pos_clave == tam_c):
    pos_clave = 0
  else:
   mensaje_ed = mensaje_ed + m
 return mensaje_ed
 
def encontrar_posicion(alfabeto, caracter):
 pos = 0
 for a in alfabeto:
  if(a == caracter): # Retornar posicion encontrada
   return pos
  pos = pos + 1

def validar_caracter(caracter):
 return caracter.isalpha() or caracter.isdigit()

clave = "peras90"
alfabeto = ['a','b','c','d','e','f','g',
       'h','i','j','k','l','m','n',
       'o','p','q','r','s','t','u',
       'v','w','x','y','z','0','1',
       '2','3','4','5','6','7','8','9']

mensaje = "Encripta este mensaje 123456??"

#mensajeE = encriptar()
mensajeE = encriptarDesencriptar(alfabeto,clave,mensaje,1)
print(mensajeE)

#mensajeD = desencriptar()
mensajeD = encriptarDesencriptar(alfabeto,clave,mensajeE,0)
print(mensajeD)
