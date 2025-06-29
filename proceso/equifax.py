from proceso.base import ProcesoBiometrico
from constants import PRECIOS

class ProcesoEquifax(ProcesoBiometrico):
    def calcular_costo(self):
        return round(PRECIOS["Equifax"] * (self._reintentos / 4), 2)