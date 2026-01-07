from sw_functions.fn_expenses import *
from sw_functions.funciones_genericas import *
from sw_functions.fn_usuarios import *
from sw_functions.constantes import *
from datos.diccionarios import *

# variable para guardar el DNI del usuario logeado
user_logged_id = ""
user_logged = {}

# ---------- FLAGS ----------
salir = False
flg_menu_login = True
flg_iniciar_sesion = False
flg_menu_principal = False
flg_menu_ver_gastos = False
flg_menu_gestionar_personas = False
flg_crear_usuario = False
flg_menu_gasto = False
flg_menu_gasto_concepto = False
flg_menu_gasto_total = False
flg_menu_gasto_pagador = False
flg_menu_gasto_tipo_division = False
flg_menu_gasto_categoria = False
flg_menu_gasto_division = False
flg_menu_gasto_participantes = False
flg_menu_gasto_guardar = False
flg_menu_saldos = False
flg_menu_saldos_deber = False
flg_menu_saldos_haber = False
flg_menu_saldos_persona = False
flg_menu_saldos_marcar_pagados_gastos = False
flg_menu_saldos_resumen = False



while not salir:
    while flg_menu_login:
        get_cabecera(splitwise_title,100,"*")
        opcion_login = get_menu(menu_login)

        if opcion_login == 1:
            flg_menu_login = False
            flg_iniciar_sesion = True
        elif opcion_login == 2:
            flg_menu_login = False
            flg_crear_usuario = True
        elif opcion_login == 3:
            flg_menu_login = False
            salir = True

    while flg_iniciar_sesion:

        get_cabecera(iniciar_sesion_title,100,"=")
        #print(menu_iniciar_sesion)
        # se pide dni
        user_logged_id = login_user(usuarios)

        if user_logged_id is None:
            flg_iniciar_sesion = False
            flg_menu_login = True
        else:
            user_logged = usuarios[user_logged_id]

            flg_iniciar_sesion = False
            flg_menu_principal = True
            print("login correcto. Bienvenido " + user_logged["nombre"])
            input(oEnterToContinue)

    while flg_crear_usuario:

        get_cabecera(crear_usuario_title, 100, "*")
        nuevo_usuario = create_user(usuarios)
        if not isinstance(nuevo_usuario, dict):
            print("¡User has not been created!")
            input(oEnterToContinue)
            flg_crear_usuario = False
            flg_menu_principal = True
        else:
            usuarios[nuevo_usuario["username"]] = nuevo_usuario

            print("¡User created successfully! You can now login.")
            input(oEnterToContinue)
            flg_crear_usuario = False
            flg_menu_login = True

    # MENU PRINCIPAL
    while flg_menu_principal:

        get_cabecera(menu_principal_title,100, "*")

        print("Hi, " + user_logged["nombre"] + "\n")
        opc = get_menu(menu_principal)

        # 1. NUEVO GASTO
        if opc == 1:
            flg_menu_principal = False
            flg_menu_gasto = True
            expense_dict = {"descripcion": "", "categoria": [], "total": 0, "participantes": [],"estado": 0, "division":0}
            cuotas_pendientes ={}

        # 2. VER GASTOS
        elif opc == 2:
            flg_menu_principal = False
            flg_menu_ver_gastos = True

        # 3. SALDOS Y DEUDAS
        elif opc == 3:
            flg_menu_principal = False
            flg_menu_saldos = True

        # 4. GESTIONAR PERSONAS
        elif opc == 4:
            flg_menu_principal = False
            flg_menu_gestionar_personas = True

        # 5. SALIR (Cerrar sesión)
        elif opc == 5:
            flg_menu_principal = False
            flg_menu_login = True
            user_logged_id = ""
            user_logged = {}

    while flg_menu_gasto:

        get_cabecera(menu_nuevo_gasto_title,  100, "*")
        opcion = get_menu(menu_nuevo_gasto)
        if opcion == 9:
            flg_menu_gasto= False
            flg_menu_principal = True
            expense_dict.clear()
            cuotas_pendientes.clear()
        elif opcion == 8:
            flg_menu_gasto = False
            flg_menu_gasto_guardar = True
        elif opcion == 7:
            flg_menu_gasto = False
            flg_menu_gasto_division = True
        elif opcion == 6:
            flg_menu_gasto = False
            flg_menu_gasto_categoria = True
        elif opcion == 5:
            flg_menu_gasto = False
            flg_menu_gasto_participantes = True
        elif opcion == 4:
            flg_menu_gasto = False
            flg_menu_gasto_pagador = True
        elif opcion == 3:
            flg_menu_gasto = False
            flg_menu_gasto_tipo_division = True
        elif opcion == 2:
            flg_menu_gasto = False
            flg_menu_gasto_total = True
        elif opcion == 1:
            flg_menu_gasto = False
            flg_menu_gasto_concepto = True

    while flg_menu_gasto_concepto:

        #########################  NEW Concept  #######################################
        expense_dict["descripcion"] = set_expense_description()

        # volver al menu de gastos
        flg_menu_gasto_concepto = False
        flg_menu_gasto = True

    while flg_menu_gasto_total:
        #########################  Añadir total  #######################################
        expense_dict["total"] = set_expense_amount()

        #volver al menu de gastos
        flg_menu_gasto_total = False
        flg_menu_gasto = True

    while flg_menu_gasto_pagador:
        #########################  Definir pagador #######################################

        expense_dict["pagador"] = get_user_from_list(usuarios)

        #print(expense_dict)

        #volver al menu de gastos
        flg_menu_gasto_pagador = False
        flg_menu_gasto = True

    while flg_menu_gasto_tipo_division:

        print("La división equitativa es la asignada por defecto, "
              "si quiere modificar esta opción, seleccione otra o mantenga la actual".center(100))

        idTipusDiv = get_element_from_list(tipo_division, "Choose type of division:")
        if not int(idTipusDiv) < 0 and int(idTipusDiv) < len(tipo_division):
            expense_dict["division"] = idTipusDiv


        #
        # __tipodivisionOK = False
        # __idTipusDiv = -1
        #
        # while not __tipodivisionOK:
        #     print("Elegir modalidad de división:\n")
        #     for i in range(len(tipo_division)):
        #         print("{}) {}".format((i + 1), tipo_division[i]))
        #
        #     __tipusDiv = input("Con que forma desea dividir el gasto:")
        #
        #     if not __tipusDiv.isdigit():
        #         if __tipusDiv == "":
        #             print("VACIO!! No has seleccionado ninguna modalidad")
        #             if input("Desea volver al menú anterior  SI/no?").lower() == "si":
        #                 __tipodivisionOK = True
        #     elif int(__tipusDiv) in range(1,len(tipo_division)+1):
        #         __idTipusDiv = int(__tipusDiv)
        #         __tipodivisionOK = True
        #     else:
        #         print(oOutRange)
        #
        # if not int(__idTipusDiv) < 0 and int(__idTipusDiv) < len(tipo_division):
        #     expense_dict["division"] = __idTipusDiv

        #volver al menu de gastos
        flg_menu_gasto_tipo_division = False
        flg_menu_gasto = True

    while flg_menu_gasto_categoria:

        __categoriaOK = False
        __categorias = []
        __idCat = 0

        while not __categoriaOK:
            lst_categorias = []
            for clave in categorias:
                print("{}) {}".format((len(lst_categorias)+1),categorias[clave]))
                lst_categorias.append(clave)

            __cat = input("Seleccione una categoría, o ingrese una categoría nueva")

            if not __cat.isdigit():
                if __cat == "":
                    print("VACIO!! No has seleccionado ninguna categoría")
                    if input("Desea volver al menú anterior  SI/no?").lower() == "si":
                        __categoriaOK = True
                else:
                    #__add_categoria = input("Desea añadir \"{}\" como nueva categoria? SI/no:  ".format(__cat))
                    if input("Desea añadir \"{}\" como nueva categoria? SI/no:  ".format(__cat)).lower() == "si":
                        __categoriaOK = True
                        __idCat=len(categorias)+1
                        categorias[__idCat]=__cat
            elif int(__cat) in lst_categorias:
                __idCat=__cat
                __categoriaOK = True
            else:
                print(oOutRange)

        expense_dict["categoria"] = __idCat

        flg_menu_gasto_categoria = False
        flg_menu_gasto = True

    while flg_menu_gasto_division:
        print(expense_dict)
        if expense_dict["division"] == 0:
            print("La división elegida es equitativa. \nSe calculará automáticamente, total/número de participantes.")
            if input("\nDesea cambiar la modalidad a personalizada, Si/no?").lower() == "si":
                expense_dict["division"] = 1
                print("La distribución del gasto ha cambiado a Personalizada.")
                input("Enter, para asignar cuotas de manera personalizada.")
                print()
                if expense_dict["total"] == 0 or len(expense_dict["participantes"]) == 0:
                    print("Debe tener previamente añadido el Total y Numero de participantes")
                else:
                    __distribucionOK = False
                    print("Total del gasto a cubrir: {}".format(expense_dict["total"]))
                    cuotas_pendientes.clear()
                    # __cuotaParticipacion = 0
                    # if expense_dict.get("division", "") == 0 and expense_dict["total"] > 0:
                    #     __cuotaParticipacion = int(expense_dict["total"]) / len(expense_dict["participantes"])
                    while not __distribucionOK:
                        __total_gasto = float(expense_dict["total"])
                        __resto_participantes = expense_dict["participantes"].copy()

                        # Listar los participantes ya añadidos
                        # y eliminarlos de la lista de los que faltan asignar.
                        if len(cuotas_pendientes) > 0:
                            print("Participantes añadidos:")
                            for clave in cuotas_pendientes:
                                __total_gasto = __total_gasto - float(cuotas_pendientes[clave])
                                __resto_participantes.remove(clave)
                                print("{} con NIF {:12} ->{:5.2f} euros".format(usuarios[clave]["nombre"],clave,cuotas_pendientes[clave]))
                                print("nombre",usuarios[clave]["nombre"])


                        if len(__resto_participantes) == 1:
                            __dni = __resto_participantes[0]
                            print("{} con NIF {}, es el último participante.".format(usuarios[__dni]["nombre"],__dni))
                            print("La cuota correspondiente es: {}".format(str(__total_gasto)))
                            print()
                            if input("Desea añadir esta cuota? Si/no").lower() == "si":
                                cuotas_pendientes[__dni] = float(__total_gasto)
                                __distribucionOK = True
                        elif len(__resto_participantes) == 0:
                            __distribucionOK = True
                        else:

                            print("Pendientes de añadir:")
                            for i in range(len(__resto_participantes)):
                                __dni = __resto_participantes[i]
                                print("{}) {} con NIF {}".format((i + 1), usuarios[__dni]["nombre"], __dni))

                            __posicion = input("Selecciona participante: ")

                            if not __posicion.isdigit():
                                print(oOnlyNumbers)
                            elif int(__posicion) not in range(1,len(__resto_participantes)+1):
                                print(type(__posicion))
                                print(len(__resto_participantes)+1)
                                print(oOutRange)
                            else:
                                __dni = __resto_participantes[int(__posicion)-1]
                                print("Pendiente de asignar: {} euros".format(str(__total_gasto)))
                                __tot_participa = input("Cual es la cuota de {} con NIF {}".format(usuarios[__dni]["nombre"],__dni))

                                if not __tot_participa.isdigit():
                                    print(oOnlyNumbers)
                                else:
                                    if not __total_gasto <= float(__tot_participa):
                                        if expense_dict["pagador"] == __dni:
                                            cuotas_pendientes[__dni] = float(__tot_participa)
                                    elif __total_gasto < float(__tot_participa):
                                        print("La cantidad de la cuota no puede ser superior al total.")
                                    else:
                                        print("La cantidad de la cuota no puede igual al total, si todavía quedan cuotas a asignar.")


                        input(oEnterToContinue)

                    if expense_dict["pagador"] in expense_dict["participantes"]:
                        del(cuotas_pendientes[expense_dict["pagador"]])
            else:
                if int(expense_dict["total"]) > 0 and len(expense_dict["participantes"]) > 0:

                    __total_gasto = float(expense_dict["total"])
                    __resto_participantes = expense_dict["participantes"].copy()
                    __tot_participa = float(__total_gasto)/len(__resto_participantes)

                    for i in range(len(__resto_participantes)):
                        __dni = __resto_participantes[i]
                        print("{}) La cuota de {} con NIF {} es {}.".format((i + 1), usuarios[__dni]["nombre"], __dni,__tot_participa))
                        if expense_dict["pagador"] != __dni:
                            cuotas_pendientes[__dni] = float(__tot_participa)


        input(oEnterToContinue)

        flg_menu_gasto_division = False
        flg_menu_gasto = True

    while flg_menu_gasto_participantes:

        #########################  Definir pagador #######################################

        if expense_dict.get("pagador","") =="" :
            print("Para añadir participantes, antes se ha determinar el pagador del gasto:")
            if input("Deseas añadir el pagador? SI/no: ").lower() == "si":
                flg_menu_gasto_participantes = False
                flg_menu_gasto_pagador = True
            else:
                flg_menu_gasto_participantes = False
                flg_menu_gasto = True

        else:
            __participaOK = False
            __participantes = []  #guardar participantes

            while not __participaOK:

                #Muestro si ya tengo participantes añadidos
                if len(__participantes) > 0:
                    print("Participantes añadidos:")
                    for clave in __participantes:
                        print("{}".format( clave))

                print("Añadir participantes del gasto pagado por {}\n".format(usuarios[expense_dict["pagador"]]['nombre']))

                lst_participantes = []
                for clave in usuarios:
                    if clave not in __participantes:
                        print("{}) {}".format((len(lst_participantes)+1),clave))
                        lst_participantes.append(clave)

                if len(lst_participantes) == 0:
                    __participaOK = True
                    break

                id_lst = input("Seleccione: ")

                if not id_lst.isdigit() or not int(id_lst) in range(1,(len(lst_participantes)+1)):
                    input(oOptionIncorrect +"\n"+ oEnterToContinue)
                    __participaOK= False
                else:
                    __participantes.append(lst_participantes[int(id_lst)-1])
                    if input("Añadir mas participantes a la lista? SI/no: ").lower() != "si":
                        __participaOK = True
                        input(oEnterToContinue)

            expense_dict["participantes"] = __participantes.copy()

            if expense_dict["pagador"] in __participantes:
                __participantes.remove(expense_dict["pagador"])

            expense_dict["lista_pendientes"] = __participantes

            flg_menu_gasto_participantes = False
            flg_menu_gasto = True

    while flg_menu_gasto_guardar:

        if (expense_dict["total"] == 0 or len(expense_dict["participantes"]) == 0
                or expense_dict["descripcion"]=="" or expense_dict["pagador"] ==""
                or len(cuotas_pendientes) == 0 ):
            print("Tienes pendiente ingresar información obligatoria.")
        else:

            print("Estas intentando guardar la siguiente información: ")
            #expense_dict


            print("Concepto {}".format(expense_dict.get("descripcion","")))
            print("Total {} euros".format(expense_dict.get("total","")))
            print("Pagador {} con NIF {}".format(usuarios[expense_dict["pagador"]]["nombre"],expense_dict.get("pagador","")))
            print("Participantes {}".format(expense_dict.get("participantes","")))
            lst_participa = ""
            for i in range(len(expense_dict["participantes"])):
                __dni = expense_dict["participantes"][i]
                if i ==0:
                    lst_participa = lst_participa + "{} con NIF {}".format( usuarios[__dni]["nombre"].title(), __dni)
                else:
                    lst_participa = lst_participa + ", {} con NIF {}".format( usuarios[__dni]["nombre"].title(), __dni)

            print("Participantes del gasto {}.".format(lst_participa))

            for dni in cuotas_pendientes:
                print("{} con NIF {} es {}.".format( usuarios[dni]["nombre"].title(), dni,
                                                                    cuotas_pendientes[dni]))

            if len(expense_dict["categoria"])>0:
                print("Categoria {}".format(expense_dict.get("categoria","")))


            if input("Deseas guardar la información, como asociada a este gasto:? SI/no: ").lower() == "si":
                __idGasto =len(gastos)+1
                gastos[len(gastos)+1]=expense_dict
                registro[__idGasto] = {"id_gasto":__idGasto, "acreedor":expense_dict["pagador"], "deudores": cuotas_pendientes }
                print("Gasto guardado correctamente.")
            else:
                print("El gasto no se ha guardado.")

        print(gastos)
        print(registro)

        flg_menu_gasto_guardar = False
        flg_menu_gasto = True

    while flg_menu_ver_gastos:

        get_cabecera(menu_ver_gastos_title,100,"*")
        opc = get_menu(menu_ver_gastos)

        # 2.1) VER TODOS LOS GASTOS
        if opc == 1:
            tabla_ver_gastos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}{:>20}{:>25}".format("ID", "Concepto","Total", "Pagador","Division", "Categoria","Estado","Participantes","Lista Pendientes")

            get_cabecera(tabla_ver_gastos, 150, "*")
            for ids in user_logged["gastos"]:
                gasto = user_logged["gastos"][ids]

                # logica para mostrar los gastos en los que el usuario logeado partiicpa en el gasto
                mostrar_este_gasto = False
                if gasto["pagador"] == user_logged_id:
                    mostrar_este_gasto = True
                else:
                    if user_logged_id in gasto["participantes"]:
                        mostrar_este_gasto = True
                    if user_logged_id in gasto["lista_pendientes"]:
                        mostrar_este_gasto = True

                # mostramos el gasto
                if mostrar_este_gasto:
                    division_id = gasto["division"]
                    nombre_division = tipo_division[division_id]
                    cat_id = gasto["categoria"][0]
                    nombre_categoria = categorias[cat_id]
                    estado_id = gasto["estado"]
                    nombre_estado = estado[estado_id]
                    datos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}".format(str(ids), gasto["descripcion"],gasto["total"], gasto["pagador"],nombre_division, nombre_categoria,nombre_estado)
                    if len(gasto["participantes"]) > len(gasto["lista_pendientes"]):
                        longitud = len(gasto["participantes"])
                    else:
                        longitud = len(gasto["lista_pendientes"])
                    for i in range(longitud):
                        if i == 0:
                            if len(gasto["participantes"]) > i:
                                datos = datos + "{:>20}".format(gasto["participantes"][i])
                            if len(gasto["lista_pendientes"]) > i:
                                datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                        else:
                            if len(gasto["participantes"]) > i:
                                datos = datos + "\n{:>125}".format(gasto["participantes"][i])
                                if len(gasto["lista_pendientes"]) > i:
                                    datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                            else:
                                if len(gasto["lista_pendientes"]) > i:
                                    datos = datos + "\n{:>150}".format(gasto["lista_pendientes"][i])
                    datos = datos + "\n" + "-" * 150
                    print(datos)
            input(oEnterToContinue)

        # 2.2) VER GASTOS (ordenados por cantidad=
        elif opc == 2:
            lista_ids = list(user_logged["gastos"].keys())
            for pasada in range(len(lista_ids) - 1):
                for i in range(len(lista_ids) - 1 - pasada):
                    id1 = lista_ids[i]
                    id2 = lista_ids[i + 1]
                    if user_logged["gastos"][id1]["total"] > user_logged["gastos"][id2]["total"]:
                        aux = lista_ids[i]
                        lista_ids[i] = lista_ids[i + 1]
                        lista_ids[i + 1] = aux
            tabla_ver_gastos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}{:>20}{:>25}".format("ID", "Concepto","Total","Pagador", "Division","Categoria", "Estado","Participantes","Lista Pendientes")

            get_cabecera(tabla_ver_gastos,  150, "*")
            for ids in lista_ids:
                gasto = user_logged["gastos"][ids]
                # logica para mostrar los gastos en los que el usuario logeado partiicpa en el gasto
                mostrar_este_gasto = False
                if gasto["pagador"] == user_logged_id:
                    mostrar_este_gasto = True
                else:
                    if user_logged_id in gasto["participantes"]:
                        mostrar_este_gasto = True
                    if user_logged_id in gasto["lista_pendientes"]:
                        mostrar_este_gasto = True

                # mostramos el gasto
                if mostrar_este_gasto:
                    division_id = gasto["division"]
                    nombre_division = tipo_division[division_id]
                    cat_id = gasto["categoria"][0]
                    nombre_categoria = categorias[cat_id]
                    estado_id = gasto["estado"]
                    nombre_estado = estado[estado_id]
                    datos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}".format(str(ids), gasto["descripcion"],gasto["total"],gasto["pagador"], nombre_division,nombre_categoria, nombre_estado)
                    if len(gasto["participantes"]) > len(gasto["lista_pendientes"]):
                        longitud = len(gasto["participantes"])
                    else:
                        longitud = len(gasto["lista_pendientes"])
                    for i in range(longitud):
                        if i == 0:
                            if len(gasto["participantes"]) > i:
                                datos = datos + "{:>20}".format(gasto["participantes"][i])
                            if len(gasto["lista_pendientes"]) > i:
                                datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                        else:
                            if len(gasto["participantes"]) > i:
                                datos = datos + "\n{:>125}".format(gasto["participantes"][i])
                                if len(gasto["lista_pendientes"]) > i:
                                    datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                            else:
                                if len(gasto["lista_pendientes"]) > i:
                                    datos = datos + "\n{:>150}".format(gasto["lista_pendientes"][i])
                    datos = datos + "\n" + "-" * 150
                    print(datos)
            input(oEnterToContinue)

        # 2.3) VER GASTOS PENDIENTES
        elif opc == 3:
            tabla_ver_gastos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}{:>20}{:>25}".format("ID", "Concepto","Total", "Pagador","Division", "Categoria","Estado","Participantes","Lista Pendientes")

            get_cabecera(tabla_ver_gastos,  150, "*")
            hay_pendientes = False
            for ids in user_logged["gastos"]:
                gasto = user_logged["gastos"][ids]

                # logica para mostrar los gastos en los que el usuario logeado partiicpa en el gasto
                mostrar_este_gasto = False
                if gasto["pagador"] == user_logged_id:
                    mostrar_este_gasto = True
                else:
                    if user_logged_id in gasto["participantes"]:
                        mostrar_este_gasto = True
                    if user_logged_id in gasto["lista_pendientes"]:
                        mostrar_este_gasto = True


                # mostramos el gasto
                if mostrar_este_gasto:
                    if gasto["estado"] == 0:
                        hay_pendientes = True
                        division_id = gasto["division"]
                        nombre_division = tipo_division[division_id]
                        cat_id = gasto["categoria"][0]
                        nombre_categoria = categorias[cat_id]
                        estado_id = gasto["estado"]
                        nombre_estado = estado[estado_id]
                        datos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}".format(str(ids), gasto["descripcion"],gasto["total"], gasto["pagador"],nombre_division, nombre_categoria,nombre_estado)
                        if len(gasto["participantes"]) > len(gasto["lista_pendientes"]):
                            longitud = len(gasto["participantes"])
                        else:
                            longitud = len(gasto["lista_pendientes"])
                        for i in range(longitud):
                            if i == 0:
                                if len(gasto["participantes"]) > i:
                                    datos = datos + "{:>20}".format(gasto["participantes"][i])
                                if len(gasto["lista_pendientes"]) > i:
                                    datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                            else:
                                if len(gasto["participantes"]) > i:
                                    datos = datos + "\n{:>125}".format(gasto["participantes"][i])
                                    if len(gasto["lista_pendientes"]) > i:
                                        datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                                else:
                                    if len(gasto["lista_pendientes"]) > i:
                                        datos = datos + "\n{:>150}".format(gasto["lista_pendientes"][i])
                        datos = datos + "\n" + "-" * 150
                        print(datos)
            if not hay_pendientes:
                print("No hay gastos pendientes.".center(150))
            input(oEnterToContinue)

        # 2.4) VER GASTOS COMPLETADOS
        elif opc == 4:
            tabla_ver_gastos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}{:>20}{:>25}".format("ID", "Concepto","Total", "Pagador","Division", "Categoria","Estado","Participantes","Lista Pendientes")
            get_cabecera(tabla_ver_gastos, 150, "*")
            hay_completados = False
            for ids in user_logged["gastos"]:
                gasto = user_logged["gastos"][ids]

                # logica para mostrar los gastos en los que el usuario logeado partiicpa en el gasto
                mostrar_este_gasto = False
                if gasto["pagador"] == user_logged_id:
                    mostrar_este_gasto = True
                else:
                    if user_logged_id in gasto["participantes"]:
                        mostrar_este_gasto = True
                    if user_logged_id in gasto["lista_pendientes"]:
                        mostrar_este_gasto = True

                # mostramos el gasto
                if mostrar_este_gasto:
                    if gasto["estado"] == 1:
                        hay_completados = True
                        division_id = gasto["division"]
                        nombre_division = tipo_division[division_id]
                        cat_id = gasto["categoria"][0]
                        nombre_categoria = categorias[cat_id]
                        estado_id = gasto["estado"]
                        nombre_estado = estado[estado_id]
                        datos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}".format(str(ids), gasto["descripcion"],gasto["total"], gasto["pagador"],nombre_division, nombre_categoria,nombre_estado)

                        if len(gasto["participantes"]) > len(gasto["lista_pendientes"]):
                            longitud = len(gasto["participantes"])
                        else:
                            longitud = len(gasto["lista_pendientes"])
                        for i in range(longitud):
                            if i == 0:
                                if len(gasto["participantes"]) > i:
                                    datos = datos + "{:>20}".format(gasto["participantes"][i])
                                if len(gasto["lista_pendientes"]) > i:
                                    datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                            else:
                                if len(gasto["participantes"]) > i:
                                    datos = datos + "\n{:>125}".format(gasto["participantes"][i])
                                    if len(gasto["lista_pendientes"]) > i:
                                        datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                                else:
                                    if len(gasto["lista_pendientes"]) > i:
                                        datos = datos + "\n{:>150}".format(gasto["lista_pendientes"][i])
                        datos = datos + "\n" + "-" * 150
                        print(datos)

            if not hay_completados:
                print("No hay gastos completados.".center(150))
            input(oEnterToContinue)

        # 2.5) VER GASTOS POR CATEGORÍA
        elif opc == 5:
            # se muestra lista de categorias

            get_cabecera("SELECCIONAR CATEGORÍA", 100, "*")
            for cat_id in categorias:
                print(str(cat_id) + ") " + categorias[cat_id])
            print()
            cat_input = input("Elige una categoria -> ")
            if not cat_input.isdigit():
                print(oOnlyNumbers)
                input(oEnterToContinue)
            else:
                cat_input = int(cat_input)
                if cat_input < 1 or cat_input > len(categorias):
                    print(oOutRange)
                    input(oEnterToContinue)
                else:
                    tabla_ver_gastos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}{:>20}{:>25}".format("ID","Concepto","Total","Pagador","Division","Categoria","Estado","Participantes","Lista Pendientes")
                    get_cabecera("SELECCIONAR CATEGORÍA", 150, "*")
                    hay_gastos_categoria = False
                    for ids in user_logged["gastos"]:
                        gasto = user_logged["gastos"][ids]

                        # logica para mostrar los gastos en los que el usuario logeado partiicpa en el gasto
                        mostrar_este_gasto = False
                        if gasto["pagador"] == user_logged_id:
                            mostrar_este_gasto = True
                        else:
                            if user_logged_id in gasto["participantes"]:
                                mostrar_este_gasto = True
                            if user_logged_id in gasto["lista_pendientes"]:
                                mostrar_este_gasto = True


                        # mostramos el gasto
                        if mostrar_este_gasto:
                            cat_id = gasto["categoria"][0]
                            if cat_id == cat_input:
                                hay_gastos_categoria = True
                                division_id = gasto["division"]
                                nombre_division = tipo_division[division_id]
                                nombre_categoria = categorias[cat_id]
                                estado_id = gasto["estado"]
                                nombre_estado = estado[estado_id]
                                datos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}".format(str(ids),gasto["descripcion"],gasto["total"],gasto["pagador"],nombre_division,nombre_categoria,nombre_estado)
                                if len(gasto["participantes"]) > len(gasto["lista_pendientes"]):
                                    longitud = len(gasto["participantes"])
                                else:
                                    longitud = len(gasto["lista_pendientes"])
                                for i in range(longitud):
                                    if i == 0:
                                        if len(gasto["participantes"]) > i:
                                            datos = datos + "{:>20}".format(gasto["participantes"][i])
                                        if len(gasto["lista_pendientes"]) > i:
                                            datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                                    else:
                                        if len(gasto["participantes"]) > i:
                                            datos = datos + "\n{:>125}".format(gasto["participantes"][i])
                                            if len(gasto["lista_pendientes"]) > i:
                                                datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                                        else:
                                            if len(gasto["lista_pendientes"]) > i:
                                                datos = datos + "\n{:>150}".format(gasto["lista_pendientes"][i])
                                datos = datos + "\n" + "-" * 150
                                print(datos)
                    if not hay_gastos_categoria:
                        texto = "No hay gastos en la categoría: " + categorias[cat_input]
                        print(texto.center(150))
                    input(oEnterToContinue)

        # 2.6) BUSCAR GASTO POR ID
        elif opc == 6:
            get_cabecera("BUSCAR GASTO POR ID", 100, "*")
            id_input = input("Introduce ID de gasto: ")
            if not id_input.isdigit():
                print(oOnlyNumbers)
                input(oEnterToContinue)
            else:
                id_input = int(id_input)
                if id_input in user_logged["gastos"]:
                    gasto = user_logged["gastos"][id_input]

                    # logica para mostrar los gastos en los que el usuario logeado partiicpa en el gasto
                    mostrar_este_gasto = False
                    if gasto["pagador"] == user_logged_id:
                        mostrar_este_gasto = True
                    else:
                        if user_logged_id in gasto["participantes"]:
                            mostrar_este_gasto = True
                        if user_logged_id in gasto["lista_pendientes"]:
                            mostrar_este_gasto = True


                    # mostramos el gasto
                    if mostrar_este_gasto:
                        tabla_ver_gastos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}{:>20}{:>25}".format("ID","Concepto","Total","Pagador","Division","Categoria","Estado","Participantes","Lista Pendientes")

                        get_cabecera(tabla_ver_gastos, 150, "*")

                        division_id = gasto["division"]
                        nombre_division = tipo_division[division_id]
                        cat_id = gasto["categoria"][0]
                        nombre_categoria = categorias[cat_id]
                        estado_id = gasto["estado"]
                        nombre_estado = estado[estado_id]
                        datos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}".format(str(id_input),gasto["descripcion"],gasto["total"], gasto["pagador"],nombre_division, nombre_categoria,nombre_estado)
                        if len(gasto["participantes"]) > len(gasto["lista_pendientes"]):
                            longitud = len(gasto["participantes"])
                        else:
                            longitud = len(gasto["lista_pendientes"])
                        for i in range(longitud):
                            if i == 0:
                                if len(gasto["participantes"]) > i:
                                    datos = datos + "{:>20}".format(gasto["participantes"][i])
                                if len(gasto["lista_pendientes"]) > i:
                                    datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                            else:
                                if len(gasto["participantes"]) > i:
                                    datos = datos + "\n{:>125}".format(gasto["participantes"][i])
                                    if len(gasto["lista_pendientes"]) > i:
                                        datos = datos + "{:>25}".format(gasto["lista_pendientes"][i])
                                else:
                                    if len(gasto["lista_pendientes"]) > i:
                                        datos = datos + "\n{:>150}".format(gasto["lista_pendientes"][i])
                        datos = datos + "\n" + "-" * 150
                        print(datos)
                        input(oEnterToContinue)
                    else:
                        print("No tienes permiso para ver este gasto.".center(100))
                        input(oEnterToContinue)
                else:
                    print("No existe ningún gasto con esa ID.".center(100))
                    input(oEnterToContinue)

        # 2.7) VOLVER AL MENU PRINCIPAL
        elif opc == 7:
            flg_menu_ver_gastos = False
            flg_menu_principal = True

