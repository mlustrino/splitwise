from FUNCTIONS_SPLIT.sw_functions.constantes import *
from FUNCTIONS_SPLIT.sw_functions.funciones_genericas import *

def add_dni(usuarios,letras_dni) ->str:
    print("Enter your DNI to register.")

    while True:
        dni = input("Enter a DNI: ").strip().upper()

        if validate_dni(dni, usuarios,letras_dni):
            print("Valid DNI.")
            return dni

def validate_dni(dni, usuarios, letras_dni):

    if not isinstance(dni,str):
        print("DNI must be a string.")
        return False

    if len(dni) != 9:
        print("Incorrect length.")
        input(oEnterToContinue)
        return False

    dni = dni.upper()
    dni_sin_letra = dni[:8]

    if not dni_sin_letra.isdigit():
        print("DNI must have all numbers (except the last character)")
        input(oEnterToContinue)
        return False

    if dni[-1].isdigit():
        print("DNI must have all numbers (except the last character)")
        input(oEnterToContinue)
        return False

    if dni in usuarios:
        print("DNI already exists.")
        input(oEnterToContinue)
        return False

    dni_sin_letra = int(dni_sin_letra)
    letra_necesaria = dni_sin_letra % 23
    letra_correcta = letras_dni[letra_necesaria]
    if dni[-1] != letra_correcta.upper():
        print("Wrong letter. You put", dni[-1], "and the correct letter for this DNI is", letra_correcta)
        input(oEnterToContinue)
        return False
    else:
        return dni


def add_password() -> str:
    print("Enter your password.")
    while True:
        try:
            password = input("Enter a password: ").strip()
            validate_password(password)
            return password
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")



def validate_password(password: str)-> bool:
    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    if len(password) < 9:
        raise ValueError("Password must be longer than 8 characters")

    if " " in password:
        raise ValueError("Password must not contain spaces.")

    return True


def validate_exists_user(dni: str, usuarios:dict)-> bool:
    if not isinstance(dni, str):
        raise TypeError("Username must be a string.")

    if len(dni) < 9:
        raise ValueError("Username must be longer than 8 characters")

    if " " in dni:
        raise ValueError("Username must not contain spaces.")

    if dni not in usuarios:
        raise ValueError("User does not exist.")

    return True


def validate_exists_usr_pass(usuarios:dict, password:str, dni:str)->bool:
    validate_password(password)

    if usuarios[dni]["password"] != password:
        raise ValueError("Combination User and Password doesn't match.")

    return True

def login_retry() -> bool:
    retry = input("Do you want to try again? (y/n): ").strip().lower()
    return retry == "y"

def login_user(usuarios: dict, width=100) -> str|None:

    print("Enter your username and password.".center(width))
    while True:
        try:
            dni = input("Enter a DNI (username): ").strip()
            validate_exists_user(dni, usuarios)
            password = input("Enter a password: ").strip()
            validate_exists_usr_pass(usuarios, password, dni)

            return dni

        except ValueError as e:
            print(e)
            if not login_retry():
                return None
        except TypeError as e:
            print(e)
            if not login_retry():
                return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None


# VER GASTOS
def mostrar_fila_gasto(ids, gasto, tipo_division, categorias, estado):
    division_id = gasto["division"]
    nombre_division = tipo_division[division_id]
    cat_id = gasto["categoria"][0]
    nombre_categoria = categorias[cat_id]
    estado_id = gasto["estado"]
    nombre_estado = estado[estado_id]

    datos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}".format(str(ids), gasto["descripcion"], gasto["total"],
                                                             gasto["pagador"], nombre_division, nombre_categoria,
                                                             nombre_estado)

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

def es_gasto_visible(gasto, user_logged_id):
    if gasto["pagador"] == user_logged_id:
        return True
    if user_logged_id in gasto["participantes"]:
        return True
    if user_logged_id in gasto["lista_pendientes"]:
        return True
    return False


