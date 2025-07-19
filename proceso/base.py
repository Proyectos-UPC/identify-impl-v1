from abc import ABC, abstractmethod
import uuid

class ProcesoBiometrico(ABC):
    def __init__(self, cliente, tipo, reintentos, validaciones):
        self._id = str(uuid.uuid4())
        self._cliente = cliente
        self._tipo = tipo
        self._reintentos = reintentos
        self._validaciones = validaciones
        self._resuelto = False
        self._pagado = False

    @abstractmethod
    def resolver(self, dni: str):
        pass

    def marcar_pagado(self):
        self._pagado = True

    def esta_pagado(self):
        return self._pagado

    def get_id(self):
        return self._id

    def get_cliente(self):
        return self._cliente

    def get_tipo(self):
        return self._tipo

    def get_resuelto(self):
        return self._resuelto

    def get_validacion(self):
        return self._validaciones

    @abstractmethod
    def calcular_costo(self):
        pass

    def __str__(self):
        estado = "Pagado" if self._pagado else "Pendiente"
        resuelto = "Sí" if self._resuelto else "No"
        return f"ID: {self._id} | Resuelto: {resuelto} | Cliente: {self._cliente} | Tipo: {self._tipo} | Reintentos: {self._reintentos} | Validación: {self._validaciones} | Costo: S/ {self.calcular_costo()} | Estado: {estado}"