from Docente import Docente
from Alumno import Alumno

class Ayudante (Docente, Alumno):
    __horasLIA= int
    def __init__(self, dni, nombre, apellido, codCargo, catedra, promedio, carrera, horasLia):
        super().__init__(dni, nombre, apellido, codCargo, catedra, promedio, carrera)
        self.__horasLIA = horasLia
        
    def gethoras(self):
        return self.__horasLIA
        
    def mostrar_datos(self):
        super().mostrar_datos() 
        print("Horas Lia: {}".format(self.gethoras()))  

        
    