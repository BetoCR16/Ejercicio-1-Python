respuesta = "1"
nombre=input("Escriba su nombre: ")
listaEdades = []
suma = 0
while (respuesta == "1"):
    print("Hola "+nombre)
    edad = input("Digite su edad: ")
    edadNumero=int(edad)
    listaEdades.append(edadNumero)
    if edadNumero >= 18 :
        print("¡Eres mayor de edad!")
        print("Puedes tomar legalmente :D")
    else:
        print("Eres menor")
        print("Se buen niño")
    respuesta = input("¿Otra vez? ( 1:sí / 2:no ): ")

print ("Adiós")
for edad in listaEdades:
    suma = suma + edadNumero

promedio = suma / len(listaEdades)
print(promedio)
#Promediar edades