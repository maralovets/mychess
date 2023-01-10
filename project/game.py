import pygame
from board import *
from b1 import Board
from dragger import Dragger


class Game:

    def __init__(self):
        self.next_player = 'white'
        self.board = Board()
        self.dragger = Dragger()

    def show_bg(self, surface):
        for row in range(rows):
            for col in range(columns):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(surface, white_color, (col * square_size, row * square_size, square_size, square_size))
                else:
                    pygame.draw.rect(surface, black_color, (col * square_size, row * square_size, square_size, square_size))

    def show_piece(self, surface):
        for row in range(rows):
            for col in range(columns):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * square_size + square_size//2, row * square_size + square_size//2
                        texture_rect = img.get_rect(center=img_center)
                        surface.blit(img, texture_rect)

    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            for move in piece.moves:
                if (move.final.row + move.final.col) % 2 == 0:
                    pygame.draw.rect(surface, '#C86464', (move.final.col * square_size, move.final.row * square_size, square_size, square_size))
                else:
                    pygame.draw.rect(surface, '#C84646', (move.final.col * square_size, move.final.row * square_size, square_size, square_size))

    def next_turn(self):
        if self.next_player == 'black':
            self.next_player = 'white'
        else:
            self.next_player = 'black'

    def reset(self):
        self.__init__()