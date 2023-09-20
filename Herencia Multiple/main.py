from Persona import Persona
from Docente import Docente
from Alumno import Alumno
from Ayudante import Ayudante

if __name__ == '__main__':
    Ayudante1 = Ayudante(44222333,"Augusto", "Manrique", 2231, "Analisis Matematico I", 9.25, "LSI", 6)
    Ayudante2 = Ayudante(45634424, "Cristian", "Álvarez", 33311, "Matematica Discreta", 8.50, "LSI", 12)
    Ayudante1.mostrar_datos()
    print ("{:=^125}".format(""))
    Ayudante2.mostrar_datos()
    