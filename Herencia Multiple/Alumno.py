from Persona import Persona

class Alumno(Persona):
    __promedio: float
    __carrera: str
    def __init__(self, dni, nombre, apellido, codCargo, catedra, promedio, carrera):
        super().__init__(dni, nombre, apellido, codCargo, catedra, promedio, carrera)
        self.__promedio = promedio
        self.__carrera = carrera
        
    def getpromedio(self):
        return self.__promedio
    def getcarrera(self):
        return self.__carrera
    def mostrar_datos(self):
        super().mostrar_datos()
        print("Promedio: {}".format(self.getpromedio()))  
        print("Carrera: {}".format(self.getcarrera()))
        