#------------------------------ Funciones --------------------------------------------
def introducirOpción():
    opción = input ('Escoja una opción:\n 1. Ingresar 2 números\n 2. Calcular sumatoria\n 3. Convertir de libras a kg\n 4. Convertir de kg a libras\n 5. Dividir los números\n 6. Salir\n \n Su opción: ')
    return opción

def calcularSumatoria(num1, num2):
    suma = 0
    for valor in range(num1, num2):
        suma = suma + valor
    return suma

def convertirLb_Kg(num1):
    resultado = num1 / 2.205
    return resultado

def convertirKg_Lb(num1):
    resultado = num1 * 2.205
    return resultado

def dividirNumeros(num1, num2):
    if num2 == 0:
        print('Error, Segundo número no puede ser cero')
    else:
        solucion = num1 / num2
    return solucion

#----------------------------------------- Programa Principal -------------------------------------------------------

opción = input ('Escoja una opción:\n 1. Ingresar 2 números\n 2. Calcular sumatoria\n 3. Convertir de kg a libras\n 4. Calcular de libras a kilogramos\n 5. Dividir los números\n 6. Salir\n \n Su opción: ')

while (opción != '6'):
    if opción == '1':
        num1 = int(input('Introduzca el primer número: '))
        num2 = int(input('Introduzca el segundo número: '))
        opción = introducirOpción()
        print('\nLISTO\n')
    
    elif opción == '2':
        print('\nEl resultado de la sumatoria es: ' + str(calcularSumatoria(num1,num2)) + '\n')
        opción = introducirOpción()
    
    elif opción == '3':
        print('\n'+ str(num1) + ' libras equivalen a ' + str(convertirLb_Kg(num1)) + ' kilogramos.\n')
        opción = introducirOpción()
   
    elif opción == '4':
        print('\n'+ str(num1) + ' kilogramos equivalen a ' + str(convertirKg_Lb(num1)) + ' libras.\n')
        opción = introducirOpción()
    
    elif opción == '5':
        print('\nLa resultado de la división es: ' + str(dividirNumeros(num1, num2)))
        opción = introducirOpción()

print('\nMuchas gracias')