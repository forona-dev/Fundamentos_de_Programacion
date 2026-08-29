menu = "¿Qué quieres hacer?\n 1: Capturar ingreso\n 2: Capturar egreso\n 3: Imprimir reporte\n 4: Cierre mensual\n 5: Salir\n"
print(f"{menu}")
while True: #1
    op = input(("Selecciona una opción del 1-5"))
    if op != "1" and op != "2" and op != "3" and op != "4" and op != "5":
        print("\n***Seleccione una opción valida***\n")
    else:    
        if op == "1":
            while True: #2
                print("\nINGRESOS\n")
                fecha_i = input("Fecha (dd/mm/aa)")
                print(f"Fecha: {fecha_i}")
                cant_i = float(input("Cantidad ($)"))
                print(f"Ingreso: ${cant_i}")
                concept_i = input("Concepto")
                print(f"Concepto: {concept_i}")
                # Guardar la información en la BD de ingresos
                while True: #3
                    agregar_i = input(print("¿Desea agregar otro ingreso?\n s para sí\n n para no"))
                    if agregar_i != "s" and agregar_i!= "S" and agregar_i != "n" and agregar_i != "N":
                        print("\n***Opción invalida***\n")
                    else:
                        break
                if agregar_i == "n" or agregar_i == "N":
                    break         
        if op == "2":
            while True:
                print("\nEGRESOS\n")
                fecha_e = input("Fecha (dd/mm/aa)")
                print(f"Fecha: {fecha_e}")
                cant_e = float(input("Egreso"))
                print(f"Egreso: ${cant_e}")
                concept_e = (input("Concepto"))
                print(f"Concepto: {concept_e}")
                # Guardar la información en la BD de egresos
                while True:
                    agregar_e = input(print("¿Desea agregar otro egreso?\n s para sí\n n para no"))
                    if agregar_e != "s" and agregar_e != "S" and agregar_e != "n" and agregar_e != "N":
                        print("\n***Opcion invalida***\n")
                    else:
                        break
                if agregar_e == "n" or agregar_e == "N":
                    break
        if op == "3":
            while True:
                print("\nREPORTE\n")
                print("Aqui voy a imprimir las BDs de ingresos y egresos")
                break
        if op == "4":
            while True:
                print("\nCIERRE\n")
                print("Aqui va el total de ingresos")
                print("Aqui va el total de egresos")
                print("Aqui va el total de Ingresos - Egresos")
                # Limpiar BD    
                break
        if op == "5":
            print("\nProceso finalizado")
            break
        