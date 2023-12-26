import pygame
from classes.board import ChessBoard

pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 800  # Set the dimensions to 800x800
FPS = 30

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

clock = pygame.time.Clock()

# Your chess game code goes here...
def run():
    board = ChessBoard()
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    board.select_square(mouse_x, mouse_y)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    board.reset()
                elif event.key == pygame.K_DELETE:
                    board.delete_selected()

        board.draw(screen)

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    run()