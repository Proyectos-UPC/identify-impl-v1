from proceso.base import ProcesoBiometrico
from constants import PRECIOS
import re

class ProcesoLiveness(ProcesoBiometrico):
    def calcular_costo(self):
        return round(PRECIOS["Liveness"] * (self._reintentos / 4), 2)
    
    def resolver(self, dni, nombre_apellido):
        try:
            nombre, apellido = nombre_apellido.strip().split()

            def es_valido(valor):
                return re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", valor) is not None

            if self.get_validacion() == "informacion":
                if es_valido(nombre) and es_valido(apellido):
                    self._resuelto = True
                else:
                    print("❌ Nombre o apellido contiene caracteres inválidos.")

            elif self.get_validacion() in ["documento", "cara"]:
                # Simulación sin base de datos
                if len(dni) == 8 and dni.isdigit():
                    self._resuelto = True
                else:
                    print("❌ DNI inválido para validación Liveness.")

        except ValueError:
            print("❌ Formato incorrecto: asegúrate de ingresar nombre y apellido separados por un espacio.")
        except Exception as e:
            print(f"⚠️ Error inesperado al resolver el proceso Liveness: {e}")