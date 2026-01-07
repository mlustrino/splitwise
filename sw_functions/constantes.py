
################### Constants ###################
oEnterToContinue = "\nEnter to continue"
oOption = "Opcion -> "
oOnlyNumbers = "Numeric Entries Only"
oOptionIncorrect = "Incorrect Option"
oOutRange = "Out of range"
oOnlyPositive = "Solo valores positivos"



# ---------- DISEÑOS PARA EL MENÚ ----------
linea_asteriscos = "*".center(100, "*")
linea_asteriscos_150 = "*".center(150, "*")
linea_iguales = "=".center(100, "=")
linea_guiones = "-".center(100, "-")
espacio = "\n" * 20


# ---------- LOGICA DNI ----------
letras_dni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
letras_dni = tuple(letras_dni)



# ---------- MENU LOGIN ----------
splitwise_title = "SPLITWISE".center(100)
#menu_login = "1) Iniciar sesión\n2) Crear usuario\n3) Salir\n"
menu_login = ("Iniciar sesión","Crear usuario","Salir")

# ---------- MENU INICIAR SESION ----------
iniciar_sesion_title = "LOGIN".center(100)
menu_iniciar_sesion = "Nombre de usuario (DNI):".center(100)

# ---------- MENU CREAR USUARIO ----------
crear_usuario_title = "CREAR USUARIO".center(100)

# ---------- MENU PRINCIPAL ----------
menu_principal_title = "MENU PRINCIPAL".center(100)
#menu_principal = "1) Nuevo Gasto\n2) Ver Gastos\n3) Saldos y deudas\n4) Gestionar personas (amigos / participantes)\n5) Salir\n"
menu_principal = ("Nuevo Gasto","Ver Gastos","Saldos y deudas","Gestionar personas (amigos / participantes)","Salir")

# ---------- MENU NUEVO GASTO ----------
menu_nuevo_gasto_title = "NUEVO GASTO".center(100)

menu00 = ("Init Data","Find Users","List Users","Exit")
#menu_nuevo_gasto = "1.1) Concepto del gasto\n1.2) Cantidad total\n1.3) Tipo de reparto (equitativo por defecto)\n1.4) Pagador\n1.5) Participantes\n1.6) Categoría del gasto\n1.7) Dividir el gasto\n1.8) Confirmar gasto\n1.9) Volver al menú principal\n"
menu_nuevo_gasto = ("Concepto del gasto","Cantidad total","Tipo de reparto (equitativo por defecto)","Pagador","Participantes","Categoría del gasto","Dividir el gasto","Confirmar gasto","Volver al menú principal")

# ---------- MENU VER GASTOS ----------
menu_ver_gastos_title = "VER GASTOS".center(100)
#menu_ver_gastos = "2.1) Ver todos los gastos\n2.2) Ordenar por cantidad\n2.3) Ver gastos pendientes\n2.4) Ver gastos completados\n2.5) Ver gastos por categoría\n2.6) Buscar gasto por ID\n2.7) Volver al menú principal\n"
menu_ver_gastos = ("Ver todos los gastos","Ordenar por cantidad","Ver gastos pendientes","Ver gastos completados","Ver gastos por categoría","Buscar gasto por ID","Volver al menú principal")

# ---------- MENU SALDOS Y DEUDAS ----------
menu_saldos_title = "SALDOS Y DEUDAS".center(100)
#menu_saldos = "3.1) Ver cuánto debo\n3.2) Ver cuánto me deben\n3.3) Marcar gastos como pagados\n3.4) Volver al menú principal\n"
menu_saldos = ("Ver cuánto debo","Ver cuánto me deben","Marcar gastos como pagados","Volver al menú principal")

# ---------- MENU GESTIONAR PERSONAS ----------
menu_personas_title = "GESTIONAR PERSONAS".center(100)
#menu_personas = "4.1) Ver lista de personas\n4.2) Añadir nueva persona\n4.3) Eliminar persona\n4.4) Volver al menú principal\n"
menu_personas = ("Ver lista de personas","Añadir nueva persona","Eliminar persona","Volver al menú principal")
