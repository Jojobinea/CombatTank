from math import *
import keyboard

import Background
from Background import *
import ObstaclesCollisionsPlayer

pygame.init()

border = pygame.image.load("Images/Border.png")
border_x = 10
border_y = 60
borderbig = pygame.transform.scale(border, [1520, 800])

# config.py

pygame.init()
score_p1 = 0
score_p2 = 0

screenInf = pygame.display.Info()
screen_size = [screenInf.current_w, screenInf.current_h]

# Player info
player_1 = pygame.image.load("Images/Player1 - Sprite.png")
player_1_y = screen_size[1] / 2
player_1_x = screen_size[0] + 100 - screen_size[0]
player_1_rect = player_1.get_rect()

player_2 = pygame.image.load("Images/Player2 - Sprite.png")
player_2_y = screen_size[0] / 3.5
player_2_x = screen_size[1] + 500
player_2_rect = player_2.get_rect()

game_clock = pygame.time.Clock()
player_size = 60

# colours
Black = (100, 45, 15)
White = (255, 255, 255)
Red = (162, 8, 0)
Green = (0, 127, 33)
Yellow = (197, 199, 37)
Blue = (0, 0, 255)
screen = pygame.display.set_mode(screen_size)
angle_1 = 1
angle_2 = 1

# Bullet 1
bullet1appear = False
bullet1_y = 0
bullet1_x = 0
bullet1_dy = 7
bullet1_dx = 7
angle_1bullet = 0
bullet1_hit = 0
# Bullet 2
bullet2appear = False
bullet2_y = 0
bullet2_x = 0
bullet2_dy = 7
bullet2_dx = 7
angle_2bullet = 0
bullet2_hit = 0


def move_p1():
    keys = pygame.key.get_pressed()

    if keys:
        global player_1_y, player_1_x, angle_1, player_2_y, player_2_x, angle_2, bullet1appear, bullet2appear, bullet1_x, bullet1_y, bullet2_x, bullet2_y

        if keyboard.is_pressed("w"):
            moveFowardp1 = 1
        else:
            moveFowardp1 = 0
        if keyboard.is_pressed("up"):
            moveFowardp2 = 1
        else:
            moveFowardp2 = 0

        if keys[pygame.K_d] and moveFowardp1 == 0:
            angle_1 += 5 * -1
        if keys[pygame.K_a] and moveFowardp1 == 0:
            angle_1 += 5
        if keys[pygame.K_w] and moveFowardp1 == 1:
            player_1_y -= 5 * cos(radians(angle_1))
            player_1_x -= 5 * sin(radians(angle_1))
        if keys[pygame.K_z] and bullet1appear == False:
            bullet1appear = True
            bullet1_y = player_1_y
            bullet1_x = player_1_x

        if keys[pygame.K_RIGHT] and moveFowardp2 == 0:
            angle_2 += 5 * -1
        if keys[pygame.K_LEFT] and moveFowardp2 == 0:
            angle_2 += 5
        if keys[pygame.K_UP] and moveFowardp2 == 1:
            player_2_y -= 5 * cos(radians(angle_2))
            player_2_x -= 5 * sin(radians(angle_2))
        if keys[pygame.K_m] and bullet2appear == False:
            bullet2_y = player_2_y
            bullet2_x = player_2_x
            bullet2appear = True


# makes sure the player won't go through the border
def limit_borders_up(player1, walls, player2, walls2):
    global player_1_y, player_2_y
    if player1 <= walls:
        player_1_y = walls
    if player2 <= walls2:
        player_2_y = walls2


def limit_borders_down(player1, walls, player2, wall2):
    global player_1_y, player_2_y
    if player1 >= walls:
        player_1_y = walls
    if player2 >= wall2:
        player_2_y = wall2


def limit_borders_left(player1, walls, player2, wall2):
    global player_1_x, player_2_x
    if player1 <= walls:
        player_1_x = walls
    if player2 <= wall2:
        player_2_x = wall2


def limit_borders_right(player1, wall, player2, wall2):
    global player_1_x, player_2_x
    if player1 >= wall:
        player_1_x = wall
    if player2 >= wall2:
        player_2_x = wall2


def bounce1y():
    global bullet1_dx, bullet1_dy, bullet1_hit
    bullet1_dy *= -1
    bullet1_dx *= 1
    bullet1_hit += 1


def bounce1x():
    global bullet1_dx, bullet1_dy, bullet1_hit
    bullet1_dy *= 1
    bullet1_dx *= -1
    bullet1_hit += 1


def bounce2y():
    global bullet2_dx, bullet2_dy, bullet2_hit
    bullet2_dy *= -1
    bullet2_dx *= 1
    bullet2_hit += 1


def bounce2x():
    global bullet2_dx, bullet2_dy, bullet2_hit
    bullet2_dy *= 1
    bullet2_dx *= -1
    bullet2_hit += 1


def limit_borders_upbullet2(player1, walls, player2, walls2):
    global bullet1_y, bullet2_y
    if player1 <= walls:
        bullet1_y = walls
        bounce1y()
    if player2 <= walls2:
        bullet2_y = walls2
        bounce2y()


def limit_borders_downbullet2(player1, walls, player2, wall2):
    global bullet1_y, bullet2_y
    if player1 >= walls:
        bullet1_y = walls
        bounce1y()
    if player2 >= wall2:
        bullet2_y = wall2
        bounce2y()


