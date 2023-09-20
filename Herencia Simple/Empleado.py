import abc
from abc import ABC
class Empleado(ABC):
    __nombre: str
    __apellido: str
    __sueldo: float
    
    def __init__(self, nombre, apellido, sueldo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__sueldo = sueldo
    
    def getnombre(self):
        return self.__nombre
    def getapellido(self):
        return self.__apellido
    def getsueldo(self):
        return self.__sueldo
        
    @abc.abstractmethod
    def getImporteSueldo(self):
        pass
    
    def __str__(self):
        return f"Nombre: {self.__nombre} Apellido: {self.__apellido} Importe Total de Sueldo a cobrar: {self.getImporteSueldo()}"