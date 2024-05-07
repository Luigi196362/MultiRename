import tkinter as tk
from tkinter import filedialog
   
class Directory:
    def getDir():
        root = tk.Tk()
        root.withdraw() # Oculta la ventana principal de tkinter
        
        # Abre el explorador de archivos y permite al usuario seleccionar una carpeta
        carpeta_seleccionada = filedialog.askdirectory()
        ruta = (carpeta_seleccionada)
        if carpeta_seleccionada:
            print("Carpeta seleccionada:", carpeta_seleccionada)
            # Aquí puedes realizar las operaciones que desees con la carpeta seleccionada
        else:
            print("Error: No se seleccionó ninguna carpeta.")
        
        return ruta
    
