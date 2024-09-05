import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Frogger')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)

# Set up game variables
player_size = 40
player_speed = 20
player = pygame.Rect(WINDOW_WIDTH // 2 - player_size // 2, WINDOW_HEIGHT - player_size - 10, player_size, player_size)
player_starting_position = player.center

vehicle_speeds = [5, 7, 9]
vehicles = []
vehicle_spawn_rate = 50
vehicle_counter = 0

log_speeds = [3, 4, 5]
logs = []
log_spawn_rate = 100
log_counter = 0

score = 0
font = pygame.font.SysFont(None, 48)

# Function to spawn vehicles
def spawn_vehicle():
    vehicle_size = 40
    lane = random.randint(0, 2)
    vehicle = pygame.Rect(-vehicle_size if lane % 2 == 0 else WINDOW_WIDTH, 50 + lane * 100, vehicle_size, vehicle_size)
    speed = random.choice(vehicle_speeds)
    vehicles.append((vehicle, speed))

# Function to spawn logs
def spawn_log():
    log_size = random.randint(80, 160)
    log = pygame.Rect(-log_size, 200 + random.choice([0, 100]), log_size, 40)
    speed = random.choice(log_speeds)
    logs.append((log, speed))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # Keep the player within the screen bounds
    player.x = max(0, min(WINDOW_WIDTH - player_size, player.x))
    player.y = max(0, min(WINDOW_HEIGHT - player_size, player.y))

    # Spawn vehicles
    vehicle_counter += 1
    if vehicle_counter == vehicle_spawn_rate:
        spawn_vehicle()
        vehicle_counter = 0

    # Move vehicles and remove off-screen ones
    for vehicle in vehicles[:]:
        vehicle[0].x += vehicle[1]
        if vehicle[0].right <= 0 or vehicle[0].left >= WINDOW_WIDTH:
            vehicles.remove(vehicle)

    # Spawn logs
    log_counter += 1
    if log_counter == log_spawn_rate:
        spawn_log()
        log_counter = 0

    # Move logs and remove off-screen ones
    for log in logs[:]:
        log[0].x += log[1]
        if log[0].right <= 0 or log[0].left >= WINDOW_WIDTH:
            logs.remove(log)

    # Check for collisions with vehicles
    for vehicle in vehicles:
        if player.colliderect(vehicle[0]):
            player.center = player_starting_position

    # Check for collisions with logs
    on_log = False
    for log in logs:
        if player.colliderect(log[0]):
            on_log = True
            player.x += log[1]

    # Check for reaching the other side
    if player.y <= 10:
        if on_log:
            score += 10
            player.center = player_starting_position
        else:
            player.y = 10

    # Fill the background with blue (water)
    window.fill(BLUE)

    # Draw the road (brown)
    pygame.draw.rect(window, BROWN, (0, 50, WINDOW_WIDTH, 300))

    # Draw the grass (green)
    pygame.draw.rect(window, GREEN, (0, 350, WINDOW_WIDTH, 250))

    # Draw the player (white)
    pygame.draw.rect(window, WHITE, player)

    # Draw vehicles (white)
    for vehicle in vehicles:
        pygame.draw.rect(window, WHITE, vehicle[0])

    # Draw logs (brown)
    for log in logs:
        pygame.draw.rect(window, BROWN, log[0])

    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
