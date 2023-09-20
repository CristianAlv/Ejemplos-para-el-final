from claseFase import Fase
class Obra:
    __nombre: str
    __ubicacion : str
    __Fase = []
    def __init__(self, nombre, ubicacion):
        self.__nombre = nombre
        self.__ubicacion = ubicacion

    def getubicacion(self):
        return self.__ubicacion
    def getnombre(self):
        return self.__nombre
    def agregarobra(self, fechaI, fechaFin):
        num = Fase.getnum()
        FaseRandom = Fase(num, fechaI, fechaFin) 
        self.__Fase.append(FaseRandom)
    def getlista(self):
        for dato in self.__Fase:
            return dato
    def __str__(self):
        return f"{self.__nombre} {self.__ubicacion} {self.getlista()}"
    