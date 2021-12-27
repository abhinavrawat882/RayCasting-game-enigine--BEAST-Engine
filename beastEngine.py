from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
import pygame
import numpy as np
import matplotlib.pyplot as plt
import math
import GameEnigneLib.AngleCal as ac
import GameEnigneLib.renderingFunctions as rf
rd = 0.0174533

pov = 100
plx = 12  # player position in x
ply = 7  # player position in y
pla = 0  # player view angle

MapSize = [16, 16]

# Import and initialize the pygame library
pygame.init()
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards

mp = [[1, 1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 1, 1., 1],
      [1, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 1],
      [1, 0., 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 1],
      [1, 1., 1., 1., 1., 1., 0., 0., 1., 0., 0., 1., 0., 0., 0., 1],
      [1, 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 0., 0., 1],
      [1, 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 1., 1., 1., 0., 1],
      [1, 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1],
      [1, 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1],
      [1, 0., 1., 0., 0., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0., 1],
      [1, 0., 1., 1., 1., 1., 0., 1., 0., 0., 0., 0., 0., 0., 0, 1],
      [1, 0., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 1],
      [1, 1., 0., 0., 0., 0., 0., 1., 0., 0., 1., 0., 0., 0., 0., 1],
      [1, 1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 0, 0., 1],
      [1, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1],
      [1, 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 1],
      [1, 1., 1., 1., 1., 1., 1., 1., 1., 1, 1., 1., 1., 1, 1., 1]]
mp2=[[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]
#plt.imshow(mp)
#plt.show()

def update(pressed_keys, x, y, a):

    if pressed_keys[K_UP]:

        x += 0.06*math.cos(a*rd)
        y += 0.06*math.sin(a*rd)
    if pressed_keys[K_DOWN]:
        x -= 0.06*math.cos(a*rd)
        y -= 0.06*math.sin(a*rd)
    if pressed_keys[K_LEFT]:
        a += 3
    if pressed_keys[K_RIGHT]:
        a -= 3
    a = ac.giveAbsAngle(a)
    # print(a)
    return(x, y, a)
# Simple pygame program


screen = pygame.display.set_mode([480*2, 480])


########################################
# .          GAME LOOP
#########################################
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ########################################
    # .          CLICK EVENT HANDLER
    #########################################
    pressed_keys = pygame.key.get_pressed()
    # print(pressed_keys)
    plx, ply, pla = update(pressed_keys, plx, ply, pla)
    ########################################
    # .          DRAW ON SCREEN
    #########################################
    #print("ANGLE :",pla)
    # the background with white
    screen.fill((0, 0, 0))
    #ln,inter,xe,ye = rf.lineTracer(plx, ply, pla, mp)
    
    rf.d2renderer(screen, plx, ply, pla, pygame, mp)
    rf.threDRenderer(plx, ply, pla, screen, mp, pygame)
    
    #break
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
