import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up game variables
snake = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]
snake_direction = 'right'
food = (random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
        random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)
score = 0
font = pygame.font.SysFont(None, 48)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'down':
                snake_direction = 'up'
            elif event.key == pygame.K_DOWN and snake_direction != 'up':
                snake_direction = 'down'
            elif event.key == pygame.K_LEFT and snake_direction != 'right':
                snake_direction = 'left'
            elif event.key == pygame.K_RIGHT and snake_direction != 'left':
                snake_direction = 'right'

    # Move the snake
    head_x, head_y = snake[0]
    if snake_direction == 'up':
        head_y -= CELL_SIZE
    elif snake_direction == 'down':
        head_y += CELL_SIZE
    elif snake_direction == 'left':
        head_x -= CELL_SIZE
    elif snake_direction == 'right':
        head_x += CELL_SIZE

    # Check for collisions with walls
    if head_x < 0 or head_x >= WINDOW_WIDTH or head_y < 0 or head_y >= WINDOW_HEIGHT:
        running = False

    # Check for collision with itself
    if (head_x, head_y) in snake[1:]:
        running = False

    # Check for collision with food
    if (head_x, head_y) == food:
        score += 1
        snake.append(snake[-1])  # Increase snake length
        food = (random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
                random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE)

    # Update snake position
    snake = [(head_x, head_y)] + snake[:-1]

    # Fill the background with black
    window.fill(BLACK)

    # Draw food
    pygame.draw.rect(window, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Draw snake
    for segment in snake:
        pygame.draw.rect(window, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

    # Draw score
    score_text = font.render(f'Score: {score}', True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(10)

# Quit Pygame
pygame.quit()
sys.exit()
