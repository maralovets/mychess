from board import *
from sq import Square
from piece import *


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(columns)]

        self._create()
        self._add_piece('white')
        self._add_piece('black')

    def _create(self):
        for row in range(rows):
            for col in range(columns):
                self.squares[row][col] = Square(row, col)
    def _add_piece(self, color):
        if color == 'white':
            row_pawn, row_p = (6, 7)
        else:
            row_pawn, row_p = (1, 0)
        for col in range(columns):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        self.squares[row_p][1] = Square(row_p, 1, Knight(color))
        self.squares[row_p][6] = Square(row_p, 6, Knight(color))

        self.squares[row_p][2] = Square(row_p, 2, Bishop(color))
        self.squares[row_p][5] = Square(row_p, 5, Bishop(color))

        self.squares[row_p][0] = Square(row_p, 0, Rook(color))
        self.squares[row_p][7] = Square(row_p, 7, Rook(color))

        self.squares[row_p][4] = Square(row_p, 4, King(color))

        self.squares[row_p][3] = Square(row_p, 3, Queen(color))

