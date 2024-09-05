import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Endless Runner')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up game variables
player_size = 50
player_speed = 5
player = pygame.Rect(50, WINDOW_HEIGHT - player_size - 50, player_size, player_size)
player_y_momentum = 0

obstacles = []
obstacle_speed = 5
obstacle_spawn_rate = 50  # Lower value spawns more obstacles
obstacle_counter = 0

coins = []
coin_spawn_rate = 100  # Lower value spawns more coins
coin_counter = 0

score = 0
font = pygame.font.SysFont(None, 48)

# Function to spawn obstacles
def spawn_obstacle():
    obstacle_size = random.randint(20, 100)
    obstacle = pygame.Rect(WINDOW_WIDTH, WINDOW_HEIGHT - obstacle_size - 50, obstacle_size, obstacle_size)
    obstacles.append(obstacle)

# Function to spawn coins
def spawn_coin():
    coin_size = 20
    coin = pygame.Rect(WINDOW_WIDTH, random.randint(50, WINDOW_HEIGHT - coin_size - 50), coin_size, coin_size)
    coins.append(coin)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and player.y >= WINDOW_HEIGHT - player_size - 50:
        player_y_momentum = -15

    player_y_momentum += 0.5
    player.y += player_y_momentum

    # Spawn obstacles
    obstacle_counter += 1
    if obstacle_counter == obstacle_spawn_rate:
        spawn_obstacle()
        obstacle_counter = 0

    # Move obstacles and remove off-screen ones
    for obstacle in obstacles[:]:
        obstacle.x -= obstacle_speed
        if obstacle.right <= 0:
            obstacles.remove(obstacle)

    # Spawn coins
    coin_counter += 1
    if coin_counter == coin_spawn_rate:
        spawn_coin()
        coin_counter = 0

    # Move coins and remove off-screen ones
    for coin in coins[:]:
        coin.x -= obstacle_speed
        if coin.right <= 0:
            coins.remove(coin)

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            running = False

    # Check for collisions with coins
    for coin in coins[:]:
        if player.colliderect(coin):
            coins.remove(coin)
            score += 10

    # Fill the background with black
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(window, WHITE, player)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(window, RED, obstacle)

    # Draw coins
    for coin in coins:
        pygame.draw.rect(window, GREEN, coin)

    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
 