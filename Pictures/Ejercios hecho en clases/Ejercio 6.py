print("Calculo de impuesto y salarios ")
nombre=input("Ingresa su nombre:")
horas=int(input("Ingresa el numero de horas "))
precios=int(input("Ingresa el numero de trabajo :"))

bruto=horas*precios
tasas=0.25*bruto
neto=bruto-tasas
print("La respuesta del bruto es:",bruto)
print("La respuesta de tasas es ",tasas)
print("La respesta de neto es:",neto)