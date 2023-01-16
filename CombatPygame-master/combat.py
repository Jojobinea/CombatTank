import pygame
from math import *
import keyboard
import Background
import ObstaclesCollisions

pygame.init()

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
player_2_x = screen_size[1] + 300
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
angle_2 = 1.2


def move_p1():

    keys = pygame.key.get_pressed()

    if keys:
        global player_1_y, player_1_x, angle_1, player_2_y, player_2_x, angle_2

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

        if keys[pygame.K_RIGHT] and moveFowardp2 == 0:
            angle_2 += 5 * -1
        if keys[pygame.K_LEFT] and moveFowardp2 == 0:
            angle_2 += 5
        if keys[pygame.K_UP] and moveFowardp2 == 1:
            player_2_y -= 5 * cos(radians(angle_2))
            player_2_x -= 5 * sin(radians(angle_2))


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


# player 1 ball
# ball_p1 = pygame.image.load("Player1 - Sprite.png")
# ball_size = (5, 5)
# ball_p1 = pygame.transform.scale(ball_p1, ball_size)
# ball_p1_x = 50
# ball_p1_y = 150
# ball_p1_dx = 1
# ball_p1_dy = 1

# player 2 ball
# ball_p2 = pygame.draw.circle()
# ball_size = (5, 5)
# ball_p2 = pygame.transform.scale(ball_p2, ball_size)
# ball_p2_x = 50
# ball_p2_y = 150
# ball_p2_dx = 1
# ball_p2_dy = 1

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
    ObstaclesCollisions.detect_collision_players()

    # show elements on screen
    surf = pygame.transform.rotate(player_1, angle_1)
    surf2 = pygame.transform.rotate(player_2, angle_2)
    screen.blit(surf, (player_1_x, player_1_y))
    screen.blit(surf2, (player_2_x, player_2_y))
    screen.blit(score_p1_text, score_p1_text_rect)
    screen.blit(score_p2_text, score_p2_text_rect)
    # screen.blit(ball_p1, (ball_p1_x, ball_p1_y))
    # screen.blit(ball_p2, (ball_p2_x, ball_p2_y))

    game_clock.tick(60)
    Background.drawGroup.draw(screen)
    pygame.display.update()
