from claseFase import Fase
from claseObra import Obra

if __name__ == '__main__':
    fechaInicio= str(input("Ingrese fecha de inicio de obra: "))
    fechaFin = str(input("Ingrese fecha de final de obra: "))
    Obra1 = Obra ("La Cabaña", "Libertador 33 Oeste")
    Obra1.agregarobra(fechaInicio, fechaFin)
    del Obra1
    print(Obra1)
    
