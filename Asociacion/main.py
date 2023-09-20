from Factura import Factura
from Cliente import Cliente


if __name__ == '__main__':
    Cliente1 = Cliente(33, "Cristian Álvarez", "Las Heras 139 Sur")
    Factura2= Factura("22333333334", "20/09/2023", 334422.22, "20-45634424-4")
    Cliente1.agregarFacturas(Factura2)
    print (Cliente1)