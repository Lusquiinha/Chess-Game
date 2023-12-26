import pygame
from classes.board import ChessBoard

FPS = 30

class Game:
    def __init__(self, screen, clock):
        self.board = ChessBoard()
        self.running = True
        self.screen = screen
        self.clock = clock

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.board.select_square(mouse_x, mouse_y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.board.reset()
                elif event.key == pygame.K_DELETE:
                    self.board.delete_selected()

    def draw(self):
        self.board.draw(self.screen)

    def run(self):
        while self.running:
            self.clock.tick(FPS)

            self.handleEvents()

            # self.update()
        
            self.draw()


        # Update the display
            pygame.display.flip()

        pygame.quit()