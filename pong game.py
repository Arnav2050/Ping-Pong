import pygame
import math
import random
import time
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ping Pong")
mixer.music.load('bg.wav')
mixer.music.play(-1)

batImg = pygame.image.load('line1.png')
batX = 740
batY = 300
batY_change = 0
bat_score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 600
textY = 10

lbatImg = pygame.image.load('line1.png')
lbatX = 0
lbatY = 300
lbatY_change = 0
lbat_score = 0
font1 = pygame.font.Font('freesansbold.ttf', 32)
textX1 = 10
textY1 = 10

ballImg = pygame.image.load('ball.png')
ballX = 400
ballY = 300
ballX_change = 1
ballY_change = 0


def show_score1(x, y):
    score = font.render("Player A:" + str(bat_score), True, (0, 0, 0))
    screen.blit(score, (x, y))


def show_score2(x, y):
    score = font1.render("Player B:" + str(lbat_score), True, (0, 0, 0))
    screen.blit(score, (x, y))


def bat(x, y):
    screen.blit(batImg, (x, y))


def lbat(x, y):
    screen.blit(lbatImg, (x, y))


def ball(x, y):
    screen.blit(ballImg, (x, y))


def collision(batX, batY, ballX, ballY):
    distance = math.sqrt((math.pow(batX - ballX, 2)) + (math.pow(batY - ballY, 2)))
    if distance < 40:
        return True
    else:
        return False


def collision1(lbatX, lbatY, ballX, ballY):
    distance = math.sqrt((math.pow(lbatX - ballX, 2)) + (math.pow(lbatY - ballY, 2)))
    if distance < 40:
        return True
    else:
        return False


running = True
while running:
    screen.fill((220, 220, 220))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # player1
            if event.key == pygame.K_UP:
                batY_change = -0.5
            if event.key == pygame.K_DOWN:
                batY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                batY_change = 0
            # player2
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                lbatY_change = -0.5
            if event.key == pygame.K_s:
                lbatY_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                lbatY_change = 0

    a = random.uniform(0.1, 0.2)
    b = random.randint(1, 2)
    if b == 1:
        b = a
    if b == 2:
        b = -a
    iscollision = collision(batX, batY, ballX, ballY)
    if iscollision:
        ballX_change = -1
        ballY_change = b
    iscollision1 = collision1(lbatX, lbatY, ballX, ballY)
    if iscollision1:
        ballX_change = 1
        ballY_change = b
    if ballY >= 550:
        ballY_change = -1
    elif ballY <= 0:
        ballY_change = 1
    if ballX >= 780:
        lbat_score += 1
        ballY = 400
        ballX = 300
        ballX_change = -1
        batY = 300
        lbatY = 300
        time.sleep(1)

    if ballX <= 0:
        bat_score += 1
        ballX = 300
        ballY = 300
        batY = 300
        lbatY = 300
        ballX_change = 1
        time.sleep(1)
    
    show_score1(textX, textY)
    show_score2(textX1, textY1)
    ballX += ballX_change
    ballY += ballY_change
    batY += batY_change
    lbatY += lbatY_change
    bat(batX, batY)
    lbat(lbatX, lbatY)
    ball(ballX, ballY)
    pygame.display.update()
