class SistemaBiometrico:
    def __init__(self):
        self.__procesos = []

    def solicitar_proceso(self):
        tipo = input("Tipo (Reniec, Equifax, Exist): ")
        reintentos = int(input("Número de reintentos (1-4): "))
        validaciones = input("Validaciones requeridas (documento, cara, informacion): ").split(',')
        print(f"Proceso creado con ID: id")

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
