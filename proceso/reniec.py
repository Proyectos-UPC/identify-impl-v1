from proceso.base import ProcesoBiometrico
from constants import PRECIOS

class ProcesoReniec(ProcesoBiometrico):
    def calcular_costo(self):
        return round(PRECIOS["Reniec"] * (self._reintentos / 4), 2)