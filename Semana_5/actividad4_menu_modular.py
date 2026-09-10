# Actividad 4 Menú modular interactivo
# Filiberto Orona Loera
# 7263103

# Menú principal
menu = ("(1). Tuplas\n(2). Diccionarios\n(3). Excepciones\n(4). Strings\n(5). Finalizar\n")
inicio = 1

while inicio ==1:
    print(f"Escoge una de las siguientes opciones:\n{menu}")
    try:
        opcion = int(input("¿Qué quieres hacer?"))
    except ValueError:
        print("Opción invalida. Por favor escoge un número del 1-5")
    else:
        if opcion == 1:
            print(f"Opción {opcion} Tuplas\n")

            print("____________________________________________________________________________")
        elif opcion == 2:
            print(f"Opción {opcion} Diccionarios\n")

            print("____________________________________________________________________________")
        elif opcion == 3:
            print(f"Opción {opcion} Excepciones\n")

            print("____________________________________________________________________________")
        elif opcion == 4:
            print(f"Opción {opcion} Strings\n")

            print("____________________________________________________________________________")
        elif opcion == 5:
            inicio = 0
            print("Programa finalizado.\nHasta la próxima!")
        else:
            if opcion <1 or opcion >5:
                print("opción invalida. Por favor escoge un número del 1-5")