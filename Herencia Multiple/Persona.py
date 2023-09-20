import abc
from abc import ABC
class Persona(ABC):
    __dni: int
    __apellido: str
    __nombre: str
    def __init__(self, dni, nombre, apellido, codCargo, catedra, promedio, carrera):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
    
    def getnombre(self):
        return self.__nombre
    def getdni(self):
        return self.__dni
    def getapellido(self):
        return self.__apellido
    def mostrar_datos(self):
        print("Nombre: {}".format(self.getnombre())) 
        print("Apellido: {}".format(self.getapellido()))
        print("Dni:{}".format(self.getdni()))
        pass
    