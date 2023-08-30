import os
from readchar import readkey, key
from functools import reduce
import random

class Juego:
    def __init__(self,pos_inicial,pos_final,laberinto):
        self._laberinto =self._covertir_mapa(laberinto)
        self._pos_inicial = pos_inicial
        self._pos_final = pos_final

    def _covertir_mapa(self, mapa:str):
        filas = mapa.split("\n")
        laberinto_lista_de_listas = list(map(list, filas))
        return laberinto_lista_de_listas
            

    def _mostrar_laberinto(self, mapa):
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in mapa:
            for caracter in fila:
                print(caracter, end=" ")
            print()

    def _main_loop(self):
        px, py = self._pos_inicial

        while (px, py) != self._pos_final:
            self._laberinto[px][py] = 'p'
            new_px = px
            new_py = py
            tecla = readkey()

            if tecla == key.UP and px - 1 >= 0 and self._laberinto[px - 1][py] != '#':
                self._laberinto[px][py] = '.'
                new_px = px - 1
                self._laberinto[new_px][py] = 'p'
                px = new_px
            elif tecla == key.DOWN and px + 1 < len(self._laberinto) and self._laberinto[px + 1][py] != '#':
                self._laberinto[px][py] = '.'
                new_px = px + 1
                self._laberinto[new_px][py] = 'p'
                px = new_px
            elif tecla == key.LEFT and py - 1 >= 0 and self._laberinto[px][py - 1] != '#':
                self._laberinto[px][py] = '.'
                new_py = py - 1
                self._laberinto[px][new_py] = 'p'
                py = new_py
            elif tecla == key.RIGHT and py + 1 < len(self._laberinto[0]) and self._laberinto[px][py + 1] != '#':
                self._laberinto[px][py] = '.'
                new_py = py + 1
                self._laberinto[px][new_py] = 'p'
                py = new_py

            self._mostrar_laberinto(self._laberinto)

        print("Fin del juego")
        
class JuegoArchivo(Juego):
    
    def __init__(self,direccion_carpeta):
        self._direccion_carpeta=direccion_carpeta
        self._lista_archivos=os.listdir(self._direccion_carpeta)
        self._ElElegido=random.choice(self._lista_archivos)
        self._direccionReal=path_completo = f"{self._direccion_carpeta}/{self._ElElegido}"
        
        
    def _leer_datos(self):
        
        with open(self._direccionReal, 'r') as archivo:
            contenido = archivo.readlines()
            coordenadas=contenido[0].strip().split()
            x=int(coordenadas[0])
            y=int(coordenadas[1])
            x_fin=int(coordenadas[2])
            y_fin=int(coordenadas[3])
            coord_inicial=(x,y)
            coord_final=(x_fin,y_fin)
            labe= reduce(lambda acumulado, linea: acumulado + linea, contenido[1:], "")
            print(type(coord_final))
            return coord_inicial, coord_final,labe
          
        
        
def main ():         
    prueba=JuegoArchivo('D:\\laberintos')
    pos_ini,pos_final,laberinto=prueba._leer_datos()  
    juego=Juego(pos_ini,pos_final, laberinto)
    juego._main_loop()

    
if __name__=="__main__":
    main()     
        
    