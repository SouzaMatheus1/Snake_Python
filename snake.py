import random
import pygame
import os
from pygame.locals import *

def onGridRandom():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def feed(cel1, cel2):
    return (cel1[0] == cel2[0]) and (cel1[1] == cel2[1])

def collisionSnake(c1):
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            return True

def collisionWall(c1):
    if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
        return True

def showGameOver():
    # Game over
    game_over_message = "GAME OVER!"
    game_over_format = font.render(game_over_message, False, (255,255,255))
    screen.blit(game_over_format, ((300 - 70),(300 - 30)))

    # Exit button
    pygame.draw.rect(screen, (255,255,255), (button_position, (70, 30)))
    screen.blit(button_text, (button_position[0] + 10, button_position[1] + 8))
    
    pygame.display.flip()

up = 0
right = 1
left = 2
down = 3
direction = left
game_over = False
score = 0

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
apple_pos = onGridRandom()

clock = pygame.time.Clock()
tick = 10

# Score font
font = pygame.font.SysFont("hack", 30, True, False)

# Exit button
button_text = font.render("Exit!", True, (0,0,0))
button_position = ((600 - 70) // 2, (600) // 2)

# Background
dir_path = os.path.dirname(os.path.realpath(__file__))
bg = pygame.image.load(os.path.join(dir_path, 'Images', 'bg.jpg'))

# Sounds
# sound = pygame.sound.load(os.path.join(dir_path, 'Sounds', 'eat.mp3'))

while True:
    screen.blit(bg, (0,0))
    clock.tick(tick)

    message = f'Score: {score}'
    text_format = font.render(message, False, (255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            if button_position[0] < x < button_position[0] + (600 - 70) // 2 and \
                    button_position[1] < y < button_position[1] + (600) // 2:
                pygame.quit()
                exit()

    if game_over:
        showGameOver()
        continue

    if feed(snake[0], apple_pos):
        apple_pos = onGridRandom()
        snake.append((0,0))
        tick += 1
        score += 1

    if collisionSnake(snake):
        game_over = collisionSnake(snake)
        
    if collisionWall(snake):
        game_over = True

    if event.type == MOUSEBUTTONDOWN:
        x,y = event.pos
        if button_position[0] < x < button_position[0] + (600 - 70) // 2 and \
            button_position[1] < y < button_position[1] + (600) // 2:
            pygame.quit()
            exit()
    
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


    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_skin, pos)
    
    screen.blit(text_format, (10, 10))

    pygame.display.update()