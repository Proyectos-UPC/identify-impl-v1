from proceso.base import ProcesoBiometrico
from constants import PRECIOS
from proceso.constants.reniec_db import RENIEC_DB

class ProcesoReniec(ProcesoBiometrico):
    def calcular_costo(self):
        return round(PRECIOS["Reniec"] * (self._reintentos / 4), 2)
    
    def resolver(self, dni, valor_ingresado):
        datos = RENIEC_DB.get(dni)
        if not datos:
            print("DNI no encontrado en Reniec.")
            return

        if self.get_validacion() == "informacion":
            nombre, apellido = valor_ingresado.split()
            if nombre == datos["nombre"] and apellido == datos["apellido"]:
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