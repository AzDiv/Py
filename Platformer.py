import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Platformer')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up game variables
player_size = 50
player_speed = 5
player_jump_force = 15
player_gravity = 0.8
player = pygame.Rect(50, WINDOW_HEIGHT - player_size - 50, player_size, player_size)
player_y_momentum = 0

platforms = [
    pygame.Rect(0, WINDOW_HEIGHT - 40, WINDOW_WIDTH, 40),
    pygame.Rect(300, 400, 200, 20),
    pygame.Rect(500, 300, 200, 20),
    pygame.Rect(100, 200, 200, 20),
]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_y_momentum == 0:
                    player_y_momentum -= player_jump_force

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Apply gravity to the player
    player_y_momentum += player_gravity
    player.y += player_y_momentum

    # Check for collisions with platforms
    for platform in platforms:
        if player.colliderect(platform):
            if player_y_momentum > 0:
                player.y = platform.top - player.height
                player_y_momentum = 0
            elif player_y_momentum < 0:
                player.y = platform.bottom
                player_y_momentum = 0

    # Keep the player within the screen bounds
    player.x = max(0, min(WINDOW_WIDTH - player_size, player.x))
    player.y = max(0, min(WINDOW_HEIGHT - player_size, player.y))

    # Fill the background with black
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(window, WHITE, player)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(window, GREEN, platform)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
