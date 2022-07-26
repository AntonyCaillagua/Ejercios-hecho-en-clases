filas=int(input("Ingrese numero de filas:"))
columnas=int(input("Ingrese numero de columnas:"))
for i in range(filas+1):
    filas(i)
    for j in range(columnas+1):
        columnas(j)
        multiplicacion=0
        multiplicacion=filas*columnas
print(multiplicacion)
