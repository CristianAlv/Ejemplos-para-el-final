class DiscoRigido:
    __marca: str
    __capacidad: int
    def __init__(self, marca, capacidad):
        self.__marca = marca
        self.__capacidad = capacidad
    
    def __str__(self):
        return f"{self.__marca} {self.__capacidad}"