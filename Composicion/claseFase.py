import datetime
class Fase:
    num = 122
    __fInicio: datetime
    __fFin: datetime

    def __init__(self, num, fInicio, fFin):
        self.num = num
        self.__fInicio = fInicio
        self.__fFin = fFin
    @classmethod
    def getnum(cls):
        return cls.num
    def getfInicio(self):
        return self.__fInicio
    def getFechaFin(self):
        return self.__fFin

    def __str__(self):
        return f"{self.getnum()} {self.getfInicio()} {self.getFechaFin()}"