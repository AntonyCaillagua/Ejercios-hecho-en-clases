print("calculo de precios")
nombre=input("ingresa nombre:")
apellido=input("ingrese apellidos:")
horas=int(input("ingresa horas:"))
precios=int(input("ingrese precios:"))
bruto=horas*precios
tasas=0.25*bruto
neto=bruto-tasas
print("el salario bruto es:",bruto)
print("las tasas son :",tasas)
print("el salario reto es:",neto)