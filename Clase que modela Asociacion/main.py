from sala import Sala
from Pelicula import Pelicula
from Proyeccion import Proyeccion


if __name__ == '__main__':
    Sala2 = Sala(2,80)
    Pelicula33 = Pelicula(221,"Comedia", "Son Como Niños", 2013, "Denis Dugan")
    Proyeccion22 = Proyeccion("20/09/2023", "21:00", Sala2, Pelicula33)
    print (Proyeccion22)