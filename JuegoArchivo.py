from juego import Juego
import os
import random
class JuegoArchivo(Juego):
    
    def __init__(self,direccion_carpeta):
        self.direccion_carpeta=direccion_carpeta
        self.lista_archivos=os.listdir(self.direccion_carpeta)
        self.ElElegido=random.choice(self.lista_archivos)
        self.direccionReal=path_completo = f"{self.direccion_carpeta}/{self.ElElegido}"
        
        
    def leer_datos(self):
        
        with open(self.direccionReal, 'r') as archivo:
            contenido = archivo.read()
            contenido_sinEspacios=contenido.strip()
            return contenido_sinEspacios
        
prueba=JuegoArchivo('D:\laberintos')
prueba.leer_datos()
       
      

    