from datos.diccionarios import gastos
from sw_functions.constantes import *

def add_dni(usuarios,letras_dni) ->str:
    print("Enter your DNI to register.")

    while True:
        try:
            dni = input("Enter a DNI: ").strip()
            validate_dni(dni, usuarios,letras_dni)
            return dni
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")

def validate_dni(dni, usuarios, letras_dni) -> bool:

    if not isinstance(dni,str):
        raise TypeError("DNI must be a string.")

    if len(dni) != 9:
        raise ValueError("DNI must have 9 digits.")

    dni = dni.upper()
    dni_sin_letra = dni[:8]

    if not dni_sin_letra.isdigit():
        raise ValueError("DNI must have all numbers (except the last character)")

    if dni[-1].isdigit():
        raise ValueError("Last character mus be a letter.")

    if dni in usuarios:
        raise ValueError("DNI already exists.")

    dni_sin_letra = int(dni_sin_letra)
    letra_necesaria = dni_sin_letra % 23
    letra_correcta = letras_dni[letra_necesaria]
    if dni[-1] != letra_correcta.upper():
        raise ValueError(f"Wrong letter. Correct letter is {letra_correcta} instead of {dni[-1]}.")

    return True


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

def ask_retry() -> bool:
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
            if not ask_retry():
                return None
        except TypeError as e:
            print(e)
            if not ask_retry():
                return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

def add_name_user()->str:
    while True:
        try:
            name = input("Enter a name of user: ").strip()
            validate_name(name)
            return name
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")

def validate_name(name:str)->bool:
    '''
    El nombre puede contener espacios, pero no debe ser vacío.
    :param name:
    :return:
    '''
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    if "" == name:
        raise ValueError("Name cannot be empty.")
    return True


def create_user(usuarios: dict) -> dict|None:
    try:
        new_dni = add_dni(usuarios, letras_dni)
        new_name = add_name_user()
        new_pass = add_password()
        return {"nombre": new_name, "username": new_dni, "password": new_pass,"gastos": gastos}

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None



