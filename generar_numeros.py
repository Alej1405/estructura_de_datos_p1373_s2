import time

#creamos el array que contiene todos los numeros
numeros = list(range(1, 1_000_001))

#prueba para verificar que el array funcione
#print(f"lista de numeros: '{numeros}'")

#generamos la opcion del numero que el usuario va a buscar.
buscar = int(input("Ingresa el número a buscar: "))

#busqueda secuencial o de uno en uno
inicio = time.time()

if buscar in numeros:
    print(f"{buscar} encontrado en la posición {numeros.index(buscar)} tardo ")
else:
    print(f"{buscar} no está en la lista")

fin = time.time()
print(f"Tiempo de búsqueda: {fin - inicio:.6f} segundos")
#fin de la busqueda en secuencial.

#busqueda binaria
inicio_binaria = time.time()

izquierda, derecha = 0, len(numeros) - 1
posicion = -1
while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if numeros[medio] == buscar:
        posicion = medio
        break
    elif numeros[medio] < buscar:
        izquierda = medio + 1
    else:
        derecha = medio - 1

fin_binaria = time.time()

if posicion != -1:
    print(f"{buscar} encontrado en la posición {posicion} (binaria)")
else:
    print(f"{buscar} no está en la lista (binaria)")

print(f"Tiempo de búsqueda binaria: {fin_binaria - inicio_binaria:.6f} segundos")
#fin de la busqueda binaria