import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Invaders')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up game variables
player_size = 50
player_speed = 5
player = pygame.Rect(WINDOW_WIDTH // 2 - player_size // 2, WINDOW_HEIGHT - 100, player_size, player_size)

bullet_size = 10
bullet_speed = 7
bullets = []

alien_size = 50
alien_speed = 2
alien_rows = 3
alien_cols = 10
aliens = []
for row in range(alien_rows):
    for col in range(alien_cols):
        alien = pygame.Rect(100 + col * (alien_size + 10), 50 + row * (alien_size + 10), alien_size, alien_size)
        aliens.append(alien)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.centerx - bullet_size // 2, player.top - bullet_size, bullet_size, bullet_size)
                bullets.append(bullet)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Keep the player within the screen bounds
    player.x = max(0, min(WINDOW_WIDTH - player_size, player.x))

    # Move the bullets
    for bullet in bullets:
        bullet.y -= bullet_speed

    # Check for collisions between bullets and aliens
    for bullet in bullets[:]:
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)

    # Draw the background
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(window, WHITE, player)

    # Draw the bullets
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, bullet)

    # Draw the aliens
    for alien in aliens:
        pygame.draw.rect(window, RED, alien)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
