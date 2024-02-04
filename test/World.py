# import sys
# sys.path.insert(1, 'src')
# import engine
import pygame

state = 0
prevQ = False

def World_Script(world):
    global state, prevQ
    # print(123,end="\r")
    if world.IsPressing(pygame.K_q) == True and prevQ == False:
        if state == 0:
            world.backgroundColor = (255,255,255)
            state = 1
        elif state == 1:
            world.backgroundColor = (0,0,0)
            state = 0
        prevQ = True
    elif world.IsPressing(pygame.K_q) == False and prevQ == True:
        prevQ = False
