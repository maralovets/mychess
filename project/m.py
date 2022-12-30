import pygame
import sys
from board import *
from game import Game





class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_piece(screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.upd_mouse(self, event.pos)
                    clicked_row = event.pos[1] // square_size
                    clicked_col = event.pos[0] // square_size
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board[clicked_row][clicked_col].piece
                        dragger.save_init(self, event.pos)
                        dragger.drag_piece(self, piece)

                elif event.type == pygame.MOUSEMOTION:
                    dragger.upd_mouse(self, event.pos)
                    dragger.upd_blit(self, screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
