
# Pong:

# Pong is a two-dimensional sports game.
# Two players control paddles vertically on opposite sides of the screen.
# A ball moves between the paddles, and players aim to hit the ball past their opponent's paddle.
# The game continues until one player fails to return the ball.

import pygame
import random
import sys  # To exit the game when a player wins

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 90
left_paddle = pygame.Rect(50, (SCREEN_HEIGHT / 2) - (PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(SCREEN_WIDTH - 50 - PADDLE_WIDTH, (SCREEN_HEIGHT / 2) - (PADDLE_HEIGHT / 2), PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 6

# Ball settings
# Ball settings with moderately faster speed
ball_speed_x, ball_speed_y = 3 * random.choice((1, -1)), 3 * random.choice((1, -1))
ball = pygame.Rect(SCREEN_WIDTH / 2 - 15, SCREEN_HEIGHT / 2 - 15, 30, 30)

# Score
left_score, right_score = 0, 0
winning_score = 5  # The score needed to win the game
font = pygame.font.Font(None, 74)

def display_winner(text):
    win_text = font.render(text, True, WHITE)
    screen.blit(win_text, (SCREEN_WIDTH / 2 - win_text.get_width() / 2, SCREEN_HEIGHT / 2 - win_text.get_height() / 2))
    pygame.display.flip()
    pygame.time.delay(3000)  # Pause for 3 seconds before closing
    pygame.quit()
    sys.exit()

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < SCREEN_HEIGHT:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < SCREEN_HEIGHT:
        right_paddle.y += paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    
    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1  # Reverses direction without increasing speed
    
    # Score update and checking for a winner
    if ball.left <= 0:
        right_score += 1
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        ball_speed_x, ball_speed_y = 2 * random.choice((1, -1)), 2 * random.choice((1, -1))
        if right_score == winning_score:
            display_winner("Right Player Wins!")
    if ball.right >= SCREEN_WIDTH:
        left_score += 1
        ball.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        ball_speed_x, ball_speed_y = 2 * random.choice((1, -1)), 2 * random.choice((1, -1))
        if left_score == winning_score:
            display_winner("Left Player Wins!")
    
    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))
    
    # Displaying scores
    left_score_display = font.render(str(left_score), True, WHITE)
    screen.blit(left_score_display, (SCREEN_WIDTH / 4, 10))
    right_score_display = font.render(str(right_score), True, WHITE)
    screen.blit(right_score_display, (3 * SCREEN_WIDTH / 4, 10))
    
    # Updating the window
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()
