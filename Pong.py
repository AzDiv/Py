import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
PADDLE_SPEED = 5

# Create paddles
player1_paddle = pygame.Rect(50, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player2_paddle = pygame.Rect(WINDOW_WIDTH - 50 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Define ball
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5

# Create ball
ball = pygame.Rect(WINDOW_WIDTH // 2 - BALL_SIZE // 2, WINDOW_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Set up game variables
player1_score = 0
player2_score = 0
font = pygame.font.SysFont(None, 48)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s]:
        player1_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP]:
        player2_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN]:
        player2_paddle.y += PADDLE_SPEED

    # Keep paddles within the screen bounds
    player1_paddle.y = max(0, min(WINDOW_HEIGHT - PADDLE_HEIGHT, player1_paddle.y))
    player2_paddle.y = max(0, min(WINDOW_HEIGHT - PADDLE_HEIGHT, player2_paddle.y))

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= WINDOW_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= WINDOW_WIDTH:
        ball_speed_x *= -1

    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x *= -1

    # Check for scoring
    if ball.left <= 0:
        player2_score += 1
        ball.x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
        ball.y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = BALL_SPEED_X
        ball_speed_y = BALL_SPEED_Y
    elif ball.right >= WINDOW_WIDTH:
        player1_score += 1
        ball.x = WINDOW_WIDTH // 2 - BALL_SIZE // 2
        ball.y = WINDOW_HEIGHT // 2 - BALL_SIZE // 2
        ball_speed_x = -BALL_SPEED_X
        ball_speed_y = BALL_SPEED_Y

    # Fill the background with black
    window.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(window, WHITE, player1_paddle)
    pygame.draw.rect(window, WHITE, player2_paddle)
    pygame.draw.ellipse(window, WHITE, ball)

    # Draw scores
    player1_text = font.render(str(player1_score), True, WHITE)
    player2_text = font.render(str(player2_score), True, WHITE)
    window.blit(player1_text, (WINDOW_WIDTH // 4, 50))
    window.blit(player2_text, (3 * WINDOW_WIDTH // 4, 50))

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
