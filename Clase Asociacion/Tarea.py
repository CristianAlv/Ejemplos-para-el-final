import datetime
class Tarea:
    __nombre: str
    __fInicio: datetime
    __fFin: datetime

    def __init__(self, nombre, fInicio, fFin):
        self.__nombre = nombre
        self.__fInicio = fInicio
        self.__fFin = fFin
    def getnombre(self):
        return self.__nombre
    def getfInicio(self):
        return self.__fInicio
    def getfFin(self):
        return self.__fFin
    def __str__(self):
        return f"{self.__nombre} {self.__fInicio} {self.__fFin}"