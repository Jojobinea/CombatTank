def detect_collision_player(player_x, player_y):
    # Top Border Square
    if 165 >= player_y >= 160 and 780 >= player_x >= 670:
        player_y = 165
    if player_y < 160 and 675 >= player_x >= 665:
        player_x = 665
    if player_y < 160 and 790 >= player_x >= 785:
        player_x = 790

    # Bottom Border Square
    if 670 >= player_y >= 660 and 780 >= player_x >= 670:
        player_y = 660
    if 670 < player_y and 675 >= player_x >= 665:
        player_x = 665
    if 670 < player_y and 790 >= player_x >= 785:
        player_x = 790

    # Top Left Curve
    if 165 >= player_y >= 160 and 640 >= player_x >= 500:
        player_y = 160
    if 315 >= player_y > 160 and 505 >= player_x >= 500:
        player_x = 500
    if 315 >= player_y > 300 and 590 >= player_x >= 500:
        player_y = 315
    if 270 >= player_y > 260 and 650 >= player_x >= 500:
        player_y = 270
    if 315 >= player_y > 160 and 600 >= player_x >= 590:
        player_x = 600
    if 250 >= player_y > 160 and 650 >= player_x >= 640:
        player_x = 650

    # Top right Curve
    if 165 >= player_y >= 160 and 950 >= player_x >= 810:
        player_y = 160
    if 250 >= player_y > 160 and 815 >= player_x >= 810:
        player_x = 810
    if 315 >= player_y > 300 and 950 >= player_x >= 885:
        player_y = 315
    if 270 >= player_y > 260 and 950 >= player_x >= 810:
        player_y = 270
    if 315 >= player_y > 160 and 970 >= player_x >= 960:
        player_x = 970
    if 315 >= player_y > 160 and 900 >= player_x >= 870:
        player_x = 870

    # Bottom Left Corner
    if 485 >= player_y > 480 and 590 >= player_x >= 490:
        player_y = 480
    if 635 >= player_y > 480 and 500 >= player_x >= 485:
        player_x = 485
    if 635 >= player_y >= 630 and 640 >= player_x >= 500:
        player_y = 635
    if 635 >= player_y > 530 and 650 >= player_x >= 640:
        player_x = 650
    if 535 >= player_y >= 530 and 640 >= player_x >= 500:
        player_y = 530
    if 635 >= player_y > 480 and 600 >= player_x >= 590:
        player_x = 600

    # Bottom Right Corner
    if 485 >= player_y > 480 and 950 >= player_x >= 880:
        player_y = 480
    if 635 >= player_y > 480 and 970 >= player_x >= 965:
        player_x = 970
    if 635 >= player_y >= 630 and 950 >= player_x >= 810:
        player_y = 635
    if 635 >= player_y > 480 and 885 >= player_x >= 880:
        player_x = 880
    if 635 >= player_y > 530 and 815 >= player_x >= 810:
        player_x = 810
    if 525 >= player_y >= 520 and 950 >= player_x >= 810:
        player_y = 520

    # Mid-Left Square
    if 485 >= player_y >= 355 and 305 >= player_x >= 300:
        player_x = 300
    if 485 >= player_y >= 355 and 425 >= player_x >= 420:
        player_x = 425
    if 350 >= player_y >= 345 and 425 >= player_x >= 300:
        player_y = 345
    if 490 >= player_y >= 485 and 425 >= player_x >= 300:
        player_y = 490

    # Mid-Right Square
    if 485 >= player_y >= 355 and 1025 <= player_x <= 1030:
        player_x = 1025
    if 485 >= player_y >= 355 and 1155 <= player_x <= 1160:
        player_x = 1160
    if 350 >= player_y >= 345 and 1160 >= player_x >= 1025:
        player_y = 345
    if 490 >= player_y >= 485 and 1160 >= player_x >= 1025:
        player_y = 490

    # Top Wall Left
    if 205 >= player_y >= 110 and 180 <= player_x <= 185:
        player_x = 180
    if 205 >= player_y >= 200 and 180 <= player_x <= 330:
        player_y = 205
    if 205 >= player_y >= 110 and 325 <= player_x <= 330:
        player_x = 330
    if 105 >= player_y >= 100 and 180 <= player_x <= 330:
        player_y = 100

    # Top Wall Right
    if 205 >= player_y >= 110 and 1095 <= player_x <= 1105:
        player_x = 1095
    if 205 >= player_y >= 200 and 1095 <= player_x <= 1250:
        player_y = 205
    if 205 >= player_y >= 110 and 1230 <= player_x <= 1250:
        player_x = 1250
    if 105 >= player_y >= 100 and 1095 <= player_x <= 1250:
        player_y = 100

    # Bottom-Left Wall
    if 735 >= player_y >= 655 and 190 <= player_x <= 200:
        player_x = 190
    if 740 >= player_y >= 735 and 190 <= player_x <= 330:
        player_y = 740
    if 735 >= player_y >= 655 and 340 <= player_x <= 345:
        player_x = 345
    if 640 >= player_y >= 635 and 190 <= player_x <= 330:
        player_y = 635

    # Bottom-Right Wall
    if 735 >= player_y >= 655 and 1095 <= player_x <= 1105:
        player_x = 1095
    if 740 >= player_y >= 735 and 1095 <= player_x <= 1250:
        player_y = 740
    if 735 >= player_y >= 655 and 1230 <= player_x <= 1250:
        player_x = 1250
    if 640 >= player_y >= 635 and 1095 <= player_x <= 1250:
        player_y = 635

    # Left Barrier
    if 250 <= player_y <= 590 and 130 <= player_x <= 135:
        player_x = 130
    if 250 <= player_y <= 590 and 220 <= player_x <= 225:
        player_x = 225
    if 250 <= player_y <= 340 and 70 <= player_x <= 75:
        player_x = 70
    if 500 <= player_y <= 590 and 70 <= player_x <= 75:
        player_x = 70
    if 240 <= player_y <= 245 and 85 <= player_x <= 210:
        player_y = 240
    if 310 <= player_y <= 345 and 85 <= player_x <= 210:
        player_y = 345
    if 595 <= player_y <= 605 and 85 <= player_x <= 210:
        player_y = 605
    if 495 <= player_y <= 500 and 85 <= player_x <= 210:
        player_y = 495

    # Right Barrier
    if 250 <= player_y <= 590 and 1215 <= player_x <= 1220:
        player_x = 1215
    if 250 <= player_y <= 590 and 1320 <= player_x <= 1325:
        player_x = 1325
    if 250 <= player_y <= 340 and 1385 <= player_x <= 1390:
        player_x = 1390
    if 500 <= player_y <= 590 and 1385 <= player_x <= 1390:
        player_x = 1390
    if 235 <= player_y <= 240 and 1215 <= player_x <= 1390:
        player_y = 235
    if 595 <= player_y <= 600 and 1215 <= player_x <= 1390:
        player_y = 600
    if 340 <= player_y <= 345 and 1215 <= player_x <= 1390:
        player_y = 345
    if 495 <= player_y <= 500 and 1215 <= player_x <= 1390:
        player_y = 495

    return player_x, player_y


