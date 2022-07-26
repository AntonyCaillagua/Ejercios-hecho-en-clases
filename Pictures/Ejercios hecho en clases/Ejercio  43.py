def keyw(**datos):
    print("\nTipo de datos del argumento:",type(datos))
    for key,value in datos.items():
        print("{} is {}".format(key, value))
keyw(Firstname="juan",Lastname="Dominguez",Age=42,Phone=1234567890)
keyw(Firstname="Jhon",Lastname="Wood",Email="johwwo@nomail.com",Country="Wakanda")

