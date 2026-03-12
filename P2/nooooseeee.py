"""
Clase Restaurante con menu, reservaciones y manejo de ordenes
"""

#Listas y diccionarios
menu = []
ordenes = []
reservaciones = {}


opcion=0
while opcion!=7:
    print("Opciones disponibles")
    print("1-crear un platillo")
    print("2-mostrar menu")
    print("3-hacer reservaciones")
    print("4-tomar ordenes")
    print("5-mostrar ordenes")
    print("6-Mostrar el listado de reservaciones")
    print("7-Salir")
    opcion = int(input("selecciona una de las opciones: "))

    #1 Agregar platillo al menu
    if opcion == 1:
        nombre = input("como se llama el platillo: ")
        precio = input("cuanto va a costar: ")
        menu.append([nombre, precio])
        print("Platillo agregado al menu")

    #2 Mostrar menu
    elif opcion == 2:
        print("MENU DEL RESTAURANTE")
        for platillo in menu:
            print("Nombre:", platillo[0], "Precio:", platillo[1])

    #3 Hacer reservaciones
    elif opcion == 3:
        cliente = input("Nombre del cliente: ")
        hora = input("Hora de la reservacion: ")
        reservaciones[cliente] = hora
        print("Reservacion guardada")


    #4 Tomar ordenes
    elif opcion == 4:
        cliente = input("Nombre del cliente: ")
        platillo = input("Que platillo quiere: ")
        ordenes.append({"cliente": cliente, "platillo": platillo})
        print("Orden guardada")
        menu=[
    ["pozole",340],
    ["enmoladas",-76],
    ["tacos",-65],
    ["bistec",-90],
]

    #5 Mostrar ordenes
    elif opcion == 5:
        print("ORDENES:")
        for orden in ordenes:
            print(orden["cliente"], "pidio", orden["platillo"])

    #6 Mostrar reservaciones
    elif opcion == 6:
        print("LISTA DE RESERVACIONES")
        for cliente, hora in reservaciones.items():
            print(cliente, "->", hora)

    else:
        print("Opcion no valida")