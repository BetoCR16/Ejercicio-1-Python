listaEdades = []
respuesta = len(listaEdades)
nombre=input("Escriba su nombre: ")
print("Hola "+ nombre)
while (len(listaEdades) <= 10):
    edad = input("Digite una edad: ")
    edadNumero=int(edad)
    listaEdades.append(edadNumero)

print ("Listo")

#-------------------------------------- Promediar edades ------------------------------
suma = 0
cantidadesDeEdades = len(listaEdades)
for edad in range(0, cantidadesDeEdades):
    suma = suma + listaEdades[edad]
promedio = suma / len(listaEdades)
print("El prmedio de edades es " + str(promedio))

