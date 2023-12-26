import pygame
from classes.game import Game

pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 800  # Set the dimensions to 800x800

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

clock = pygame.time.Clock()

if __name__ == "__main__":
    game = Game(screen, clock)
    game.run()