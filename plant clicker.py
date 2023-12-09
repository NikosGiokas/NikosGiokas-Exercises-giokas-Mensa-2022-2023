from pygame import pygame
pygame.init()
width = 350
height = 350

skyC = (47,155,255)
red = (255,0,0)
green = (20,255,20)
pink = (255,120,120)
brown = (120,80,0)
yellow = (255,255,0)
seeds = 0
screen = pygame.display.set_mode((width,height))

shopcounter = [0,0,0]
shopnames = ["klipper","gardener","garden"]
shopprice = [10,100,1500]
shopSPS= [0.1,1,10]
font = pygame.font.Font(pygame.font.get_default_font(), 20)


pygame.display.flip()

Spielstand = True

while Spielstand:
    for event in pygame.event.get():
        mpos = pygame.mouse.get_pos()
        mpos1 = mpos[0]
        mpos2 = mpos[1]

    if event.type == pygame.MOUSEBUTTONUP and mpos1 > 60 and mpos1 < 160 and mpos2 > 100 and mpos2 < 280:
        seeds += 1

 
        print(seeds)
        text_surface = font.render(str(seeds)+" seeds", True, (0, 0, 0))
        screen.blit(text_surface, dest=(60,60))
        pygame.display.flip()
        plantHitbox = pygame.draw.rect(screen,skyC,(60,100,100,180))
        plantBackground = pygame.draw.rect(screen,skyC,(0,0,400,400))
        dirt = pygame.draw.rect(screen,brown,(0,250,400,40))
        stem = pygame.draw.rect(screen,green,(100,150,20,100))
        leaf1 = pygame.draw.rect(screen,green,(60,194,40,30))
        leaf2 = pygame.draw.rect(screen,green,(120,184,40,30))
        flower = pygame.draw.rect(screen,pink,(90,124,40,30))
        flower2 = pygame.draw.rect(screen,pink,(100,144,20,25))
        pollen = pygame.draw.rect(screen,yellow,(104,124,12,15))
        buttonSClip = pygame.draw.rect(screen,yellow,(4,294,45,45))
        text_clip = font.render("clip", True, (0, 0, 0))
        screen.blit(text_clip, dest=(9,300))
        buttonSgardener = pygame.draw.rect(screen,yellow,(54,294,45,45))
        text_grdr = font.render("grdr", True, (0, 0, 0))
        screen.blit(text_grdr, dest=(56,300))
        buttonSgarden = pygame.draw.rect(screen,yellow,(104,294,45,45))
        text_grd = font.render("grd", True, (0, 0, 0))
        screen.blit(text_grd, dest=(110,300))
pygame.time.wait(10)