class Pelicula:
    __codigo: str
    __genero: str
    __titulo: str
    __anio: int
    __productor: str
    __proyeccion: list
    
    def __init__(self, codigo, genero, titulo, anio, productor):
        self.__codigo = codigo
        self.__genero = genero
        self.__titulo = titulo
        self.__anio = anio
        self.__productor = productor
        self.__proyeccion = []
        
    def agregarProyeccion(self, laproyeccion):
        self.__proyeccion.append(laproyeccion)
    
    def __str__(self):
        return f"{self.__codigo} {self.__genero} {self.__titulo} {self.__anio} {self.__productor}"