# AQUI VA EL PUNTO 3

    while flg_menu_saldos:
        get_cabecera(menu_saldos_title,100,"*")
        opcion = get_menu(menu_saldos)

        # 3.1 Ver cuánto debo
        if opcion == 1:
            flg_menu_saldos = False
            flg_menu_saldos_deber = True

        # 3.2 Ver cuánto me deben
        elif opcion == 2:
            flg_menu_saldos = False
            flg_menu_saldos_haber = True

        # 3.3 Marcar gastos como pagados
        elif opcion == 3:
            flg_menu_saldos = False
            flg_menu_saldos_marcar_pagados_gastos = True

        # 3.4 Volver
        elif opcion == 4:
            flg_menu_saldos = False
            flg_menu_principal = True

    while flg_menu_saldos_deber:
        get_cabecera("VER CUÁNTO DEBO",100,"*")

        # obtener lista de usuarios que deben algo
        lst_deudores = []
        for gasto in registro.values():
            for nif_deudor in gasto["deudores"].keys():
                if nif_deudor not in lst_deudores:
                    lst_deudores.append(nif_deudor)

        if len(lst_deudores) == 0:
            print("No hay deudas registradas en el sistema.".center(100))
            input(oEnterToContinue)
            flg_menu_saldos_deber = False
            flg_menu_saldos = True
        else:
            print("Seleccione usuario para consultar sus deudas:")
            for i in range(len(lst_deudores)):
                __dni = lst_deudores[i]
                print("{}) {} con NIF {}".format((i + 1), usuarios[__dni]["nombre"].title(), __dni))

            __usrSelec = input(oOption)

            if not __usrSelec.isdigit():
                print(oOnlyNumbers)
                input(oEnterToContinue)
            elif not int(__usrSelec) in range(1, len(lst_deudores) + 1):
                print(oOutRange)
                input(oEnterToContinue)
            else:
                __usrSelec = int(__usrSelec)
                __dniUsrSelect = lst_deudores[__usrSelec - 1]

                print(espacio)
                print("DEUDAS DE: " + usuarios[__dniUsrSelect]["nombre"].upper())
                cabecera = "{:5} {:30} {:20} {:>10}".format("ID", "Concepto", "Acreedor", "Importe")
                print(linea_asteriscos + "\n" + cabecera + "\n" + linea_asteriscos)
                #get_cabecera(cabecera, 100, "*")

                __totalDeuda = 0
                for _clave_gasto in registro:
                    _registro = registro[_clave_gasto]
                    id_gasto = _registro["id_gasto"]
                    dni_acreedor = _registro["acreedor"]
                    nombre_acreedor = usuarios[dni_acreedor]["nombre"]

                    if __dniUsrSelect in _registro["deudores"]:
                        valor = _registro["deudores"][__dniUsrSelect]
                        descripcion = gastos[id_gasto]["descripcion"]

                        print("{:5} {:30} {:20} {:10.2f} €".format(str(id_gasto), descripcion, nombre_acreedor,
                                                                   valor))
                        __totalDeuda = float(__totalDeuda) + float(valor)

                print(linea_guiones)
                print("{:>57} {:10.2f} €".format("TOTAL A DEBER:", __totalDeuda))
                input(oEnterToContinue)

                flg_menu_saldos_deber = False
                flg_menu_saldos = True

    while flg_menu_saldos_haber:

        get_cabecera("VER CUÁNTO ME DEBEN (HABER)",100,"*")

        lista_acreedores = []
        for gasto in registro.values():
            acreedor = gasto["acreedor"]
            if acreedor not in lista_acreedores:
                lista_acreedores.append(acreedor)

        if len(lista_acreedores) == 0:
            print("No hay acreedores registrados.".center(100))
            input(oEnterToContinue)
            flg_menu_saldos_haber = False
            flg_menu_saldos = True
        else:
            print("Seleccione usuario para ver quién le debe dinero:")
            for i in range(len(lista_acreedores)):
                __dni = lista_acreedores[i]
                print("{}) {} con NIF {}".format((i + 1), usuarios[__dni]["nombre"].title(), __dni))

            __usrSelec = input(oOption)

            if not __usrSelec.isdigit():
                print(oOnlyNumbers)
                input(oEnterToContinue)
            elif not int(__usrSelec) in range(1, len(lista_acreedores) + 1):
                print(oOutRange)
                input(oEnterToContinue)
            else:
                __usrSelec = int(__usrSelec)
                __dniUsrSelect = lista_acreedores[__usrSelec - 1]

                print(espacio)
                print("SALDO A FAVOR DE: " + usuarios[__dniUsrSelect]["nombre"].upper())
                cabecera = "{:5} {:30} {:20} {:>10}".format("ID", "Concepto", "Deudor", "Importe")
                print(linea_asteriscos + "\n" + cabecera + "\n" + linea_asteriscos)

                __totalHaber = 0
                for _clave_gasto in registro:
                    _registro = registro[_clave_gasto]
                    id_gasto = _registro["id_gasto"]

                    if _registro["acreedor"] == __dniUsrSelect:
                        for dni_deudor in _registro["deudores"]:
                            valor = _registro["deudores"][dni_deudor]
                            nombre_deudor = usuarios[dni_deudor]["nombre"]
                            descripcion = gastos[id_gasto]["descripcion"]

                            print("{:5} {:30} {:20} {:10.2f} €".format(str(id_gasto), descripcion, nombre_deudor,
                                                                       valor))
                            __totalHaber = float(__totalHaber) + float(valor)

                print(linea_guiones)
                print("{:>57} {:10.2f} €".format("TOTAL A RECIBIR:", __totalHaber))
                input(oEnterToContinue)

                flg_menu_saldos_haber = False
                flg_menu_saldos = True

    while flg_menu_saldos_marcar_pagados_gastos:
        get_cabecera("MARCAR GASTO COMO PAGADO", 100, "*")

        print("Elegir usuario del que desea ingresar el pago:")
        lst_usuarios = []
        for k in usuarios:
            lst_usuarios.append(k)
        for i in range(len(lst_usuarios)):
            __dni = lst_usuarios[i]
            print("{}) {} con NIF {}".format((i + 1), usuarios[__dni]["nombre"].title(), __dni))

        __usrSelec = input(oOption)

        if not __usrSelec.isdigit():
            print(oOnlyNumbers)
            input(oEnterToContinue)
        elif not int(__usrSelec) in range(1, len(lst_usuarios) + 1):
            print(oOutRange)
            input(oEnterToContinue)
        else:
            __usrSelec = int(__usrSelec)
            __dniUsrSelect = lst_usuarios[__usrSelec - 1]

            __gasto_pagadoOK = False

            while not __gasto_pagadoOK:
                print(espacio)
                print(linea_guiones)
                print("DEUDAS DE {}".format(usuarios[__dniUsrSelect]["nombre"].upper()))
                print(linea_guiones)
                temp_lista_ids = []
                cabecera = "{:5} {:5} {:30} {:>10}".format("Op.", "ID", "Concepto", "Deuda")
                print(cabecera)

                contador_opciones = 1
                for _clave_gasto in registro:
                    _registro = registro[_clave_gasto]
                    if __dniUsrSelect in _registro["deudores"]:
                        id_gasto = _registro["id_gasto"]
                        valor = _registro["deudores"][__dniUsrSelect]
                        desc = gastos[id_gasto]["descripcion"]

                        print(
                            "{:5} {:5} {:30} {:10.2f} €".format(str(contador_opciones), str(id_gasto), desc, valor))
                        temp_lista_ids.append(id_gasto)
                        contador_opciones = contador_opciones + 1

                if len(temp_lista_ids) == 0:
                    print("\nEste usuario no tiene deudas pendientes.")
                    __gasto_pagadoOK = True
                    input(oEnterToContinue)
                else:
                    print("\n0) Cancelar y salir")
                    __idSelecGasto = input("seleccione numero de opc a liquidar: ")

                    if not __idSelecGasto.isdigit():
                        print(oOnlyNumbers)
                        input(oEnterToContinue)
                    else:
                        opcion_elegida = int(__idSelecGasto)
                        if opcion_elegida == 0:
                            __gasto_pagadoOK = True
                        elif opcion_elegida not in range(1, len(temp_lista_ids) + 1):
                            print(oOutRange)
                            input(oEnterToContinue)
                        else:
                            # recuperamos el ID real usando la lista temporal
                            __idGastoReal = temp_lista_ids[opcion_elegida - 1]

                            # logica de borrado
                            print("Liquidando deuda de {} en el gasto ID {}...".format(
                                usuarios[__dniUsrSelect]["nombre"], __idGastoReal))

                            # 1. borrar del registro de deudas
                            del registro[__idGastoReal]["deudores"][__dniUsrSelect]

                            # 2. borrar de la lista de pendientes en gastos
                            if __dniUsrSelect in gastos[__idGastoReal]["lista_pendientes"]:
                                gastos[__idGastoReal]["lista_pendientes"].remove(__dniUsrSelect)

                            # 3. comprobar si el gasto está totalmente pagado
                            if len(gastos[__idGastoReal]["lista_pendientes"]) == 0:
                                gastos[__idGastoReal]["estado"] = 1  # Pagado
                                print("--> ¡El gasto ha sido completado totalmente!")

                            # 4. Limpieza de registro si ya no hay deudores
                            if len(registro[__idGastoReal]["deudores"]) == 0:
                                del registro[__idGastoReal]

                            print("Pago registrado correctamente.")

                            seguir = input("¿Deseas marcar otro gasto de este usuario? (S/N): ")
                            if seguir.upper() != "S":
                                __gasto_pagadoOK = True

            flg_menu_saldos_marcar_pagados_gastos = False
            flg_menu_saldos = True


