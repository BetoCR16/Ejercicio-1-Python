respuesta = "1"
nombre=input("Escriba su nombre: ")
listaEdades = []
print("Hola "+nombre)
while (respuesta == "1"):
    edad = input("Digite una edad: ")
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

#-------------------------------------- Promediar edades ------------------------------
suma = 0
cantidadesDeEdades = len(listaEdades)
for edad in range(0, cantidadesDeEdades):
    suma = suma + listaEdades[edad]
promedio = suma / len(listaEdades)
print("El prmedio de edades es " + promedio)

