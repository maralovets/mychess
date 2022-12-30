import pygame
from board import *
from b1 import Board
from dr import Dragger


class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger

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

                    img = pygame.image.load(piece.texture)
                    img_center = col * square_size + square_size//2, row * square_size + square_size//2
                    texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, texture_rect)
