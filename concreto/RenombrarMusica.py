from Base.Archivos.Archivo import Archivo
from Base.Archivos.Musica import Musica
from concreto.RenombradorArchivo import RenombradorArchivo

class RenombrarMusica(RenombradorArchivo):
    def RenombrarArchivo()-> Archivo:
        return Musica()
