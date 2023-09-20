from claseRegistroTrabajo import RegistroTrabajo
from Tarea import Tarea
from Empleado import Empleado


if __name__ == '__main__':
    Persona1 = Empleado("Cristian", "45634424", "Ingeniero Civil", "2646281622")
    Tarea1 = Tarea("Inspeccion de Materiales", "19/09/2023", "20/09/2023")
    RegistroTT = RegistroTrabajo(30, Persona1, Tarea1)
    Persona1.agregarTareas(Tarea1)
    print (RegistroTT)