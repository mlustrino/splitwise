from constantes import *
from datos.diccionarios import usuarios


def validate_description(description) -> bool:

    if not isinstance(description, str):
        raise TypeError("Description must be a string.")
    if 3 <= len(description):
        raise ValueError("Description must have longer than 3 characters.")
    return True

def set_expense_description() -> str:
    while True:
        try:
            description = input("Add expense description: ".center(100)).strip()
            validate_description(description)
            return description
        except (ValueError, TypeError) as e:
            print(e)
            input(oEnterToContinue.center(100))
        except Exception as e:
            print(f"Unexpected error: {e}")

def validate_expense(amount) -> bool:
    if not isinstance(amount, float):
        raise TypeError(oOnlyNumbers)
    if amount <= 0:
        raise ValueError(oOnlyPositive)
    return True


def set_expense_amount() -> float:
    while True:
        try:
            total_expense = input("Añadir total del gasto: ".center(70))
            validate_expense(total_expense)
            return float(total_expense)
        except (ValueError, TypeError) as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")


def validate_selected_user(id_select:str, lst_pagadores:list ) -> int:

    if not id_select.isdigit():
        raise ValueError(oOnlyNumbers)

    if int(id_select) not in range(1,len(lst_pagadores)+1):
        raise ValueError(oOutRange)

    return int(id_select) - 1


def get_user_from_list(usuarios: dict) -> str:

    lst_pagadores = list(usuarios.keys())

    while True:
        try:
            print("Who will pay the expense:\n")

            for i in range(len(lst_pagadores)):
                print("{}) {}".format(i + 1, lst_pagadores[i]))

            id_lst = input("Choose a number:")
            indice = validate_selected_user(id_lst, lst_pagadores)

            return lst_pagadores[indice]

        except (ValueError, TypeError) as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

def validate_lst_selection(id_select:str, lst_select:list ) -> int:

    if not id_select.isdigit():
        raise ValueError(oOnlyNumbers)

    if int(id_select) not in range(1,len(lst_select)+1):
        raise ValueError(oOutRange)

    return int(id_select) - 1

def get_element_from_list(lst_select: list, intro:str) -> str:

    while True:
        try:

            print(intro)

            for i in range(len(lst_select)):
                    print("{}) {}".format(i + 1, lst_select[i]))

            id_lst = input("Choose a number:")
            indice = validate_lst_selection(id_lst, lst_select)

            return lst_select[indice]

        except (ValueError, TypeError) as e:
            print(e)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None


