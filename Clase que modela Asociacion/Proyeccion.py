from Pelicula import Pelicula
from sala import Sala
class Proyeccion:
    __fecha: str
    __hora: str
    __Sala: object
    __Pelicula: object
    def __init__(self, fecha, hora, Sala, Pelicula):
        self.__fecha = fecha
        self.__hora = hora
        self.__Sala = Sala
        self.__Pelicula = Pelicula
        self.__Sala.agregarProyeccion(self)
        self.__Pelicula.agregarProyeccion(self)
    
    def __str__(self):
        return f"{self.__fecha} {self.__hora} {self.__Sala} {self.__Pelicula}"