import datetime
class Factura:
    __numFactura: str
    __fecha: datetime
    __importe: float
    __cuit: str
    def __init__(self, numFactura, fecha, importe, cuit):
        self.__numFactura = numFactura
        self.__fecha = fecha
        self.__importe= importe
        self.__cuit = cuit
        
    def getnumFactura(self):
        return self.__numFactura
    def getfecha(self):
        return self.__fecha
    def getimporte(self):
        return self.__importe
    def getcuit(self):
        return self.__cuit
        
    def __str__(self):
        return f"{self.getnumFactura()} {self.getfecha()} {self.getimporte()} {self.getcuit()}"