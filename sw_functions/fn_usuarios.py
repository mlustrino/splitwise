from sw_functions.constantes import *

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

