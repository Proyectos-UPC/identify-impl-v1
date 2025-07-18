from cliente import Cliente
from proceso.reniec import ProcesoReniec
from proceso.equifax import ProcesoEquifax
from proceso.liveness import ProcesoLiveness
from proceso.constants.reniec_db import RENIEC_DB
from proceso.constants.equifax_db import EQUIFAX_DB

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
                # Para Reniec y Equifax, pasar dato externo (nombre o base64)
                if p.get_validacion() == "informacion":
                    nombre = input("Ingrese nombre: ")
                    if p.get_tipo() in ["Reniec", "Liveness"]:
                        apellido = input("Ingrese apellido: ")
                        p.resolver(dni, f"{nombre} {apellido}")
                    else:
                        p.resolver(dni, nombre)

                elif p.get_validacion() in ["cara", "documento"]:
                    dato = input(f"Ingrese {p.get_validacion()} en base64: ")
                    p.resolver(dni, dato)

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
