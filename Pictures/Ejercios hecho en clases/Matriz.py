from random import randint
f=int(input("Ingrese la cantidad de filas:"))
c=int(input("Ingrese la cantidad de columnas:"))
m=[]

for i in range(f):
     m.append([])
     for j in range(c):
         m[i].append(randint(1,100))
for i in range(f):
    for j in range(c):
        print(m[i][j],end=" ")
    print(" ")
x=int(input("Digite columna a obtener:"))
g=[]
for i in range(len(m) ):
    g.append(m[i][j])
    sum+= g
print(g)
