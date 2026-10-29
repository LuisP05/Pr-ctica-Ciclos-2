opcion = ""
while opcion != "salir":
    opcion = input("Escribe 'hola' o 'salir': ")
    if opcion == "hola":
        print("¡Hola, mucho gusto!")
    elif opcion == "salir":
        print("Hasta luego")
    else:
        print("Opción no válida")