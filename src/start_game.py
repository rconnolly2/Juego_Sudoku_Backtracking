from generar_sudoku import *
from juego_sudoku import *
from signal import *
from solucionar_sudoku import *


# Le he implementado singleton a la clase Sudoku para solo poder crear un objeto de Sudoku
mi_sudoku = Sudoku("Sudoku Juego")
mi_sudoku.dibujar_tabla()
mi_sudoku.dibujar_menu()
mi_sudoku.run_sudoku()
# Aquí si creas otro sudoku te devolverá el objeto ya creado
#mi_sudoku2 = Sudoku("Sudoku Juego 2")
#print(str(mi_sudoku2.ventana.title()))