def limit_borders_leftbullet2(player1, walls, player2, wall2):
    global bullet1_x, bullet2_x
    if player1 <= walls:
        bullet1_x = walls
        bounce1x()
    if player2 <= wall2:
        bullet2_x = wall2
        bounce2x()


def limit_borders_rightbullet2(player1, wall, player2, wall2):
    global bullet1_x, bullet2_x
    if player1 >= wall:
        bullet1_x = wall
        bounce1x()
    if player2 >= wall2:
        bullet2_x = wall2
        bounce2x()


# player 1 score
score_p1_font = pygame.font.SysFont('IMPACT', 50)
score_p1_text = score_p1_font.render('0', True, Green)
score_p1_text_rect = score_p1_text.get_rect()
score_p1_text_rect.center = (300, 30)

# player 2 score
score_p2_font = pygame.font.SysFont('IMPACT', 50)
score_p2_text = score_p2_font.render('0', True, Blue)
score_p2_text_rect = score_p2_text.get_rect()
score_p2_text_rect.center = (1000, 30)

score_1_text = score_p1

run = True

while run:
    screen.fill(Black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    score_space = 70
    border_thickness = 25

    # drawing objects
    Background.draw_background()

    limit_borders_up(player_1_y, score_space + 5, player_2_y, score_space + 5)
    limit_borders_down(player_1_y, 750, player_2_y, 750)
    limit_borders_left(player_1_x, 25, player_2_x, 25)
    limit_borders_right(player_1_x, 1415, player_2_x, 1415)

    move_p1()
    player_1_x, player_1_y = ObstaclesCollisionsPlayer.detect_collision_player(player_1_x, player_1_y)
    player_2_x, player_2_y = ObstaclesCollisionsPlayer.detect_collision_player(player_2_x, player_2_y)

    bullet1_x, bullet1_y = ObstaclesCollisionsPlayer.detect_collision_ball1(bullet1_x, bullet1_y)

    limit_borders_upbullet2(bullet1_y, score_space + 5, bullet2_y, score_space + 5)
    limit_borders_downbullet2(bullet1_y, 750, bullet2_y, 750)
    limit_borders_leftbullet2(bullet1_x, 25, bullet2_x, 25)
    limit_borders_rightbullet2(bullet1_x, 1415, bullet2_x, 1415)

    # show elements on screen
    surf = pygame.transform.rotate(player_1, angle_1)
    surf2 = pygame.transform.rotate(player_2, angle_2)
    screen.blit(surf, (player_1_x, player_1_y))
    screen.blit(surf2, (player_2_x, player_2_y))
    screen.blit(score_p1_text, score_p1_text_rect)
    screen.blit(score_p2_text, score_p2_text_rect)

    center1 = 0
    center2 = 0
    if not bullet1appear:
        angle_1bullet = angle_1
    if bullet1appear:
        if bullet1_hit == 0:
            bullet1_dy = 7
            bullet1_dx = 7
        bullet1_y -= bullet1_dy * cos(radians(angle_1bullet)) * 3
        bullet1_x -= bullet1_dx * sin(radians(angle_1bullet)) * 3
        bullet1 = pygame.Rect(bullet1_x + 40, bullet1_y + 40, 6, 6)
        pygame.draw.rect(screen, White, bullet1)

    # Angle that the green player's bullet must go
    if not bullet2appear:
        angle_2bullet = angle_2
    # Green player's bullet's movement if it is triggered
    if bullet2appear:
        if bullet2_hit == 0:
            bullet2_dy = 7
            bullet2_dx = 7
        bullet2_y -= bullet2_dy * cos(radians(angle_2bullet)) * 3
        bullet2_x -= bullet2_dx * sin(radians(angle_2bullet)) * 3

        bullet2 = pygame.Rect(bullet2_x + 50, bullet2_y + 40, 6, 6)
        pygame.draw.rect(screen, "red", bullet2)

    # Check how many times the "balls" bounced
    if bullet1_hit == 6:
        bullet1appear = False
        bullet1_hit = 0
    if bullet2_hit == 6:
        bullet2appear = False
        bullet2_hit = 0
    # Blue tank bullet collision
    if player_2_x + 80 >= bullet1_x >= player_2_x and player_2_y + 80 >= bullet1_y >= player_2_y or player_2_x - 80 >= bullet1_x >= player_2_x and player_2_y - 80 >= bullet1_y >= player_2_y:
        bullet1_hit = 0
        bullet1_x = player_1_x
        bullet1_y = player_1_x
        bullet1appear = False
        score_p1 += 1
        player2_damaged = pygame.Rect(player_2_x, player_2_y, 120, 120)
        pygame.draw.rect(screen, Red, player2_damaged)
        score_p1_text = score_p1_font.render(f'{score_p1}', True, Green)
    # Green tank bullet collision
    if player_1_x + 80 >= bullet2_x >= player_1_x and player_1_y + 80 >= bullet2_y >= player_1_y or player_1_x - 80 >= bullet2_x >= player_1_x and player_1_y - 80 >= bullet2_y >= player_1_y:
        bullet2_hit = 0
        bullet2_x = player_2_x
        bullet2_y = player_2_y
        bullet2appear = False
        score_p2 += 1
        player1_damaged = pygame.Rect(player_1_x, player_1_y, 120, 120)
        pygame.draw.rect(screen, Red, player1_damaged)

        score_p2_text = score_p1_font.render(f'{score_p2}', True, Blue)

    screen.blit(borderbig, (border_x, border_y))
    game_clock.tick(60)
    Background.drawGroup.draw(screen)
    pygame.display.update()
