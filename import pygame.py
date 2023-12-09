import pygame
from BOX import Box

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Bouncing Square")

#RBG
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (140,0,120)
RED = (255,0,0)
GREEN = (0,0,255)
BLUE = (0,255,0)

boxSize = 50
x=screen.get_width()/2-boxSize/2
y=screen.get_height()/2-boxSize/2
x_vel = 1
y_vel = 2

myBox = Box(boxSize,x,y,PURPLE,x_vel,y_vel)
sbox = Box(25,100,200,RED,2,3)

done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    myBox.move(screen)
    sbox.move(screen)  

    screen.fill(BLACK)

    myBox.draw(screen)
    sbox.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit() 
