import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# Set up colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black color
    screen.fill(BLACK)

    # Draw a red rectangle
    pygame.draw.rect(screen, RED, (width // 2 - 50, height // 2 - 50, 100, 100))

    # Update the display
    pygame.display.flip()

