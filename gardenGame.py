import pygame
import sys
import random
pygame.init()
width = 800
height = 800
skyC = (100,155,255)
red = (255,0,0)
green = (20,255,20)
pink = (255,120,120)
brown = (120,80,0)
yellow = (255,255,0)
timer = 0
ticks = [9000,3000,27000]
tickChosen = 0
Spielstand = True
while Spielstand:
    pygame.time.wait(20)
    timer += 1
    for event in pygame.event.get():
        mpos = pygame.mouse.get_pos()
        mpos1 = mpos[0]
        mpos2 = mpos[1]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    if timer == 50:
        timer -= 50
    