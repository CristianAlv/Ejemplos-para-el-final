class RegistroTrabajo:
    __cantidadDias: int
    __Tarea: object
    __Empleado: object
    def __init__(self, cantidadDias, Tarea, Empleado):
        self.__cantidadDias = cantidadDias
        self.__Tarea = Tarea
        self.__Empleado = Empleado
        
    def __str__(self):
        return f"{self.__cantidadDias} {self.__Empleado} {self.__Tarea}"