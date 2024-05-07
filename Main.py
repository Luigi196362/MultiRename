from concreto.RenombrarMusica import RenombrarMusica
from concreto.RenombrarPelicula import RenombrarPelicula
from concreto.RenombrarSerie import RenombrarSerie
from service.Directory import Directory
from service.Files import Files

ruta = Directory.getDir() #Obtener ruta de archivos
if ruta != "":
    #eleccion=int(input("¿Que deseas renombrar? 1.-Archivos 2.-Series 3.-Musica \n"))
    eleccion=2
    if eleccion == 1:
        
        fabrica=RenombrarPelicula()
        fabrica.RenombrarArchivo().renombrar(ruta)
    if eleccion == 2:
        
        fabrica=RenombrarSerie()
        fabrica.RenombrarArchivo().renombrar(ruta)
    if eleccion == 3:
        
        fabrica=RenombrarMusica()
        fabrica.RenombrarArchivo().renombrar(ruta)

    if 1<eleccion>3:
        print("Error")
    

