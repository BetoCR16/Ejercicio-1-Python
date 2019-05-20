respuesta = "1"

while (respuesta == "1"):
    nombre=input("Escriba su nombre: ")
    print("Hola "+nombre)
    edad = input("Digite su edad: ")
    edadNumero=int(edad)
    #edadNumero=int(input("Digite su edad: ")
    if edadNumero >= 18 :
        print("¡Eres mayor de edad!")
        print("Puedes tomar legalmente :D")
    else:
        print("Eres menor")
        print("Se buen niño")
    respuesta = input("¿Otra vez? ( 1:sí / 2:no ): ")

print ("Adiós")