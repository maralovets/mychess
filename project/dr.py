import pygame
from board import *
class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mousex = 0
        self.mousey = 0
        self.init_row = 0
        self.init_col = 0

    def upd_mouse(self, pos):
        self.mousex, self.mousey = pos

    def save_init(self, pos):
        self.init_row = pos[1] // square_size
        self.init_col = pos[0] // square_size

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False

    def upd_blit(self, surface):
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        img = pygame.image.load(texture)
        img_center = (self.mousex, self.mousey)
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)
