from Persona import Persona
class Docente(Persona):
    __codCargo: int
    __catedra: str
    def __init__(self, dni, nombre, apellido, codCargo, catedra, promedio=0, carrera=None):
        super().__init__(dni, nombre, apellido, codCargo, catedra, promedio, carrera)
        self.__codCargo = codCargo
        self.__catedra = catedra
        
    def mostrar_datos(self):
        super().mostrar_datos()
        print("Codigo Cargo: {}".format(self.__codCargo))  
        print("Catedra: {}".format(self.__catedra))
    