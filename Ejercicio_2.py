#print ('Escoja una opción:\n 1. Ingresar 2 números\n 2. Calcular sumatoria\n 3. Convertir de kg a libras\n 4. Calcular de libras a kilogramos\n 5. Dividir los números\n 6. Salir')

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

