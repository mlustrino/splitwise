from sw_functions.constantes import *

def get_menu(tupla):
    texto = ""
    for i in range(len(tupla)):
        texto += "{}) {}\n".format(str(i+1),tupla[i])

    while True:
        print(texto)
        opc = input("Option:\n")
        if not opc.isdigit():
            print(oOnlyNumbers)
        elif int(opc) not in range(1, len(tupla)+1):
            print(oOutRange)
        else:
            opc = int(opc)
            return opc


def get_cabecera(texto_principal="", width=100, tipus_separacion="*"):
    print(espacio)
    print(tipus_separacion.center(width, tipus_separacion) + "\n" + texto_principal.center(width) + "\n" + tipus_separacion.center(width, tipus_separacion) + "\n")

def bubblesort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                # METODO ALTERNATIVO QUE SOLO FUNCIONA EN PYTHON PARA CAMBIAR LOS NUMEROS SIN NECESIDAD DE AUX.
                # lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
