class Cliente:
    __idCliente: int
    __nombreyApellido: str
    __domicilio: str
    __facturas: list
    def __init__(self, idCliente, nombreyApellido, domicilio):
        self.__idCliente = idCliente
        self.__nombreyApellido = nombreyApellido
        self.__domicilio = domicilio
        self.__facturas = []
    
    def agregarFacturas(self, unaFactura):
        self.__facturas.append(unaFactura)
        
    def getlista(self):
        for dato in self.__facturas:
            return(dato)
            
    
    def __str__(self):
        return f"{self.__idCliente} {self.__nombreyApellido} {self.__domicilio} {self.getlista()}"
        
    