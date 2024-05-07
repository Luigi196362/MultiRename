from Base.Archivos.Archivo import Archivo
from Base.Archivos.Serie import Serie
from concreto.RenombradorArchivo import RenombradorArchivo


class RenombrarSerie(RenombradorArchivo) :
    def RenombrarArchivo(self) -> Archivo:
        return Serie()