def imprimir_cabecera_gastos():
    tabla_ver_gastos = "{:10}{:30}{:>5}{:>15}{:>15}{:>15}{:>15}{:>20}{:>25}".format("ID", "Concepto", "Total",
                                                                                    "Pagador", "Division", "Categoria",
                                                                                    "Estado", "Participantes",
                                                                                    "Lista Pendientes")
    print(espacio)
    print(linea_asteriscos_150 + "\n" + tabla_ver_gastos + "\n" + linea_asteriscos_150)


def listar_todos_los_gastos(user_logged_gastos, user_logged_id, tipo_division, categorias, estado):
    imprimir_cabecera_gastos()
    for ids in user_logged_gastos:
        gasto = user_logged_gastos[ids]
        if es_gasto_visible(gasto, user_logged_id):
            mostrar_fila_gasto(ids, gasto, tipo_division, categorias, estado)
    input(oEnterToContinue)


def listar_gastos_ordenados(user_logged_gastos, user_logged_id, tipo_division, categorias, estado):
    lista_aux = []
    for id_gasto in user_logged_gastos:
        lista_aux.append([user_logged_gastos[id_gasto]["total"], id_gasto])
    lista_ordenada_datos = bubblesort(lista_aux)
    lista_ids = []
    for item in lista_ordenada_datos:
        lista_ids.append(item[1])
    imprimir_cabecera_gastos()
    for ids in lista_ids:
        gasto = user_logged_gastos[ids]
        if es_gasto_visible(gasto, user_logged_id):
            mostrar_fila_gasto(ids, gasto, tipo_division, categorias, estado)
    input(oEnterToContinue)


def listar_gastos_por_estado(user_logged_gastos, user_logged_id, estado_buscado, tipo_division, categorias,
                             estado_labels):
    imprimir_cabecera_gastos()
    encontrados = False
    for ids in user_logged_gastos:
        gasto = user_logged_gastos[ids]
        if es_gasto_visible(gasto, user_logged_id):
            if gasto["estado"] == estado_buscado:
                encontrados = True
                mostrar_fila_gasto(ids, gasto, tipo_division, categorias, estado_labels)

    if not encontrados:
        if estado_buscado == 0:
            print("No hay gastos pendientes.".center(150))
        else:
            print("No hay gastos completados.".center(150))
    input(oEnterToContinue)


def listar_gastos_por_categoria(user_logged_gastos, user_logged_id, categorias, tipo_division, estado_labels):
    print(espacio)
    print(linea_asteriscos + "\n" + "SELECCIONAR CATEGORÍA".center(100) + "\n" + linea_asteriscos)
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
            imprimir_cabecera_gastos()
            hay_gastos_categoria = False
            for ids in user_logged_gastos:
                gasto = user_logged_gastos[ids]
                if es_gasto_visible(gasto, user_logged_id):
                    cat_id = gasto["categoria"][0]
                    if cat_id == cat_input:
                        hay_gastos_categoria = True
                        mostrar_fila_gasto(ids, gasto, tipo_division, categorias, estado_labels)
            if not hay_gastos_categoria:
                texto = "No hay gastos en la categoría: " + categorias[cat_input]
                print(texto.center(150))
            input(oEnterToContinue)


def buscar_gasto_por_id(user_logged_gastos, user_logged_id, tipo_division, categorias, estado_labels):
    print(espacio)
    print(linea_asteriscos + "\n" + "BUSCAR GASTO POR ID".center(100) + "\n" + linea_asteriscos)
    id_input = input("Introduce ID de gasto: ")
    if not id_input.isdigit():
        print(oOnlyNumbers)
        input(oEnterToContinue)
    else:
        id_input = int(id_input)
        if id_input in user_logged_gastos:
            gasto = user_logged_gastos[id_input]
            if es_gasto_visible(gasto, user_logged_id):
                imprimir_cabecera_gastos()
                mostrar_fila_gasto(id_input, gasto, tipo_division, categorias, estado_labels)
                input(oEnterToContinue)
            else:
                print("No tienes permiso para ver este gasto.".center(100))
                input(oEnterToContinue)
        else:
            print("No existe ningún gasto con esa ID.".center(100))
            input(oEnterToContinue)