import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong with AI")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle dimensions and properties
paddle_width = 10
paddle_height = 100
paddle_speed = 10

# Player paddle
player_x = 50
player_y = screen_height // 2 - paddle_height // 2

# AI Paddle
ai_x = screen_width - 50 - paddle_width
ai_y = screen_height // 2 - paddle_height // 2
ai_speed = 7  # Slower than player to make it beatable

# Ball properties
ball_size = 15
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 5 * random.choice([-1, 1])  # Initial random direction
ball_speed_y = 5 * random.choice([-1, 1])  # Initial random direction

# Score
player_score = 0
ai_score = 0
font = pygame.font.Font(None, 36) # Default font, size 36

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= paddle_speed
    if keys[pygame.K_DOWN]:
        player_y += paddle_speed

    # Keep player paddle within bounds
    player_y = max(0, min(player_y, screen_height - paddle_height))

    # AI Logic (Simple AI)
    if ai_y + paddle_height // 2 < ball_y:  # Ball below AI
        ai_y += ai_speed
    elif ai_y + paddle_height // 2 > ball_y:  # Ball above AI
        ai_y -= ai_speed

    # Keep AI paddle within bounds
    ai_y = max(0, min(ai_y, screen_height - paddle_height))

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball_y - ball_size // 2 <= 0 or ball_y + ball_size // 2 >= screen_height:
        ball_speed_y *= -1  # Reverse vertical direction

    # Ball collision with paddles
    player_paddle_rect = pygame.Rect(player_x, player_y, paddle_width, paddle_height)
    ai_paddle_rect = pygame.Rect(ai_x, ai_y, paddle_width, paddle_height)
    ball_rect = pygame.Rect(ball_x - ball_size // 2, ball_y - ball_size // 2, ball_size, ball_size) # Rect representation for ball

    if ball_rect.colliderect(player_paddle_rect):
        ball_speed_x *= -1  # Reverse horizontal direction
        ball_speed_x += 1 # Increase ball speed slightly
        ball_speed_y += random.choice([-1, 1]) # Add a bit of angle change

    if ball_rect.colliderect(ai_paddle_rect):
        ball_speed_x *= -1 # Reverse horizontal direction
        ball_speed_x -= 1 # Reduce speed after AI paddle
        ball_speed_y += random.choice([-1, 1])

    # Ball out of bounds (scoring)
    if ball_x - ball_size // 2 <= 0:  # AI scores
        ai_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x = 5 * random.choice([-1, 1])
        ball_speed_y = 5 * random.choice([-1, 1])
    elif ball_x + ball_size // 2 >= screen_width:  # Player scores
        player_score += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x = 5 * random.choice([-1, 1])
        ball_speed_y = 5 * random.choice([-1, 1])

    # Drawing
    screen.fill(black)  # Clear the screen

    # Draw paddles
    pygame.draw.rect(screen, white, (player_x, player_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (ai_x, ai_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_size // 2)

    # Draw scores
    player_text = font.render(str(player_score), True, white)
    ai_text = font.render(str(ai_score), True, white)
    screen.blit(player_text, (screen_width // 4, 20))
    screen.blit(ai_text, (screen_width * 3 // 4, 20))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    pygame.time.Clock().tick(60)  # Limit to 60 frames per second

# Quit Pygame
pygame.quit()

