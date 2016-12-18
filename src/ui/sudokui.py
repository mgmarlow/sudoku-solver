from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class SudokuUI (Frame):
    def __init__(self, parent, puzzle):
        self.puzzle = puzzle
        self.parent = parent
        Frame.__init__(self, parent)
        self.row, self.col = 0, 0
        self.__initUI()

    def redraw (self, grid, time):
        self.parent.title("Sudoku solved in: %fs" % time)
        self.canvas.delete('numbers')
        self.__draw_cells(grid)

    def __initUI (self):
        self.parent.title('Sudoku')
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)
        self.__draw_grid()
        self.__draw_puzzle()

    def __draw_grid(self):
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

    def __draw_puzzle(self):
        self.canvas.delete('numbers')
        self.__draw_cells(self.puzzle)

    def __draw_cells (self, puzzle):
        for i in range(9):
            for j in range (9):
                cell = puzzle[i][j]
                if cell != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    self.canvas.create_text(x, y, text=cell, tags='numbers', fill='black')