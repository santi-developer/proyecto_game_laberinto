import os
import readchar
from readchar import readkey, key

def covertir_mapa(mapa:str) -> list: 
    filas=mapa.split("\n")
    laberinto_lista_de_listas = [list(linea) for linea in filas]
                
    return laberinto_lista_de_listas  

def mostrer_laberinto(mapa:list):
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in mapa:
        for caracter in fila:
            print(caracter, end=" ")
            
        print() 
        
def main_loop(mapa:list, pos_inicial:tuple, pos_final:tuple):
    px,py=pos_inicial
    
    while (px,py)!= pos_final:
        
        mapa[px][py]='p'
        new_px=px
        new_py=py
        tecla=readkey()
        if tecla==key.UP and px-1>=0 and mapa[px-1][py]!='#':
            mapa[px][py]='.'
            new_px=px-1
            mapa[new_px][py]='p'
            px=new_px         
        elif tecla==key.DOWN and px+1<len(mapa[0]) and mapa[px+1][py]!='#':
            mapa[px][py]='.'
            new_px=px+1
            mapa[new_px][py]='p'
            px=new_px          
        elif tecla==key.LEFT and py-1>=0 and mapa[px][py-1]!='#':
            mapa[px][py]='.'
            new_py=py-1
            mapa[px][new_py]='p'
            py=new_py              
        elif tecla==key.RIGHT and py+1<len(mapa[0]) and mapa[px][py+1]!='#':
            mapa[px][py]='.'
            new_py=py+1
            mapa[px][new_py]='p'
            py=new_py  
            
        mostrer_laberinto(mapa)
    print("fin del juego")          
            
laberinto=covertir_mapa("..#########\n......#.#.#\n###.###.#.#\n#.....#.#.#\n#.###.#.#.#\n#.#.......#\n#.#####.###\n#.#...#...#\n#.#.###.#.#\n#.....#.#.#\n#########.#")
main_loop(laberinto,(0,0),(10,9))
 
            

            
