# Filiberto Orona Loera
# 7263103
# 21/08/2026
#                                                           Actividad 2
while True:
    # Bienvenida y menú de precios y descuentos
    print("Bienvenido al Museo de Antropología e Historia")
    print("\nCostos:")
    print("Menores de 3 años: $0 \t Menores de edad (3-17 años): $30 \t Mayores de edad: $45\n")
    print("descuentos:")
    print("Estudiantes: 10% \t Maestreos: 10% \t Adultos mayores (60 +): 12%")
# Variables 
    contador = 0                                                                        # Aqui voy sumando el numero de visitantes
    visitantes = 0                                                                      # Reinicia el valor de visitantes a "0" en caso de que el usuario se equivoque e inicie de nuevo                 
    total = 0                                                                           # Aqui voy sumando el total a pagar de todas las entradas
    visitantes = int(input("¿Cúantas personas visitaran el museo?"))                    # Aqui el usuario ingresa la cantidad de personas que visitaran el museo
    for contador in range(1, visitantes+1):                                             # Aqui se empiezan a procesar los visitantes, for repite el programa segun el numero de visitantes ingresado por el usuario (for empieza a contar desde "0" entonces agregue un +1 a visitantes)
        edad = int(input(f" ¿Cúal es la edad del visitante: {contador}" ))              # Aqui voy filtrando a los visitantes segun su edad para determinar el costo de sus entradas y si aplica algun descuento por edad (adulto mayor o menor de 3 años)
        if edad >=60:
            precio = 45        
            descuento = precio - (precio * 0.12)
            total = total + descuento
            print(f"\nVisitante {contador}" "\n Aplica descuento de adulto mayor: (12%)" f"\n Entrada: ${descuento:.2f}")
            print("=========================================\n")
            continue
        if edad <3:
            print(f"Visitante {contador}" "\n Menor de 3 años \n Entrada gratuita: $0.00")
            print("=========================================\n")
            total = total +0
        else:
            if edad <=17:
                precio = 30
                estudiante = input("¿Tienes credencial de estudiante?")                 # Aqui verifico si el visitante menor de edad es elegible para un descuento de estudiante
                if estudiante =="si":
                    descuento = precio - (precio * 0.10)
                    total = total + descuento
                    print(f"Visitante {contador}" "\n Aplica descuento de estudiante (10%)" f"\n Entrada: ${descuento:.2f}")
                    print("=========================================\n")
                else:                                                                   # Aqui entran los visitantes que son menores de edad, pero no fueron elegibles para el descuento
                    total = total + precio
                    print(f"Visitante {contador}" "\n No aplica descuento" f"\n Entrada: ${precio:.2f}")
                    print("=========================================\n")
            else:                                                                       # Aqui entran los visitantes que son mayores de edad, pero no fueron elegibles para el descuento de adulto mayor
                precio = 45
                opcion_1 = input("¿Tienes credencial de estudiante?")                   # Aqui verifico si el visitante mayor de edad es elegible para descuento de estudiante
                if not opcion_1 ==  "si":                                               # Aqui usé el operador not para condicionar la siguiente pregunta solo en caso de que la respuesta a la pregunta anterior sea "no"
                    opcion_2 = input("¿Eres maestro?")                                  # Aqui verifico si el visitante mayor de edad es elegible para un descuento de maestro
                if opcion_1 == "si" or opcion_2 == "si":                                # Aqui como el descuento de estudiante y maestro es el mismo usé el operador "or" para calcular el descuento
                    descuento = precio - (precio * 0.10)
                    total = total + descuento
                    if opcion_1 == "si":                                                # Este paso es para que se muestre el descuento correcto
                        print(f"Visitante {contador}" "\n Aplica descuento de estudiante (10%)" f"\n Entrada: ${descuento:.2f}")
                        print("=========================================\n")
                    elif opcion_2 == "si":
                        print(f"Visitante {contador}" "\n Aplica descuento de maestro (10%)" f"\n Entrada: ${descuento:.2f}")
                        print("=========================================\n")
                else:                                                                   # Aqui entran los visitantes mayores de edad que no fueron elegibles para ningun descuento
                    total = total + precio
                    print(f"Visitante {contador}" "\n No aplica descuento" f"\n Entrada: ${precio:.2f}")        
                    print("=========================================\n")         
    print(f"El total a pagar por {visitantes} visitante(s) es de: ${total:.2f}")        # Aqui muestro el total de todas las emtradas
    confirmar_datos = input("\n¿Sus datos son correctos?")                              # Aqui pido al usuario que confirme que la informacion mostrada sea correcta
    if confirmar_datos == "si":                                                         # Si la info. no es correcta el ciclo comienza de nuevo, si sí es correcta el ciclo termina y el programa se cierra
# Despedida
        print("=========================================\n")   
        print("Gracias por visitar el Museo de Antropología e Historia \n¡Disfrute(n) su recorrido!")
        break