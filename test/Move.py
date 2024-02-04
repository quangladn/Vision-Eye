import pygame

# For Graphic Move 
def Script(world, graphic):
    speed = 5
    if world.IsPressing(pygame.K_a) == True:
        graphic.x -= speed
    if world.IsPressing(pygame.K_d) == True:
        graphic.x += speed
    if world.IsPressing(pygame.K_w) == True:
        graphic.y -= speed
    if world.IsPressing(pygame.K_s) == True:
        graphic.y += speed

    # global state, prevQ
    # print(123,end="\r")
    # elif world.IsPressing(pygame.K_q) == False and prevQ == True:
    #     prevQ = False