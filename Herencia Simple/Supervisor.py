from Empleado import Empleado
#Por antiguedad de 10 años o menos = +75000 Antiguedad de 10 años o mas = 125000
class Supervisor(Empleado):
    __antig: int
    def __init__(self, nombre, apellido, sueldo, antig):
        super().__init__(nombre, apellido, sueldo)
        self.__antig = antig

    def getImporteSueldo(self):
        if self.__antig >= 10:
            sueldo = self.getsueldo() + 125000
        elif self.__antig < 10:
            sueldo = self.getsueldo() + 125000
        return sueldo

    def __str__(self):
        return f"{super().__str__()} Antiguedad: {self.__antig} Años"