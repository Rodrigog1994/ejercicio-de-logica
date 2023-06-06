nombre_archivo = input("Ingrese el nombre del archivo:")

try:
    with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()

    lineas = contenido.count('\n') + 1
    palabras = len(contenido.split())
    caracteres = len(contenido)

    palabras_lista = contenido.split()
    palabra_mas_larga = max(palabras_lista, key=len)
    largo_palabra_mas_larga = len(palabra_mas_larga)

    oraciones = contenido.split('.')
    oracion_mas_larga = max(oraciones, key=len)
    cantidad_palabras_oracion_mas_larga = len(oracion_mas_larga.split())

    parrafos = contenido.split('\n\n')
    parrafo_mas_largo = max(parrafos, key=len)
    cantidad_palabras_parrafo_mas_largo = len(parrafo_mas_largo.split())
    cantidad_oraciones_parrafo_mas_largo = parrafo_mas_largo.count('.') + 1

    print("Cantidad de líneas:", lineas)
    print("Cantidad de palabras:", palabras)
    print("Cantidad de caracteres:", caracteres)
    print("Palabra más larga:", palabra_mas_larga)
    print("Largo de la palabra más larga:",largo_palabra_mas_larga)
    print("oración más larga:", oracion_mas_larga)
    print("Cantidad de palabras en la oración más larga:",cantidad_palabras_oracion_mas_larga)
    print("Párrafo más largo:", parrafo_mas_largo)
    print("Cantidad de palabras en el párrafo más largo:", cantidad_palabras_parrafo_mas_largo)
    print("Cantidad de oraciones en el párrafo más largo:", cantidad_oraciones_parrafo_mas_largo)

except FileNotFoundError:
      print ("No se encuentra el archivo:", nombre_archivo)

    
