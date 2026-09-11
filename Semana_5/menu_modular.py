# Actividad 4 Menú modular interactivo
# Filiberto Orona Loera
# 7263103

# Menú principal
menu = ("(1). Tuplas\n(2). Diccionarios\n(3). Excepciones\n(4). Strings\n(5). Finalizar\n")                     # Declaré el menú en una variable para que cuando lo quiera imprimir solo llame a la variabe que lo contiene                  
inicio = 1                 # Esta variable la cree para controlar el ciclo while

while inicio ==1:
    print(f"Escoge una de las siguientes opciones:\n{menu}")                                                    
    try:                                                                                # Con este bloque try / except verifico que el usuario no ingrese texto o una entrada vacia
        opcion = int(input("¿Qué quieres hacer?"))                                                               
    except ValueError:
        print("Opción invalida. Por favor escoge un número del 1-5")
    else:                                                                               # Una ves que verificamos que los datos son correctos, entonces el programa envia al usuaro a la sección que eligio mediante el if y elif's anidados dentro de este else
        if opcion == 1:
            print(f"Opción {opcion}: Tuplas\n")
            def suma_tupla(numeros_new):                                    # Declaramos la función para sumar los datos dentro de la tupla y le damos como parametro la tupla con los números que ingreso el usuario
                resultado = 0                                               # Declaramos una variable = 0 que funcionara como acumulador
                for e in numeros_new:                                       # Con este for recorremos los elementos dentro de la tupla
                    resultado = resultado + e                               # Actualizamos el acumulador
                return resultado                                            # Pedimos a la función que retorne el acumulador
            tup = 1                                                         # variable de contro para el ciclo interno de la seccion 1 (Tuplas)
            numeros = (35, 20, 55, 109, 70, 19, 43, 29)
            print(f"Tupla: {numeros}")
            print(f"El tercer elemento de la tupla es: {numeros[2]}")       # Aqui imprimimos el tercer elemento de la tupla solisitando el elemento numero 2 porque python empieza a contar desde 0
            while tup == 1:                                                 # ciclo interno de la seccion 1. para pedir al usuario que vuelva a ingresar valores en caso de que ingrese uno incorrecto
                try:
                    num_1 = int(input("Ingresa un número"))
                    num_2 = int(input("Ingresa otro número"))
                except ValueError:                                          # Usamos el ValueError para mostrar un mensaje, en vez de que se interrumpa el programa
                    print("Valor invalido. Ingresa números enteros")
                else:
                    numeros_new = numeros + (num_1, num_2)                  # Aqui creamos una nueva tupla para agregar los números que solisitamos al usuario
                    lista_num = list(numeros_new)                           # Aqui convertimos la tupla actualizada con los nuevos números a lista, para ordenar los valores mas adelante.
                    lista_num.sort(reverse=True)                            # Aqui usamos .sort() para ordenar la lista y utilizamos la instrucción reverse=True para que el ordenamiento sea de mayor a menor
                    numeros_ord = tuple(lista_num)                          # Aqui convertimos la lista con los números ordenados a tupla
                    print(f"Tupla actualizada: {numeros_new}")
                    print(f"Tupla ordenada: {lista_num}")
                    print(f"La suma de todos los elementos es: {suma_tupla(numeros_new)}")  # Aqui llamamos a la funcion para sumar para imprimir el resultado de la suma
                    tup = 0                                                 # Aqui cambiamos el valor de la variable de control para romper el ciclo interno
            print("________________________________________________________________________________________")
        elif opcion == 2:
            print(f"Opción {opcion}: Diccionarios\n")
            def encontrar_contacto(contactos, nombre):                                  # Declaramos la funcion para buscar contactos dandole de parametros el diccionario y nombre
                return contactos.get(nombre, "Lo siento, no encontré el contacto")      # Aqui usamos get() para buscar claves (nombres) dentro del diccionario y tambien para desplegar un mensaje en caso de que el contacto no este en el diccionario

            contactos = {"Fili": "555-123",
                        "Emilia": "555-098",
                        "Ricardo": "555-106",
                        "Sofía": "555-804",
                        "Fernando": "555-564",
                        "Regina": "555-375"
                        }
            print("Ingresa un nuevo contacto a la agenda")                              
            nuevo_contacto = input("Nombre del nuevo contacto: ")                       # Solicitamos al usuario que ingrese el nombre del nuevo contacto (esto sera la clave)
            nuevo_num = input("Número del nuevo contacto")                              # Ahora solicitamos que ingrese el número de telefono (esto sera el valor)
            contactos [nuevo_contacto.capitalize()] = nuevo_num                         # Aqui agregamos los datos ingresados por el usuario al diccionario entre los [] va lo que sera la clave y despues del = lo que sera el valor. tambien utilizamos capitalize() para convertir la primera letra del nombre en mayúscula por si el usuario no lo hace 
            print("Contactos registrados: ", end="")                                    
            for k in contactos.keys():                                                  # Con este for recorremos las llaves o claves del diccionario con la ayuda de .keys()
                print(k, end=", ")                                                      # Aqui imprimimos los nombres de los contactos que se encuentran en el diccionario
            nombre = input("\nEscribe el nombre del contacto que buscas")               # Aqui pedimos al usuario que ingrse un nombre para pasarselo a la funcion para encontrar contactos más adelante
            tel = encontrar_contacto(contactos, nombre.capitalize())                    # Creamos una variable que almacene el resultado de la funcion y a la funcion le pasamos el nombre del contacto que el usuario busca, aqui tambien usamos .capitalize() para convertir la primer letra en mayúscula en caso de que el usuario ingresara el nombre con minusculas en el paso anterior
            print(f"\nEl contacto de {nombre.capitalize()} es: {tel}")
            print("________________________________________________________________________________________")
        elif opcion == 3:
            print(f"Opción {opcion}: Excepciones\n")
            exc = 1                                                                 # Variable de control para el ciclo interno de la sección 3 (excepciones)
            while exc ==1:                                                                                    
                try:                                                                # Primer bloque try / except 
                    num_1 = int(input("Ingresa un número entero"))                  
                    num_2 = int(input("Ingresa otro número entero"))                # Dentro del try solicitamos al usuario que ingrese dos números y realizamos la suma de los mismos
                    suma = num_1 + num_2
                except ValueError:                                                  # Usamos el ValueError para verificar que los datos sean correctos y mostrar un mensaje, en vez de que se interrumpa el programa en caso de que los datos no sean correctos
                    print("Parece que ingresaste un dato incorrecto. Por favor ingresa solo números enteros")
                else:                                                               # Usamos el else para mostrar el resultado de la suma solo en caso de que no se hayan ingresado datos invalidos
                    print(f"El resultado de {num_1} + {num_2} es: {suma}") 
                    try:                                                            # segundo bloque try / except (dentro del else)
                        dividendo = num_1                                           
                        divisor = num_2                                             # Tras haber verificado que los datos ingresados fueran correctos usamos los mismos numeros que el usuario ingreso para hacer una división
                        division = dividendo / divisor
                        exc = 0                                                     # Cambiamos el valor de la variable de control para salir del ciclo tras una división exitosa
                    except ZeroDivisionError:                                       # Aqui ussamos ZeroDivisionError para mostrar un mensaje en vez de qie el programa se interrumpa en caso de que el usuario ingresara un 0 en el segundo número
                        print(f"{dividendo} ÷ {divisor} = Error de division entre cero.")
                        exc = 0                                                     # Cambiamos el valor de la variable de control para salir del ciclo tras un error de división entre 0
                    else:                                                           # Usamos otro else para mostrar el resultado de la division solo en caso de que no se ingresen datos incorrectos ni haya un error de división entre 0
                        print(f"El resultado de {dividendo} ÷ {divisor} es: {division}")
            print("________________________________________________________________________________________")
        elif opcion == 4:
            print(f"Opción {opcion}: Strings\n")
            def cont_palabras(mensaje):                                             # Definimos una función para contar palabras dandole como parametro mensaje
                palabras = mensaje.split()                                          # creamos una variable para guardar las palabras de la frase y usamos .split() para romper la cadena de texto de la frase en cadenas mas pequeñas. split() rompe cadenas de texto en cadenas mas pequeñas y las guarda en una lista
                return len(palabras)                                                # Le solicitamos a la funcion que retorne la cantidad de elementos dentro de la lista palabras que creamos con split() usando len

            mensaje = "Al que madruga dios lo ayuda"                                # declaramos una variable con una frase dentro
            print(mensaje)                          
            len_mnsj = len(mensaje)                                                 # Aqui usamos len para obtener la longitud de la frase dentro de mensaje esto equivale a la cantidad de caracteres (espacios incluidos)
            upper_mnsj = mensaje.upper()                                            # Aqui usamos .upper() para convertir la frase a mayúsculas
            rplc_mnsj = mensaje.replace("dios lo ayuda", "encuentra todo cerrado")  # Aqui usamos .replace() para cambiar una palabra por otra (en este caso lo usamos para cambiar la segunda parte de la frase y darle un significado distinto)

            print(f"El mensaje tiene {len_mnsj} caracteres")
            print(f"Conversión a mayúsculas: {upper_mnsj}")
            print(f"Intercambio de palabras: {mensaje} -> {rplc_mnsj}")
            print(f"El mensaje tiene {cont_palabras(mensaje)} palabras")
            print("________________________________________________________________________________________")
        elif opcion == 5:
            inicio = 0                                                              # Cambiamos el valor de la variable de control para salir del ciclo principal
            print("Programa finalizado.\nHasta la próxima!")                        # Mensaje de despedida
        else:
            if opcion <1 or opcion >5:                                              # Aqui verificamos que el usuario ingrese un valor dentro de las opciones que ofrece el menú 
                print("opción invalida. Por favor escoge un número del 1-5")