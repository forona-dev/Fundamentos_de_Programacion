# Filiberto Orona Loera
# 7263103
# 03/09/2026
                                                                        # Actividad 3: Tabla de pitágoras

# Saludo
print("¡Hola!\nCon este programa podrás realizar multiplicaciones de 2 factores usando una tabla de Pitágoras")

# Declaración de la matriz
tabla = []                                                                                 # Esta va a ser la matriz donde voy a construir la tabla pitagorica
# verificacion de datos
while True:                                                                                
    dimension = (input("¿Cuántas filas y columnas quieres que tu tabla de Pitágoras tenga?"))    # Con este input el usuario puede escoger el tamaño de la tabla   
    if dimension.isdigit():                                                                # La función de .isdigit() la vimos en un ejercicio de la materia computación en la nube. Aqui la estoy usando para verificar que el dato ingresado sea un numero entero y positivo. *Nota si ingreso un número con .0 (ej. 3.0) no lo considera como entero
        dimension = int(dimension)                                                         # Aqui cambio el tipo de dato de str a int, ya que lo necesito como un dato númerico más adelante. * Nota .isdigit() solo funciona con datos de texto (str)
        break
    else:
        print("Por favor selecciona un número entero y positivo")                          # Aqui solicito al usuario que ingrese un dato correcto de ser necesario.
        

# Construccion de la tabla de pitágoras
for fila in range(dimension +1):            # Con este for determinamos el limite de las filas * Nota agregue un +1 porque el programa empieza a contar desde 0
    fila_actual =[]                         # Aqui creamos una lista vacia para guardar los datos que se desplegaran en las filas
    for columna in range(dimension +1):     # Con este for determinamos el limite de las columnas
        valor = fila * columna              # Aqui guardamos el resultado de la multiplicación de las filas * las columnas. Esto es lo que le da el formato de tabla de pitágoras a la matriz
        fila_actual.append(valor)           # Agrega el resultado de la multiplicación a la lista fila_actual
    tabla.append(fila_actual)               # Agrega toda la fila a la lista principal (tabla) para formar la matriz


# Despliegue de la tabla       
for c in range(dimension +1):               # Este for recorre todos los números del 0 hasta lo que el usuario ingrese en dimension
    print("\t", c, end="")                  # Aqui imprimimos el indice superior de la tabla, que muestra el numero de cada columna
print("\n")                                 # Un salto de renglon para separar el indice de la tabla
for f in range(dimension+1):                # Este for recorre todas las filas desde 0 hasta el valor de dimension 
    print(f, end="\t ")                     # Aqui imprimimos el indice lateral de la tabla, este muestra el número de cada fila
    for c in range(dimension+1):            # 
        print(tabla [f][c], end="\t ")      # Imprime la matriz dandole un formato donde cada valor esta separado por un tabulador
    print()                                 # Crea un salto de linea al final de cada fila


# Selección de coordenadas, verficación, busqueda de datos y despliegue de resultados
while True:
    coordenada_1 = (input(f"Escoge un número del 0-{dimension}"))                               
    coordenada_2 = (input(f"Escoge otro número del 0-{dimension}"))                             # En estos pasos le pido al usuario que ingrese las coordenadas que usaremos para encontrar el resultado de la multiplicacion en la tabla. (las coordenadas son los numeros que queremos multiplicar)
    if coordenada_1.isdigit() and coordenada_2.isdigit():                                       # Aqui volvemos a usar .isdigit() para verificar que los datos ingresados sean correctos (positivo y entero)
        coordenada_1 = int(coordenada_1)                                                        
        coordenada_2 = int(coordenada_2)                                                        # Aqui convertimos las coordenadas de str a int 
        break
    else:
        print("Coordenadas invalidas.\nPor favor ingresa numeros enteros y positivos")          # Aqui pedimos al usuario que ingrese datos correctos de ser necesario
while True:
    if coordenada_1 > dimension or coordenada_2 > dimension:                                    # Aqui verificamos que las coordenadas ingresadas no exceda el limite de la tabla
        print(f"Coordenadas invalidas.\nPor favor selecciona numeros del 0 al {dimension}")     # Pedimos al usuario que ingrese datos correctos
    else:
        print(f"\nEl resultado de la multiplicación de {coordenada_1} X {coordenada_2} es: {tabla[coordenada_1][coordenada_2]}")        # Aqui desplegamos el resultado de la multiplicación buscando el valor de la tabla contenido en las coordenadas ingresadas 
        break