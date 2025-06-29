from cliente import Cliente
from proceso.reniec import ProcesoReniec
from proceso.equifax import ProcesoEquifax
from proceso.liveness import ProcesoLiveness
class SistemaBiometrico:
    def __init__(self):
        self.__procesos = []

    def solicitar_proceso(self):
        cliente_nombre = input("Cliente (Rimac, Prima): ")
        cliente = Cliente(cliente_nombre)
        tipo = input("Tipo (Reniec, Equifax, Liveness): ")
        reintentos = int(input("Número de reintentos (1-4): "))
        validaciones = input("Validaciones requeridas (documento, cara, informacion): ").split(',')

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
        print("ID no encontrado.")

    def listar_transacciones(self):
        total = 0
        print(f"Total a pagar: S/ {round(total, 2)}")

    def pagar_todo(self):
        print("Todas las transacciones han sido pagadas.")

    def pagar_individual(self):
        pid = input("Ingrese el ID del proceso a pagar: ")
        print("ID no encontrado.")

    def listar_procesos(self):
        for p in self.__procesos:
            print(p)
