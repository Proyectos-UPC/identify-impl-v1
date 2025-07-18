from cliente import Cliente
from proceso.reniec import ProcesoReniec
from proceso.equifax import ProcesoEquifax
from proceso.liveness import ProcesoLiveness
from constants.reniec_db import RENIEC_DB
from constants.equifax_db import EQUIFAX_DB

class SistemaBiometrico:
    def __init__(self):
        self.__procesos = []

    def solicitar_proceso(self):
        cliente_nombre = input("Cliente (Rimac, Prima): ")
        cliente = Cliente(cliente_nombre)
        tipo = input("Tipo (Reniec, Equifax, Liveness): ")
        reintentos = int(input("Número de reintentos (1-4): "))
        validaciones = input("Validación requerida (documento, cara, informacion): ")

        if tipo == "Reniec":
            proceso = ProcesoReniec(cliente, tipo, reintentos, validaciones)
        elif tipo == "Equifax":
            proceso = ProcesoEquifax(cliente, tipo, reintentos, validaciones)
        else:
            proceso = ProcesoLiveness(cliente, tipo, reintentos, validaciones)

        self.__procesos.append(proceso)
        print(f"Proceso creado con ID: {proceso.get_id()}")

    def resolver_proceso(self):
        pid = input("Ingrese el ID del proceso: ")
        for p in self.__procesos:
            if p.get_id() == pid:
                dni = input("DNI: ")

                # Buscar tipo de proceso
                tipo = p.get_tipo()

                # Simulación de búsquedas externas
                datos_reniec = RENIEC_DB.get(dni) if tipo == "Reniec" else None
                datos_equifax = EQUIFAX_DB.get(dni) if tipo == "Equifax" else None

                if p.get_validacion() == "informacion":
                    if tipo == "Reniec" and datos_reniec:
                        p.resolver(dni, datos_reniec["nombre"])
                    elif tipo == "Equifax" and datos_equifax:
                        p.resolver(dni, datos_equifax["nombre"])
                    else:
                        print("Datos no encontrados en base externa.")
                        return

                elif p.get_validacion() == "cara":
                    cara = input("Ingrese rostro en base64: ")
                    p.resolver(dni, cara)

                elif p.get_validacion() == "documento":
                    docu = input("Ingrese foto del documento en base64: ")
                    p.resolver(dni, docu)

                print("Proceso resuelto.")
                return
        print("ID no encontrado.")


    def listar_transacciones(self):
        total = 0
        for p in self.__procesos:
            print(p)
            if not p.esta_pagado():
                total += p.calcular_costo()
        print(f"Total a pagar: S/ {round(total, 2)}")

    def pagar_todo(self):
        for p in self.__procesos:
            if not p.esta_pagado():
                p.marcar_pagado()
        print("Todas las transacciones han sido pagadas.")

    def pagar_individual(self):
        pid = input("Ingrese el ID del proceso a pagar: ")
        for p in self.__procesos:
            if p.get_id() == pid:
                if not p.esta_pagado():
                    p.marcar_pagado()
                    print("Proceso pagado.")
                else:
                    print("Ya está pagado.")
                return
        print("ID no encontrado.")

    def listar_procesos(self):
        for p in self.__procesos:
            print(p)
