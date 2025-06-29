from proceso.base import ProcesoBiometrico
from constants import PRECIOS

class ProcesoLiveness(ProcesoBiometrico):
    def calcular_costo(self):
        return round(PRECIOS["Liveness"] * (self._reintentos / 4), 2)