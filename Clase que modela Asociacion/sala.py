class Sala:
    __numero: int
    __aforo: int
    __proyeccion: list
    def __init__(self, numero, aforo):
        self.__numero = numero
        self.__aforo = aforo
        self.__proyeccion = []
        
    def agregarProyeccion(self, Proyeccion):
        self.__proyeccion.append(Proyeccion)
        
    def __str__(self):
        return f"{self.__numero} {self.__aforo}"