dinero=anios=interes=0
while (dinero <500):
    dinero=float(input("ingrese la cantidad de dinero inicial:"))
while (anios <=0):
    anios=int(input("ingrese el tiempo(años):"))
while (interes <=0 or interes >10):
    interes=float(input("ingrese el intteres:"))
for i in range (1,anios*12+1):
    dinero +=(dinero*interes)/100
    print(f"total de la poliza:{round(dinero,2)}")
    