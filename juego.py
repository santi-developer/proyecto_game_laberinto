import os
from readchar import readkey, key

class Juego:
    def __init__(self):
        self.laberinto = self.covertir_mapa(
            "..#########\n"
            "......#.#.#\n"
            "###.###.#.#\n"
            "#.....#.#.#\n"
            "#.###.#.#.#\n"
            "#.#.......#\n"
            "#.#####.###\n"
            "#.#...#...#\n"
            "#.#.###.#.#\n"
            "#.....#.#.#\n"
            "#########.#"
        )
        self.pos_inicial = (0, 0)
        self.pos_final = (10, 9)

    def covertir_mapa(self, mapa):
        filas = mapa.split("\n")
        laberinto_lista_de_listas = [list(linea) for linea in filas]
        return laberinto_lista_de_listas  

    def mostrar_laberinto(self, mapa):
        os.system('cls' if os.name == 'nt' else 'clear')
        for fila in mapa:
            for caracter in fila:
                print(caracter, end=" ")
            print()

    def main_loop(self):
        px, py = self.pos_inicial

        while (px, py) != self.pos_final:
            self.laberinto[px][py] = 'p'
            new_px = px
            new_py = py
            tecla = readkey()

            if tecla == key.UP and px - 1 >= 0 and self.laberinto[px - 1][py] != '#':
                self.laberinto[px][py] = '.'
                new_px = px - 1
                self.laberinto[new_px][py] = 'p'
                px = new_px
            elif tecla == key.DOWN and px + 1 < len(self.laberinto) and self.laberinto[px + 1][py] != '#':
                self.laberinto[px][py] = '.'
                new_px = px + 1
                self.laberinto[new_px][py] = 'p'
                px = new_px
            elif tecla == key.LEFT and py - 1 >= 0 and self.laberinto[px][py - 1] != '#':
                self.laberinto[px][py] = '.'
                new_py = py - 1
                self.laberinto[px][new_py] = 'p'
                py = new_py
            elif tecla == key.RIGHT and py + 1 < len(self.laberinto[0]) and self.laberinto[px][py + 1] != '#':
                self.laberinto[px][py] = '.'
                new_py = py + 1
                self.laberinto[px][new_py] = 'p'
                py = new_py

            self.mostrar_laberinto(self.laberinto)

        print("Fin del juego")

def main():
    juego = Juego()
    juego.main_loop()

if __name__ == "__main__":
    main()