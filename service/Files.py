import os


class Files:
    def  read(ruta,extension):
    # Lista para almacenar los nombres de los archivos
        archivos = []
        # Iterar sobre los archivos en la ruta
        j=0

        if len(os.listdir(ruta))>0:
            for i in range (len(extension)):    
                for archivo in os.listdir(ruta):
                    # Comprobar si el archivo tiene la extensión deseada
                    
                    if archivo.endswith(extension[i]):
                        archivos.append(archivo)
                        j=j+1

            archivos.sort()
            
            """
            #Prueba consola                        
            print("Files function: ")     
            print("Archivos encontrados: "+str(len(archivos)))
            for i in range (len(archivos)):
                print(archivos[i])
            print("_____________________________")     
            #Prueba consola
            """

            
        else:
            print("No se encontraron archivos")            
        
        return archivos