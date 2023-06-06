numeros = []
ordinales = ('primer', 'segundo', 'tercero', 'cuarto', 'quinto', 'sexto')

for iterador in range(6):
    leyenda = "Ingrese el " + ordinales[iterador] + " número: "
    numero = input(leyenda)
    
    try:  
        numeros.append(float(numero))
    except:
        print("Solo se aceptan números, por lo tanto su ingreso será tomado como 0")
        numeros.append(0)

suma = 0
producto = 1

for valor in numeros:
    suma += valor
    producto *= valor

print('\n' * 2)
print('El número mayor es:', max(numeros))
print('El número menor es:', min(numeros))
print('La suma de todos los números es:', suma)
print('El producto de todos los números es:', producto)
print('\n' * 2)