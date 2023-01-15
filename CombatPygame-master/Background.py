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

def draw_objects(obj, w, h, x_pos, y_pos, data, rot,ang):
    obj.image = pygame.image.load(data)
    obj.image = pygame.transform.scale(obj.image, [w, h])
    obj.rect = pygame.Rect(x_pos, y_pos, 0, 0)
    if rot == 1:
        obj.image = pygame.transform.rotate(obj.image, ang)

