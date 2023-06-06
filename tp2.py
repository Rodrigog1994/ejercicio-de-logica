nombre_archivo = input("ingrese un nombre de archivo para analizar:")
sigue = True

try:
    archivo = open(nombre_archivo, "r")
except:
    sigue = False
    print("archivo no enconctrado!")

if sigue == True:
    contenido = archivo.readlines()

    cantidad _caracteres = 0
    for parrafo in contenido:
        cantidad_caracteres = cantidad _caracteres + len(parrafo)

print ("Cantidad de caracteres: ", cantidad_caracteres)
print("cantidad de párrafos: ", len(contenido))
archivo.close()    