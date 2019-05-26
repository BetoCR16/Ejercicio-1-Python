import random
def palabraSecreta():
    palabras = ['agua', 'perro', 'juego', 'computadora', 'usuario', 'programa', 'programacion']
    eleccion = random.choice(palabras)
    return eleccion

def adivinar(palabra, intentadas):
    for letra in palabra:
        if letra != " ":
            if letra not in intentadas:
                return False
    return True

def mostrar(palabra, intentadas, intentos, turno, letraIntento):
    print('Turno: ', turno)
    print('Letras incorrectas: ', aciertoFallo(palabra, intentadas))
    print('Fallos: ', intentos)
    print(ocultarPalabra(palabra, intentadas))

def ocultarPalabra(palabra, intentadas):
    resultado = ""
    for letra in palabra:
        if letra in intentadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado

def leerIntento(intentadas):
    print()
    letra = input('Escribe una letra: ').lower()
    while len(letra) != 1 or letra not in 'abcdefghijklmnñopqrstuvwxyz' or letra in intentadas:
        print ('Ingrese una letra que no haya intentado. Letras intentadas: ', intentadas)
        letra = input('Escriba una letra: ').lower()
    return letra

def aciertoFallo(palabra, intentadas):
    letraCorrecta = ''
    letraIncorrecta = ''
    if intentadas in palabra:
        letraCorrecta += intentadas + ' ' 
    else:
        letraIncorrecta += intentadas + ' '
        
    return letraIncorrecta
    
    

def jugarOtraVez():
    respuesta = input('Quiere volver a jugar? (s/n) :').lower()
    if respuesta == 's':
        jugar = True
    elif respuesta == 'n':
        jugar = False
        print('Muchas gracias por jugar :D')
    return jugar
    
#---------------------------------- Principal ------------------------------
print('Bienvenido al juego de ahorcado\n')
intentosMax = 7

jugar = True
while jugar:
    palabra = palabraSecreta()
    intentadas = ''
    ocultarPalabra(palabra, intentadas)
    intentos = 0
    turno = 1
    while intentos < intentosMax and not adivinar(palabra, intentadas):
        letraIntento = ''
        mostrar(palabra, intentadas, intentos, turno, letraIntento)
        letraIntento = leerIntento(intentadas)
        aciertoFallo(palabra, letraIntento)
        intentadas += letraIntento
        turno += 1
     
    jugar = jugarOtraVez()
    
