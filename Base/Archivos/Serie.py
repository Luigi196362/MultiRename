from Base.Archivos.Archivo import Archivo
from service.Files import Files


class Serie (Archivo) :
    
    def renombrar(self,ruta) -> str:
        extensiones=[".mp4",".avi",".mov",".mkv",".wmv",".flv",".mpeg",".mpg"]
        
        archivos=Files.read(ruta,extensiones)
        
        #Prueba consola                        
        print("_____________________________")     
        print("\nSerie function: \n")     
        print("Archivos encontrados: "+str(len(archivos)))
        for i in range (len(archivos)):
            print(archivos[i])
        print("_____________________________\n\n")     
        #Prueba consola
        