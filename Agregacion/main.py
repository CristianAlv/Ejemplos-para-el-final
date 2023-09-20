from Computadora import Computadora
from DiscoRigido import DiscoRigido

if __name__ == '__main__':
    DiscoRigido1 = DiscoRigido("Kingston", 512)
    ComputadoraLIA04 = Computadora("IEWDDC-WWQQ", 16, DiscoRigido1)
    print (ComputadoraLIA04)
    