class Empleado:
    __nombre = str
    __dni = str
    __funcion = str
    __telefono = str
    __tareas = []
    def __init__(self, nombre, dni, funcion, telefono):
        self.__nombre = nombre
        self.__dni = dni
        self.__funcion = funcion
        self.__telefono = telefono
        
    def agregarTareas(self, tarea):
        self.__tareas.append(tarea)
    
    def __str__(self):
        return f"{self.__nombre} {self.__dni} {self.__funcion} {self.__telefono}"