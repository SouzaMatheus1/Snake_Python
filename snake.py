import random
import pygame
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def feed(cel1, cel2):
    return (cel1[0] == cel2[0]) and (cel1[1] == cel2[1])

def collision_snake(c1):
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            return True

def collision_wall(c1):
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        return True

up = 0
right = 1
left = 2
down = 3
direction = left
game_over = False

# Screen creation
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

# Snake creation
snake = [(200,200), (210,200), (220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

# Apple creation
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
apple_pos = on_grid_random()

clock = pygame.time.Clock()
tick = 10

while True:
    clock.tick(tick)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if feed(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
        tick += 0.5

    if collision_snake(snake):
        game_over = collision_snake(snake)
        
    if collision_wall(snake):
        game_over = True

    if game_over:
        break
    
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if event.type == KEYDOWN:
        if event.key == K_UP:
            direction = up
        if event.key == K_DOWN:
            direction = down
        if event.key == K_LEFT:
            direction = left
        if event.key == K_RIGHT:
            direction = right
        if event.key == K_ESCAPE:
            break

    if direction == up:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direction == left:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if direction == right:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direction == down:
        snake[0] = (snake[0][0], snake[0][1] + 10)


    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()