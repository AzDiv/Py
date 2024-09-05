import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Simple Game')

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initial position of the square
square_x = 300
square_y = 200

# Define the square size
square_size = 50

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key presses
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                square_x -= 10
            elif event.key == pygame.K_RIGHT:
                square_x += 10
            elif event.key == pygame.K_UP:
                square_y -= 10
            elif event.key == pygame.K_DOWN:
                square_y += 10

    # Fill the background with white
    window.fill(WHITE)

    # Draw the square
    pygame.draw.rect(window, RED, (square_x, square_y, square_size, square_size))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
