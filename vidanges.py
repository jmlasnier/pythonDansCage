import pygame
import random

# initialize pygame
pygame.init()

# set screen dimensions
screen_width = 640
screen_height = 480

# create screen
screen = pygame.display.set_mode((screen_width, screen_height))

# set title and icon
pygame.display.set_caption("Pong")
icon = pygame.image.load('pong_icon.png')
pygame.display.set_icon(icon)

# load images
paddle_image = pygame.image.load('paddle.png')
ball_image = pygame.image.load('ball.png')

# set paddle and ball dimensions
paddle_width = paddle_image.get_width()
paddle_height = paddle_image.get_height()
ball_width = ball_image.get_width()
ball_height = ball_image.get_height()

# set game variables
paddle_left = screen_width / 2 - paddle_width / 2
paddle_right = screen_width / 2 - paddle_width / 2
ball_x = screen_width / 2 - ball_width / 2
ball_y = screen_height / 2 - ball_height / 2
velocity_x = random.randint(-2, 2)
velocity_y = random.randint(-2, 2)
score_left = 0
score_right = 0

# set font
font = pygame.font.Font('freesansbold.ttf', 32)

# set colors
white = (255, 255, 255)

# define function for drawing paddles
def draw_paddles():
    screen.blit(paddle_image, (paddle_left, screen_height - paddle_height))
    screen.blit(paddle_image, (paddle_right, 0))

# define function for drawing ball
def draw_ball():
    screen.blit(ball_image, (ball_x, ball_y))

# define function for drawing scores
def draw_scores():
    score_text = font.render(f"{score_left}  |  {score_right}", True, white)
    score_rect = score_text.get_rect()
    score_rect.center = (screen_width / 2, screen_height / 8)
    screen.blit(score_text, score_rect)

# define function for updating game state
def update_game():
    global ball_x, ball_y, velocity_x, velocity_y, score_left, score_right

    # move ball
    ball_x += velocity_x
    ball_y += velocity_y

    # check for ball collision with wall
    if ball_y <= 0 or ball_y + ball_height >= screen_height:
        velocity_y = -velocity_y
    if ball_x <= 0 or ball_x + ball_width >= screen_width:
        velocity_x = -velocity_x

    # check for ball collision with paddle
    if ball_y <= paddle_height and paddle_right < ball_x < paddle_right + paddle_width:
        velocity_y
