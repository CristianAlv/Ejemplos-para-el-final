from DiscoRigido import DiscoRigido

class Computadora:
    __identificador: str
    __ram: int
    __disco: object
    def __init__(self, identificador, ram, disco):
        self.__identificador = identificador
        self.__ram = ram
        self.__disco = disco
    def __str__(self):
        return f"{self.__identificador} {self.__ram} {self.__disco}"