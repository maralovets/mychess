from board import *
from sq import Square
from piece import *
from move import Move


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(columns)]
        self.last_move = None
        self._create()
        self._add_piece('white')
        self._add_piece('black')

    def moving(self, piece, move):
        initial = move.initial
        final = move.final
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece
        if isinstance(piece, Pawn):
            self.check_prom(piece, final)
        if isinstance(piece, King):
            if self.castling(initial, final):
                dif = final.col - initial.col
                if dif < 0:
                    rook = piece.left_rook
                else:
                    rook = piece.right_rook
                self.moving(rook, rook.moves[-1])
        piece.moved = True
        piece.reset_moves()
        self.last_move = move

    def valid_move(self, piece, move):
        return move in piece.moves

    def check_prom(self, piece, final):
        if final.row == 0 or final.row == 7:
            self.squares[final.row][final.col].piece = Queen(piece.color)

    def castling(self, initial, final):
        return abs(initial.col - final.col) == 2


    def calc_moves(self, piece, row, col):

        def knight_moves():
            possible_moves = [(row-2, col+1), (row-1, col+2), (row+1, col+2), (row+2, col+1), (row+2, col-1), (row+1, col-2), (row-1, col-2), (row-2, col-1)]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)

        def pawn_moves():
            if piece.moved:
                steps = 1
            else:
                steps = 2
            start = row + piece.direction
            end = row + (piece.direction * (1 + steps))
            for move_row in range(start, end, piece.direction):
                if Square.in_range(move_row):
                    if self.squares[move_row][col].isempty():
                        initial = Square(row, col)
                        final = Square(move_row, col)
                        move = Move(initial, final)
                        piece.add_moves(move)
                    else:
                        break
                else:
                    break
            move_row = row + piece.direction
            move_cols = [col-1, col+1]
            for move_col in move_cols:
                if Square.in_range(move_row, move_col):
                    if self.squares[move_row][move_col].has_rival_piece(piece.color):
                        initial = Square(row, col)
                        final = Square(move_row, move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)

        def str_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr
                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            piece.add_moves(move)
                        elif self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color):
                            piece.add_moves(move)
                            break
                        elif self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                    else:
                        break
                    possible_move_row = possible_move_row + row_incr
                    possible_move_col = possible_move_col + col_incr

        def king_moves():
            possible_moves = [(row-1, col+1), (row-1, col-1), (row+1, col+1), (row+1, col-1), (row-1, col+0), (row+0, col+1), (row+1, col+0), (row+0, col-1)]
            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        move = Move(initial, final)
                        piece.add_moves(move)
            if not piece.moved:
                left_rook = self.squares[row][0].piece
                if isinstance(left_rook, Rook):
                    if not left_rook.moved:
                        for c in range(1, 4):
                            if self.squares[row][c].has_piece():
                                break
                            if c == 3:
                                piece.left_rook = left_rook
                                initial = Square(row, 0)
                                final = Square(row, 3)
                                move = Move(initial, final)
                                left_rook.add_moves(move)
                                initial = Square(row, col)
                                final = Square(row, 2)
                                move = Move(initial, final)
                                piece.add_moves(move)
                right_rook = self.squares[row][7].piece
                if isinstance(right_rook, Rook):
                    if not right_rook.moved:
                        for c in range(5, 7):
                            if self.squares[row][c].has_piece():
                                break
                            if c == 6:
                                piece.right_rook = right_rook
                                initial = Square(row, 7)
                                final = Square(row, 5)
                                move = Move(initial, final)
                                right_rook.add_moves(move)
                                initial = Square(row, col)
                                final = Square(row, 6)
                                move = Move(initial, final)
                                piece.add_moves(move)

        if isinstance(piece, Pawn):
            pawn_moves()

        if isinstance(piece, Knight):
            knight_moves()

        if isinstance(piece, Bishop):
            str_moves([(-1, 1), (-1, -1), (1, 1), (1, -1)])

        if isinstance(piece, Rook):
            str_moves([(-1, 0), (0, 1), (1, 0), (0, -1)])

        if isinstance(piece, Queen):
            str_moves([(-1, 1), (-1, -1), (1, 1), (1, -1), (-1, 0), (0, 1), (1, 0), (0, -1)])

        if isinstance(piece, King):
            king_moves()

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

