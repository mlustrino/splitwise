
gastos = {
    1: {"descripcion": "Menú restaurante Popup", "total": 324, "pagador": "76767676H", "division": 0, "categoria": [1],
        "estado": 0, "participantes": ["47474747X", "24536425T", "11111111X"],"lista_pendientes": ["47474747X", "24536425T"]},
    2: {"descripcion": "Testeando", "total": 128, "pagador": "76767676H", "division": 0, "categoria": [1], "estado": 0,
        "participantes": ["47474747X", "24536425T", "11111111X"], "lista_pendientes": ["47474747X", "24536425T"]},
    3: {"descripcion": "Nuevo Gasto", "total": 423, "pagador": "76767676H", "division": 0, "categoria": [1],
        "estado": 1, "participantes": ["47474747X", "24536425T"], "lista_pendientes": []},
    4: {"descripcion": "Nuevo Gasto", "total": 62, "pagador": "76767676H", "division": 0, "categoria": [1], "estado": 0,
        "participantes": ["47474747X", "24536425T"], "lista_pendientes": ["47474747X", "24536425T", "11111111X"]}

    }

registro = {1:
                {"id_gasto":1,"acreedor": "76767676H","deudores":
                    {
                    "47474747X":108,
                    "24536425T":108
                    }
                 },
            2:
                {"id_gasto": 2, "acreedor": "76767676H", "deudores":
                    {
                    "47474747X":42.67,"24536425T":42.67
                    }
                 },
            4:
                {"id_gasto": 4, "acreedor": "76767676H", "deudores":
                    {
                    "47474747X":20.67,
                    "24536425T":20.67
                    }
                 }
            }

categorias = {1: "Comida", 2: "Transporte", 3: "Ocio", 4: "Otros"}
tipo_division = ["equitativa", "personalizado"]
estado = ["pendiente", "pagado"]

usuario1 = {"nombre": "Ivan", "username": "11111111", "password": "genialidad123", "gastos": gastos}
usuario2 = {"nombre":"Pedro", "username":"peter", "password":"genialidad123", "gastos": gastos}
usuario3 = {"nombre":"Luis", "username":"lucho", "password":"genialidad123", "gastos": gastos}
usuario4 = {"nombre":"Maite", "username":"lamate", "password":"genialidad123", "gastos": gastos}
usuario5 = {"nombre":"Marta", "username":"martuki", "password":"genialidad123", "gastos": gastos}
usuarios = {"11111111J":usuario1,"22222222X":usuario2,"47474747X":usuario3,"24536425T":usuario4,"76767676H":usuario5}
