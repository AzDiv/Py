import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Tower Defense')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up game variables
player_base = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT - 50, 100, 50)

enemies = []
enemy_speed = 1
enemy_spawn_rate = 50  # Lower value spawns more enemies
enemy_counter = 0

towers = []
tower_cost = 50
tower_range = 100
tower_damage = 10

bullets = []
bullet_speed = 5

resources = 100
font = pygame.font.SysFont(None, 24)

# Function to spawn enemies
def spawn_enemy():
    enemy_size = 20
    enemy = pygame.Rect(0, random.randint(50, WINDOW_HEIGHT - enemy_size - 50), enemy_size, enemy_size)
    enemies.append(enemy)

# Function to spawn towers
def spawn_tower(pos):
    tower = pygame.Rect(pos[0], pos[1], 30, 30)
    towers.append(tower)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if resources >= tower_cost:
                    spawn_tower(pygame.mouse.get_pos())
                    resources -= tower_cost

    # Spawn enemies
    enemy_counter += 1
    if enemy_counter == enemy_spawn_rate:
        spawn_enemy()
        enemy_counter = 0

    # Move enemies and remove off-screen ones
    for enemy in enemies[:]:
        enemy.x += enemy_speed
        if enemy.left >= WINDOW_WIDTH:
            enemies.remove(enemy)

    # Check for collisions between enemies and player base
    for enemy in enemies:
        if enemy.colliderect(player_base):
            running = False

    # Check for collisions between bullets and enemies
    for bullet in bullets[:]:
        bullet.x += bullet_speed
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                resources += 10  # Earn resources for each defeated enemy

    # Draw the background
    window.fill(BLACK)

    # Draw the player base
    pygame.draw.rect(window, RED, player_base)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(window, GREEN, enemy)

    # Draw towers
    for tower in towers:
        pygame.draw.rect(window, BLUE, tower)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(window, WHITE, bullet)

    # Draw resources
    resources_text = font.render(f'Resources: {resources}', True, WHITE)
    window.blit(resources_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
