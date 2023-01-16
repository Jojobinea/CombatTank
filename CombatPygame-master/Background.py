import pygame

# Drawing the objects
drawGroup = pygame.sprite.Group()

border = pygame.sprite.Sprite(drawGroup)
borderDetail1 = pygame.sprite.Sprite(drawGroup)
borderDetail2 = pygame.sprite.Sprite(drawGroup)

obsMidCorner1 = pygame.sprite.Sprite(drawGroup)
obsMidCorner2 = pygame.sprite.Sprite(drawGroup)
obsMidCorner3 = pygame.sprite.Sprite(drawGroup)
obsMidCorner4 = pygame.sprite.Sprite(drawGroup)

sideBarrier1 = pygame.sprite.Sprite(drawGroup)
sideBarrier2 = pygame.sprite.Sprite(drawGroup)

sideCube1 = pygame.sprite.Sprite(drawGroup)
sideCube2 = pygame.sprite.Sprite(drawGroup)

sideWallLeft1 = pygame.sprite.Sprite(drawGroup)
sideWallLeft2 = pygame.sprite.Sprite(drawGroup)
sideWallRight1 = pygame.sprite.Sprite(drawGroup)
sideWallRight2 = pygame.sprite.Sprite(drawGroup)


def draw_objects(obj, w, h, x_pos, y_pos, data, ang):
    obj.image = pygame.image.load(data)
    obj.image = pygame.transform.scale(obj.image, [w, h])
    obj.rect = pygame.Rect(x_pos, y_pos, w, h)
    obj.image = pygame.transform.rotate(obj.image, ang)


def draw_background():
    draw_objects(border, 1520, 800, 10, 60, "Images/Border.png", 0)
    draw_objects(borderDetail1, 50, 100, 750, 78, "Images/Obstacle_side_cube.png", 0)
    draw_objects(borderDetail2, 50, 100, 750, 740, "Images/Obstacle_side_cube.png", 0)

    draw_objects(obsMidCorner1, 100, 100, 570, 240, "Images/Obstacle_mid_corner.png", 180)
    draw_objects(obsMidCorner2, 100, 100, 890, 240, "Images/Obstacle_mid_corner_flip.png", 180)
    draw_objects(obsMidCorner3, 100, 100, 570, 550, "Images/Obstacle_mid_corner_flip.png", 0)
    draw_objects(obsMidCorner4, 100, 100, 890, 550, "Images/Obstacle_mid_corner.png", 0)

    draw_objects(sideBarrier1, 100, 300, 150, 320, "Images/Obstacle_side_barrier.png", 0)
    draw_objects(sideBarrier2, 100, 300, 1300, 320, "Images/Obstacle_side_barrier.png", 180)

    draw_objects(sideCube1, 60, 70, 380, 430, "Images/Obstacle_side_cube.png", 0)
    draw_objects(sideCube2, 60, 70, 1110, 430, "Images/Obstacle_side_cube.png", 0)

    draw_objects(sideWallLeft1, 90, 40, 270, 180, "Images/Obstacle_side_cube.png", 0)
    draw_objects(sideWallRight1, 90, 40, 1180, 180, "Images/Obstacle_side_cube.png", 0)
    draw_objects(sideWallLeft2, 90, 40, 270, 720, "Images/Obstacle_side_cube.png", 0)
    draw_objects(sideWallRight2, 90, 40, 1180, 720, "Images/Obstacle_side_cube.png", 0)