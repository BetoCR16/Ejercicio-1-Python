import time
#------------------------------ Funciones --------------------------------------------
def introducirOpción():
    time.sleep(1.5)
    opción = input ('\nEscoja una opción:\n 1. Ingresar 2 números\n 2. Calcular sumatoria\n 3. Convertir de libras a kg\n 4. Convertir de kg a libras\n 5. Dividir los números\n 6. Salir\n \n Su opción: ')
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
    solucion = num1 / num2
    return solucion

#----------------------------------------- Programa Principal -------------------------------------------------------

opción = input ('Escoja una opción:\n 1. Ingresar 2 números\n 2. Calcular sumatoria\n 3. Convertir de kg a libras\n 4. Calcular de libras a kilogramos\n 5. Dividir los números\n 6. Salir\n \n Su opción: ')

while (opción != '6'):
#------------------------------------------ Introducir números ------------------------------------------    
    if opción == '1':
        num1 = int(input('Introduzca el primer número: '))
        num2 = int(input('Introduzca el segundo número: '))
        opción = introducirOpción()
        
#------------------------------------------ Sumatoria --------------------------------------------------------------    
    elif opción == '2':
        print('\nEl resultado de la sumatoria es: ' + str(calcularSumatoria(num1,num2)) + '\n')
        opción = introducirOpción()
#------------------------------------------ Conversión lb - kg ---------------------------------------------------    
    elif opción == '3':
        print('\n'+ str(num1) + ' libras equivalen a ' + str(convertirLb_Kg(num1)) + ' kilogramos.\n')
        opción = introducirOpción()
#----------------------------------------- Conversión kg - lb -------------------------------------   
    elif opción == '4':
        print('\n'+ str(num1) + ' kilogramos equivalen a ' + str(convertirKg_Lb(num1)) + ' libras.\n')
        opción = introducirOpción()
#----------------------------------------- División ----------------------------------------------------    
    elif opción == '5':
        if num2 == 0:
            print('\nError, Segundo número no puede ser cero\n')
        else:
            print('\nLa resultado de la división es: ' + str(dividirNumeros(num1, num2)))
        opción = introducirOpción()

print('\nMuchas gracias por usar este programa.\n¡Tenga un bonito día! :D')
time.sleep(5)