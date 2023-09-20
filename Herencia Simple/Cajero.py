from Empleado import Empleado
class Cajero(Empleado):
    __importeExtra: float
    def __init__(self, nombre, apellido, sueldo, importeExtra):
        super().__init__(nombre, apellido, sueldo)
        self.__importeExtra = importeExtra

    def getImporteSueldo(self):
        sueldo = self.getsueldo() + self.__importeExtra
        return sueldo
    
    def __str__(self):
        return f"{super().__str__()}"