# --------------------------------------------------
    while flg_menu_gestionar_personas:

        get_cabecera(menu_personas_title, 100, "*")
        opc = get_menu(menu_personas)

        # 4.1) ver lista  personas
        if opc == 1:

            get_cabecera("LISTA DE PERSONAS", 100, "*")

            if len(usuarios) == 0:
                print("No hay personas registradas.".center(100))
            else:
                cabecera = "{:15}{:30}{:30}".format("DNI", "Nombre", "Username")
                print(cabecera)
                print(linea_guiones)
                for dni in usuarios:
                    persona = usuarios[dni]
                    nombre = persona["nombre"]
                    username = persona["username"]
                    fila = "{:15}{:30}{:30}".format(dni, nombre, username)
                    print(fila)

            input(oEnterToContinue)

        # 4.2) añade nueva persona
        elif opc == 2:
            get_cabecera("AÑADIR NUEVA PERSONA", 100, "*")

            correct_dni = False
            dni_nuevo = ""
            print("Introduzca el DNI de la nueva persona.")
            while not correct_dni:
                dni = input("Enter a DNI: ")
                dni = dni.upper()
                dni_sin_letra = dni[:8]
                if len(dni) != 9:
                    print("Incorrect length.")
                    input(oEnterToContinue)
                elif not dni_sin_letra.isdigit():
                    print("DNI must have all numbers (except the last character)")
                    input(oEnterToContinue)
                elif dni[-1].isdigit():
                    print("DNI must have all numbers (except the last character)")
                    input(oEnterToContinue)
                elif dni in usuarios:
                    print("DNI existente.")
                    input(oEnterToContinue)
                else:
                    dni_sin_letra = int(dni_sin_letra)
                    letra_necesaria = dni_sin_letra % 23
                    letra_correcta = letras_dni[letra_necesaria]
                    if dni[-1] == letra_correcta.upper():
                        correct_dni = True
                        dni_nuevo = dni
                    else:
                        print("Wrong letter. You put", dni[-1], "and the correct letter for this DNI is",
                              letra_correcta)
                        input(oEnterToContinue)
            print("DNI Válido.")
            nombre_nuevo = input("Nombre completo: ")
            if len(dni_nuevo) > 1:
                username_nuevo = dni_nuevo[:-1]
            else:
                username_nuevo = dni_nuevo
            usuarios[dni_nuevo] = {"nombre": nombre_nuevo,"username": username_nuevo,"password": "", "gastos": gastos}
            print("Persona añadida correctamente.".center(100))
            input(oEnterToContinue)

        # 4.3) eliminamos persona pero no tiene q tener gastos asociados
        elif opc == 3:
            get_cabecera("ELIMINAR PERSONA", 100, "*")

            if len(usuarios) == 0:
                print("No hay personas registradas.".center(100))
                input(oEnterToContinue)
            else:
                for dni in usuarios:
                    texto = dni +" - " +usuarios[dni]["nombre"]
                    print(texto)
                print()
                dni_borrar = input("Introduce el DNI de la persona a eliminar: ").upper()
                #print(dni_borrar)
                if dni_borrar == "":
                    print("El DNI no puede estar vacío.".center(100))
                    input(oEnterToContinue)
                else:
                    if dni_borrar not in usuarios:
                        print("No existe ninguna persona con ese DNI.".center(100))
                        input(oEnterToContinue)
                    else:
                        # comoprobacion de gastos del usuario a borrar
                        gastos_persona = usuarios[dni_borrar]["gastos"]
                        if len(gastos_persona) > 0:
                            print("No se puede eliminar: la persona tiene gastos asociados.".center(100))
                            input(oEnterToContinue)
                        else:
                            del usuarios[dni_borrar]
                            print("Persona eliminada correctamente.".center(100))
                            input(oEnterToContinue)

        # 4.4) Volver al menú principal
        elif opc == 4:
            flg_menu_gestionar_personas = False
            flg_menu_principal = True