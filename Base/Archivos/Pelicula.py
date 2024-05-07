from Base.Archivos.Archivo import Archivo


class Pelicula (Archivo):
    
    def renombrar(self, ruta) -> str:
        for i in range (len (ruta)):
            print(ruta+" 🟨")