import pygame
import Background


def detect_collision_players():
    import combat

    # Top Border Square
    if 165 >= combat.player_1_y >= 160 and 780 >= combat.player_1_x >= 670:
        combat.player_1_y = 165
    if combat.player_1_y < 160 and 675 >= combat.player_1_x >= 665:
        combat.player_1_x = 665
    if combat.player_1_y < 160 and 790 >= combat.player_1_x >= 785:
        combat.player_1_x = 790

    if 165 >= combat.player_2_y >= 160 and 780 >= combat.player_2_x >= 670:
        combat.player_2_y = 165
    if combat.player_2_y < 160 and 675 >= combat.player_2_x >= 665:
        combat.player_2_x = 665
    if combat.player_2_y < 160 and 790 >= combat.player_2_x >= 785:
        combat.player_2_x = 790