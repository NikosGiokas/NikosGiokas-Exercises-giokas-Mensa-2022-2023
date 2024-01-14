import pygame
import sys
pygame.init()
width = 350
height = 350
seedGen = False
skyC = (47,155,255)
red = (255,0,0)
green = (20,255,20)
pink = (255,120,120)
brown = (120,80,0)
yellow = (255,255,0)
seeds = 0
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("plant clicker")
timer = 0
shopcounter = [0,0,0]
shopprice = [15,100,1500]
#shopSPS= [0.1,1,10]
totalSPS = 0
font = pygame.font.Font(pygame.font.get_default_font(), 10)
fontBig = pygame.font.Font(pygame.font.get_default_font(), 20)

pygame.display.flip()

Spielstand = True
sliderX = [4,94,184,289]
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
        seeds += totalSPS
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 60 and mpos1 < 160 and mpos2 > 100 and mpos2 < 280:
        seedGen = True
    if event.type == pygame.MOUSEBUTTONUP and mpos1 > 60 and mpos1 < 160 and mpos2 > 100 and mpos2 < 280 and seedGen:
        seeds += 1
        seedGen = False
        print(seeds)
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > sliderX[0] and mpos1 < sliderX[1] and mpos2 > 294 and mpos2 < 329 and seeds > shopprice[0]:
        totalSPS += 1
        seeds-=shopprice[0]
        shopprice[0]+=5
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > sliderX[1] and mpos1 < sliderX[2] and mpos2 > 294 and mpos2 < 329 and seeds > shopprice[1]:
        totalSPS += 10
        seeds-=shopprice[1]
        shopprice[1]+=33
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > sliderX[2] and mpos1 < sliderX[3] and mpos2 > 294 and mpos2 < 329 and seeds > shopprice[2]:
        totalSPS += 100
        seeds-=shopprice[2]
        shopprice[2]+=500
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 30 and mpos1 < 40 and mpos2 > 260 and mpos2 < 280:
        sliderX[0]-=2
        sliderX[1]-=2
        sliderX[2]-=2
        sliderX[3]-=2
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 300 and mpos1 < 310 and mpos2 > 260 and mpos2 < 280:
        sliderX[0]+=2
        sliderX[1]+=2
        sliderX[2]+=2
        sliderX[3]+=2
    text_surface = fontBig.render(str(seeds)+" seeds", True, (0, 255, 0))
    
    plantHitbox = pygame.draw.rect(screen,skyC,(60,100,100,180))
    plantBackground = pygame.draw.rect(screen,skyC,(0,0,400,400))
    dirt = pygame.draw.rect(screen,brown,(0,250,400,40))
    stem = pygame.draw.rect(screen,green,(100,150,20,100))
    leaf1 = pygame.draw.rect(screen,green,(60,194,40,30))
    leaf2 = pygame.draw.rect(screen,green,(120,184,40,30))
    flower = pygame.draw.rect(screen,pink,(90,124,40,30))
    flower2 = pygame.draw.rect(screen,pink,(100,144,20,25))
    pollen = pygame.draw.rect(screen,yellow,(104,124,12,15))
    sliderfront = pygame.draw.polygon(screen,yellow,((310,270),(300,280),(300,260)),3)
    sliderback = pygame.draw.polygon(screen,yellow,((30,270),(40,280),(40,260)),3)
    text_tutorial = font.render("Welcome to plant clicker! Click the flower to get seeds, and click the",True,(0,0,0))
    text_tutorial2 = font.render("buttons down below to buy items ( or people ) that help you gather ",True,(0,0,0))
    text_tutorial3 = font.render("seeds. More updates are coming! Have fun playing Plant Clicker! ",True,(0,0,0))
    buttonSClip = pygame.draw.rect(screen,green,(sliderX[0],294,90,45))
    text_clip = font.render("clipper ", True, (0, 0, 0))
    text_clip_price = font.render("sps: 1 prc: "+str(shopprice[0]), True, (0, 0, 0))
    screen.blit(text_clip, dest=(sliderX[0]+2,300))
    screen.blit(text_clip_price, dest=(sliderX[0]+2,320))
    buttonSgardener = pygame.draw.rect(screen,green,(sliderX[1]+5,294,90,45,))
    text_grdr = font.render("gardener", True, (0, 0, 0))
    text_grdr_price = font.render("sps: 10 prc:"+str(shopprice[1]), True, (0, 0, 0))
    screen.blit(text_grdr, dest=(sliderX[1]+7,300))
    screen.blit(text_grdr_price, dest=(sliderX[1]+7,320))
    buttonSgarden = pygame.draw.rect(screen,green,(sliderX[2]+9,294,100,45))
    text_grd = font.render("garden", True, (0, 0, 0))
    text_grd_prc = font.render("sps: 100 prc: "+str(shopprice[2]), True, (0, 0, 0))

    text_totalSPS = font.render(str(totalSPS)+" SPS",True,(255,200,0))
    screen.blit(text_tutorial,dest=(3,3))
    screen.blit(text_tutorial2,dest=(3,13))
    screen.blit(text_tutorial3,dest=(3,23))
    screen.blit(text_totalSPS,dest=(300,220))
    screen.blit(text_grd, dest=(sliderX[2]+11,300))
    screen.blit(text_grd_prc,dest=(sliderX[2]+11,320))
    screen.blit(text_surface, dest=(60,60))
    round(seeds,1)
    pygame.display.flip()        
