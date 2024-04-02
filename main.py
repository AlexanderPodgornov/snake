# писал в 2019 (5 лет назад)

import pygame
import random
import time
pygame.init()
lensnake = 1
key_w = 0
key_a = 0
key_s = 0
key_d = 0
width = 25  # ширина
height = 25  # высота
sizex = 600
sizey = 600
ax = []
ay = []
Score = 0
Time = 0
window = pygame.display.set_mode((sizex, sizey))
pygame.display.set_caption('game')
run = True
for i in range(160, 560):
    if (i - 10) % width == 0:
        ax.append(i)
for i in range(11, 560):
    if (i - 10) % height == 0:
        ay.append(i)
# print(ax)
# print(ay)
font = pygame.font.SysFont('название шрифта', 32)
text_score = font.render('СЧЕТ:', True, (0, 255, 255))
text_time = font.render('ВРЕМЯ:', True, (0, 255, 255))
xx = 10 + 14 * width
yy = 10 + 11 * height
game_speed = 50
yyy = []
xxx = []
yyy1 = []
xxx1 = []
Game_Over = 0
Game_over = 0
go = 0
time = 0


def creating_field():
    for i in range(1, sizex):
        for j in range(1, sizey):
            if j % 2 == 0:
                if i % 2 == 0:
                    color = "white"
                if i % 2 == 1:
                    color = "lightblue"
            if j % 2 == 1:
                if i % 2 == 1:
                    color = "white"
                if i % 2 == 0:
                    color = "lightblue"
            if 5 < i < 23 and 0 < j < 22:
                pygame.draw.rect(window, color, (10 + i * width, 10 + j * height, width, height))
    return pygame.draw.rect(window, color, (10 + i * width, 10 + j * height, width, height))


ranx = random.choice(ax)
rany = random.choice(ay)
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if not go:
        Time = pygame.time.get_ticks()
        TIME = font.render(str(Time)[:len(str(Time)) - 3], True, (255, 255, 255))
        SCORE = font.render(str(Score), True, (255, 255, 255))
    pygame.time.delay(game_speed)
    window.fill('limegreen')
    creating_field()  # функция
    pygame.draw.rect(window, "blue", (xx, yy, width, height))
    ranx1 = ranx
    rany1 = rany
    keys = pygame.key.get_pressed()
    if not key_s:
        if keys[pygame.K_w]:
            key_w = True
            key_a = False
            key_d = False
            key_s = False
    if not key_a:
        if keys[pygame.K_d]:
            key_d = True
            key_a = False
            key_w = False
            key_s = False
    if not key_d:
        if keys[pygame.K_a]:
            key_a = True
            key_w = False
            key_d = False
            key_s = False
    if not key_w:
        if keys[pygame.K_s]:
            key_s = True
            key_a = False
            key_d = False
            key_w = False
    if key_w:
        yy = yy - height
    if key_s:
        yy = yy + height
    if key_a:
        xx = xx - width
    if key_d:
        xx = xx + width
    if yy <= 10:
        yy = 535
    if yy >= 560:
        yy = 35
    if xx >= 575:
        xx = 160
    if xx <= 145:
        xx = 560
    pygame.draw.rect(window, 'red', (ranx, rany, width, height))
    yyy.append(yy)
    xxx.append(xx)
    if ranx == xx and rany == yy:
        Score += 1
        ranx = random.choice(ax)
        rany = random.choice(ay)
        lensnake += 1
    if len(xxx) > lensnake:
        del xxx[len(xxx) - lensnake - 1]
    if len(yyy) > lensnake:
        del yyy[len(yyy) - lensnake - 1]
    yyy1 = yyy[1:]
    xxx1 = xxx[1:]
    for i in range(600):
        if lensnake > 1 and i < lensnake:
            pygame.draw.rect(window, "blue", (xxx[lensnake - i - 1], yyy[lensnake - i - 1], width, height))
        if lensnake > 1 and 5 <= i < lensnake:
            if xxx[-1] == xxx[lensnake - i - 1] and yyy[-1] == yyy[lensnake - i - 1]:
                Game_Over = 1
                break  # выходим из цикла, если игра окончена
    if Game_Over == 1:
        go = True
    if go:
        window.fill("midnight blue")
        text_score = font.render('СЧЕТ:', True, (255, 0, 0))
        text_time = font.render('ВРЕМЯ:', True, (255, 0, 0))
        sec = font.render('сек.', True, (255, 0, 0))
        Game_over = font.render('ИГРА ОКОНЧЕНА', True, (255, 0, 0))
        TIME = font.render(str(Time)[:len(str(Time)) - 3], True, (255, 0, 0))
        SCORE = font.render(str(Score), True, (255, 0, 0))
        window.blit(Game_over, (240, 250))
        window.blit(text_score, (240, 300))
        window.blit(text_time, (240, 350))
        window.blit(SCORE, (320, 300))
        window.blit(TIME, (350, 350))
        window.blit(sec, (400, 350))
    if not go:
        pygame.display.update()
        window.blit(text_score, (20, 20))
        window.blit(text_time, (20, 200))
        window.blit(SCORE, (20, 50))
        window.blit(TIME, (20, 230))
    pygame.display.update()
pygame.quit()
