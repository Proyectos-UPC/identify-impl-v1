from proceso.base import ProcesoBiometrico
from proceso.constants.equifax_db import EQUIFAX_DB
from constants import PRECIOS

class ProcesoEquifax(ProcesoBiometrico):
    def calcular_costo(self):
        return round(PRECIOS["Equifax"] * (self._reintentos / 4), 2)
    def resolver(self, dni, valor_ingresado):
        datos = EQUIFAX_DB.get(dni)
        if not datos:
            print("DNI no encontrado en Equifax.")
            return

        if self.get_validacion() == "informacion":
            if valor_ingresado == datos["nombre"]:
                self._resuelto = True
            else:
                print("Nombre incorrecto.")

        elif self.get_validacion() == "documento":
            if valor_ingresado == datos["base64_doc"]:
                self._resuelto = True
            else:
                print("Documento incorrecto.")

        elif self.get_validacion() == "cara":
            if valor_ingresado == datos["base64_cara"]:
                self._resuelto = True
            else:
                print("Cara no coincide.")