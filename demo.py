import json;
import glob
import os


from service.Directory import Directory

Ruta = Directory.getDir() #Obtener ruta de archivos
with open('Data/Palabras.json',encoding='utf-8') as f:
    data= json.load(f)

Serie = 'Demon Slayer'
Temporada = "04"
Nombre= data ['Demon Slayer4']
Inicio=1
NumEpisodio=Inicio-1
nuevoNombreArchivo = []
format='mp4'
formato='./*'+format
formatotxt='.'+format
print (formatotxt)
archivos = glob.glob(Ruta+formato)

print("Archivos encontrados  "+ str(len(archivos)) +" :")

for i in range (len(archivos)):
    print (archivos[i]+" 🟨 ")

input("Continuar?")
if NumEpisodio<len(archivos):
    for i in range (len(archivos)):
        if (NumEpisodio+1)<10:
            NumEpisodiotxt= "0"+str(NumEpisodio+1)
        else:
            NumEpisodiotxt= str(NumEpisodio+1)
        
        nuevoNombreArchivo.append(Ruta+".\\"+Serie+" "+Temporada+"x"+str(NumEpisodiotxt)+" "+Nombre[NumEpisodio]+formatotxt)

        print("\n 🟥 "+archivos[i]+"  \n 🟦 "+nuevoNombreArchivo[i])
        NumEpisodio=NumEpisodio+1
    
    NumEpisodio=Inicio-1

    input("Continuar?")
    for i in range (len (nuevoNombreArchivo)):
        print("\n 🟥 "+archivos[i],Ruta+" 🟥 \n 🟩 "+nuevoNombreArchivo[i]+" 🟩 ")
        os.rename(archivos[i],nuevoNombreArchivo[i])
        NumEpisodio=NumEpisodio+1
        
    print ("Escritura completada")