def detect_collision_ball1(ball_x, ball_y):
    import combat

    # Top Border Square
    if 160 >= ball_y and 780 >= ball_x >= 670:
        combat.bounce1y()
    if ball_y < 160 and 710 >= ball_x >= 700:
        combat.bounce1x()
    if ball_y < 160 and 790 >= ball_x >= 785:
        combat.bounce1x()

    # Bottom Border Square
    if ball_y >= 680 and 780 >= ball_x >= 670:
        combat.bounce1y()
    if 670 < ball_y and 710 >= ball_x >= 700:
        combat.bounce1x()
    if 670 < ball_y and 790 >= ball_x >= 785:
        combat.bounce1x()

    # Top Left Curve
    if ball_y >= 180 and 640 >= ball_x >= 500:
        combat.bounce1y()
    if 315 >= ball_y > 160 and ball_x >= 520:
        combat.bounce1x()
    if 315 >= ball_y > 300 and 590 >= ball_x >= 500:
        combat.bounce1y()
    if 270 >= ball_y > 260 and 650 >= ball_x >= 500:
        combat.bounce1y()
    if 315 >= ball_y > 160 and 600 >= ball_x >= 590:
        combat.bounce1x()
    if 250 >= ball_y > 160 and 650 >= ball_x >= 640:
        combat.bounce1x()

    # Top right Curve
    if 165 >= ball_y >= 160 and 950 >= ball_x >= 810:
        combat.bounce1y()
    if 250 >= ball_y > 160 and 815 >= ball_x >= 810:
        combat.bounce1x()
    if 315 >= ball_y > 300 and 950 >= ball_x >= 885:
        combat.bounce1y()
    if 270 >= ball_y > 260 and 950 >= ball_x >= 810:
        combat.bounce1y()
    if 315 >= ball_y > 160 and 970 >= ball_x >= 960:
        combat.bounce1x()
    if 315 >= ball_y > 160 and 900 >= ball_x >= 870:
        combat.bounce1x()

    # Bottom Left Corner
    if 485 >= ball_y > 480 and 590 >= ball_x >= 490:
        combat.bounce1y()
    if 635 >= ball_y > 480 and 500 >= ball_x >= 485:
        combat.bounce1x()
    if 635 >= ball_y >= 630 and 640 >= ball_x >= 500:
        combat.bounce1y()
    if 635 >= ball_y > 530 and 650 >= ball_x >= 640:
        combat.bounce1x()
    if 535 >= ball_y >= 530 and 640 >= ball_x >= 500:
        combat.bounce1y()
    if 635 >= ball_y > 480 and 600 >= ball_x >= 590:
        combat.bounce1x()

    # Bottom Right Corner
    if 485 >= ball_y > 480 and 950 >= ball_x >= 880:
        combat.bounce1y()
    if 635 >= ball_y > 480 and 970 >= ball_x >= 965:
        combat.bounce1x()
    if 635 >= ball_y >= 630 and 950 >= ball_x >= 810:
        combat.bounce1y()
    if 635 >= ball_y > 480 and 885 >= ball_x >= 880:
        combat.bounce1x()
    if 635 >= ball_y > 530 and 815 >= ball_x >= 810:
        combat.bounce1x()
    if 525 >= ball_y >= 520 and 950 >= ball_x >= 810:
        combat.bounce1y()

    # Mid-Left Square
    if 485 >= ball_y >= 355 and 305 >= ball_x >= 300:
        combat.bounce1x()
    if 485 >= ball_y >= 355 and 425 >= ball_x >= 420:
        combat.bounce1x()
    if 350 >= ball_y >= 345 and 425 >= ball_x >= 300:
        combat.bounce1y()
    if 490 >= ball_y >= 485 and 425 >= ball_x >= 300:
        combat.bounce1y()

    # Mid-Right Square
    if 485 >= ball_y >= 355 and 1025 <= ball_x <= 1030:
        combat.bounce1x()
    if 485 >= ball_y >= 355 and 1155 <= ball_x <= 1160:
        combat.bounce1x()
    if 350 >= ball_y >= 345 and 1160 >= ball_x >= 1025:
        combat.bounce1y()
    if 490 >= ball_y >= 485 and 1160 >= ball_x >= 1025:
        combat.bounce1y()

    # Top Wall Left
    if 205 >= ball_y >= 110 and 180 <= ball_x <= 185:
        combat.bounce1x()
    if 205 >= ball_y >= 200 and 180 <= ball_x <= 330:
        combat.bounce1y()
    if 205 >= ball_y >= 110 and 325 <= ball_x <= 330:
        combat.bounce1x()
    if 105 >= ball_y >= 100 and 180 <= ball_x <= 330:
        combat.bounce1y()

    # Top Wall Right
    if 205 >= ball_y >= 110 and 1095 <= ball_x <= 1105:
        combat.bounce1x()
    if 205 >= ball_y >= 200 and 1095 <= ball_x <= 1250:
        combat.bounce1y()
    if 205 >= ball_y >= 110 and 1230 <= ball_x <= 1250:
        combat.bounce1x()
    if 105 >= ball_y >= 100 and 1095 <= ball_x <= 1250:
        combat.bounce1y()

    # Bottom-Left Wall
    if 735 >= ball_y >= 655 and 190 <= ball_x <= 200:
        combat.bounce1x()
    if 740 >= ball_y >= 735 and 190 <= ball_x <= 330:
        combat.bounce1y()
    if 735 >= ball_y >= 655 and 340 <= ball_x <= 345:
        combat.bounce1x()
    if 640 >= ball_y >= 635 and 190 <= ball_x <= 330:
        combat.bounce1y()

    # Bottom-Right Wall
    if 735 >= ball_y >= 655 and 1095 <= ball_x <= 1105:
        combat.bounce1x()
    if 740 >= ball_y >= 735 and 1095 <= ball_x <= 1250:
        combat.bounce1y()
    if 735 >= ball_y >= 655 and 1230 <= ball_x <= 1250:
        combat.bounce1x()
    if 640 >= ball_y >= 635 and 1095 <= ball_x <= 1250:
        combat.bounce1y()

    # Left Barrier
    if 250 <= ball_y <= 590 and 130 <= ball_x <= 135:
        combat.bounce1x()
    if 250 <= ball_y <= 590 and 220 <= ball_x <= 225:
        combat.bounce1x()
    if 250 <= ball_y <= 340 and 70 <= ball_x <= 75:
        combat.bounce1x()
    if 500 <= ball_y <= 590 and 70 <= ball_x <= 75:
        combat.bounce1x()
    if 240 <= ball_y <= 245 and 85 <= ball_x <= 210:
        combat.bounce1y()
    if 310 <= ball_y <= 345 and 85 <= ball_x <= 210:
        combat.bounce1y()
    if 595 <= ball_y <= 605 and 85 <= ball_x <= 210:
        combat.bounce1y()
    if 495 <= ball_y <= 500 and 85 <= ball_x <= 210:
        combat.bounce1y()

    # Right Barrier
    if 250 <= ball_y <= 590 and 1215 <= ball_x <= 1220:
        combat.bounce1x()
    if 250 <= ball_y <= 590 and 1320 <= ball_x <= 1325:
        combat.bounce1x()
    if 250 <= ball_y <= 340 and 1385 <= ball_x <= 1390:
        combat.bounce1x()
    if 500 <= ball_y <= 590 and 1385 <= ball_x <= 1390:
        combat.bounce1x()
    if 235 <= ball_y <= 240 and 1215 <= ball_x <= 1390:
        combat.bounce1y()
    if 595 <= ball_y <= 600 and 1215 <= ball_x <= 1390:
        combat.bounce1y()
    if 340 <= ball_y <= 345 and 1215 <= ball_x <= 1390:
        combat.bounce1y()
    if 495 <= ball_y <= 500 and 1215 <= ball_x <= 1390:
        combat.bounce1y()

    return ball_x, ball_y
