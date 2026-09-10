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
            print(f"Opción {opcion}: Tuplas\n")
            def suma_tupla(numeros_new):
                resultado = 0
                for e in numeros_new:
                    resultado = resultado + e
                return resultado

            numeros = (35, 20, 55, 109, 70, 19, 43, 29)
            print(f"Tupla: {numeros}")
            print(f"El tercer elemento de la tupla es: {numeros[2]}")
            try:
                num_1 = int(input("Ingresa un número"))
                num_2 = int(input("Ingresa otro número"))
            except ValueError:
                print("Valor invalido. Ingresa números enteros")
            else:
                numeros_new = numeros + (num_1, num_2)
            lista_num = list(numeros_new)
            lista_num.sort(reverse=True)
            numeros_ord = tuple(lista_num)
            
            print(f"Tupla actualizada: {numeros_new}")
            print(f"Tupla ordenada: {lista_num}")
            print(f"La suma de todos los elementos es: {suma_tupla(numeros_new)}")
            print("____________________________________________________________________________")
        elif opcion == 2:
            print(f"Opción {opcion}: Diccionarios\n")
            def encontrar_contacto(contactos, nombre):
                return contactos.get(nombre, "Lo siento, no encontré el contacto")

            contactos = {"Fili": "555-123",
                        "Emilia": "555-098",
                        "Ricardo": "555-106",
                        "Sofía": "555-804",
                        "Fernando": "555-564",
                        "Regina": "555-375"
                        }
            print("Ingresa un nuevo contacto a la agenda")
            nuevo_contacto = input("Nombre del nuevo contacto: ")
            nuevo_num = input("Número del nuevo contacto")
            contactos [nuevo_contacto.capitalize()] = nuevo_num
            print("Contactos registrados: ", end="")
            for k in contactos.keys():
                print(k, end=", ")
            nombre = input("\nEscribe el nombre del contacto que buscas")
            tel = encontrar_contacto(contactos, nombre.capitalize())
            print(f"\nEl contacto de {nombre.capitalize()} es: {tel}")
            print("____________________________________________________________________________")
        elif opcion == 3:
            print(f"Opción {opcion}: Excepciones\n")

            print("____________________________________________________________________________")
        elif opcion == 4:
            print(f"Opción {opcion}: Strings\n")
            def cont_palabras(mensaje):
                palabras = mensaje.split()
                return len(palabras)

            mensaje = "Al que madruga dios lo ayuda"
            print(mensaje)
            len_mnsj = len(mensaje)
            upper_mnsj = mensaje.upper()
            rplc_mnsj = mensaje.replace("dios lo ayuda", "encuentra todo cerrado")

            print(f"El mensaje tiene {len_mnsj} caracteres")
            print(f"Conversión a mayúsculas: {upper_mnsj}")
            print(f"Intercambio de palabras: {mensaje} -> {rplc_mnsj}")
            print(f"El mensaje tiene {cont_palabras(mensaje)} palabras")
            print("____________________________________________________________________________")
        elif opcion == 5:
            inicio = 0
            print("Programa finalizado.\nHasta la próxima!")
        else:
            if opcion <1 or opcion >5:
                print("opción invalida. Por favor escoge un número del 1-5")