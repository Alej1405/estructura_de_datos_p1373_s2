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