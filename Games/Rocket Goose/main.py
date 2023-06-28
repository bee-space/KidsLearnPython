import random
import os

import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

HEIGHT = 800
WIDTH = 1200

FONT = pygame.font.SysFont('Verdana', 20)

COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_GREEN = (0, 255, 0)

main_display = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.transform.scale(pygame.image.load("Games/Rocket Goose/background.png"), (WIDTH, HEIGHT))
bg_x1 = 0 
bg_x2 = bg.get_width()
bg_move = 3

IMAGE_PASS = "Games/Rocket Goose/Goose"
PLAYER_IMAGES = os.listdir(IMAGE_PASS)

player_size = (20,20)
player = pygame.image.load('Games/Rocket Goose/player.png').convert_alpha()
player_rect = player.get_rect()
player_move_down = [0, 1]
player_move_right = [1, 0]
player_move_up = [0, -1]
player_move_left = [-1, 0]


def create_enemy():
    enemy_size = (30, 30)
    enemy = pygame.image.load('Games/Rocket Goose/enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]

def create_gift():
    gift_size = (25, 25)
    gift = pygame.image.load('Games/Rocket Goose/bonus.png').convert_alpha()
    gift_rect = pygame.Rect(random.randint(0, WIDTH), 0, *gift_size)
    gift_move = [0, random.randint(1, 6)]
    return [gift, gift_rect, gift_move]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
CREATE_GIFT = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_GIFT, 2500)
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 200)

enemies = []
gifts = []

score = 0

image_index = 0

playing = True

while playing:
    FPS.tick(120)

    for event in pygame.event.get():
        if event.type == QUIT:
            playing = False
        if event.type == CREATE_ENEMY:
           enemies.append(create_enemy())
        if event.type == CREATE_GIFT:
           gifts.append(create_gift())  
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PASS, PLAYER_IMAGES[image_index]))   
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    bg_x1 -= bg_move
    bg_x2 -= bg_move

    if bg_x1 < -bg.get_width():
        bg_x1 = bg.get_width()

    if bg_x2 < -bg.get_width():
        bg_x2 = bg.get_width()

    main_display.blit(bg, (bg_x1, 0))
    main_display.blit(bg, (bg_x2, 0))

    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(player_move_down)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(player_move_right)

    if keys[K_UP] and player_rect.top >= 0:
        player_rect = player_rect.move(player_move_up)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(player_move_left)


    for enemy in enemies:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            playing = False


    for gift in gifts:
        gift[1] = gift[1].move(gift[2])
        main_display.blit(gift[0], gift[1])

        if player_rect.colliderect(gift[1]):
           score += 1
           gifts.pop(gifts.index(gift))


    main_display.blit(player, player_rect)
    main_display.blit(FONT.render(str(score), True, COLOR_BLACK), (WIDTH-50, 20))

    pygame.display.flip()

    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

    for gift in gifts:
        if gift[1].bottom > HEIGHT:
            gifts.pop(gifts.index(gift))

if pygame.event.get():
    if event.type == QUIT:
        quit;



