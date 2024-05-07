from Base.Archivos.Archivo import Archivo
from Base.Archivos.Pelicula import Pelicula
from concreto.RenombradorArchivo import RenombradorArchivo


class RenombrarPelicula (RenombradorArchivo):
    def RenombrarArchivo(self) -> Archivo:
        return Pelicula()