import pygame
import sys
import random
from AchievementPL import Achievement
pygame.init()
width = 800
height = 800
seedGen = False
skyC = (100,155,255)
red = (255,0,0)
green = (20,255,20)
pink = (255,120,120)
brown = (120,80,0)
yellow = (255,255,0)
black = (0,0,0)
bugColor = brown
seeds = 0
totalSPS = 0
sliderY = [4,69,134,199,0]
change=0
changed=False
#a_ = Achievement()

a_seed1 = Achievement("a seedy place"," get ur 1st seed!",[seeds,0,False,"s"],400,100+sliderY[4],False)
a_seed2 = Achievement("making seeds"," make 1000 cookies",[seeds,999,False,"s"],400,155+sliderY[4],False)
a_seed3 = Achievement("a lot of seeds"," make 100k cookies",[seeds,99999,False,"s"],400,210+sliderY[4],False)
a_seed4 = Achievement("fledgling garden"," make 1M cookies",[seeds,999999,False,"s"],400,265+sliderY[4],False)
a_seed5 = Achievement("affluent garden"," make 100M cookies",[seeds,99999999,False,"s"],400,320+sliderY[4],False)
a_seed6 = Achievement("world-famous garden"," make 1B cookies",[seeds,999999999,False,"s"],400,375+sliderY[4],False)
a_seed7 = Achievement("cosmic garden"," make 100B cookies",[seeds,99999999999,False,"s"],400,430+sliderY[4],False)
a_seed8 = Achievement("galactic garden"," make 1T cookies",[seeds,999999999999,False,"s"],400,485+sliderY[4],False)
a_sps1 = Achievement("casual gardening","make 1 seed per sec",[totalSPS,0,False,"sps"],400,540+sliderY[4],False)
a_sps2 = Achievement("hardcore gardening","make 10 seeds per sec",[totalSPS,9,False,"sps"],400,595+sliderY[4],False)
a_sps3 = Achievement("steady growing stream","make 100 seeds per sec",[totalSPS,99,False,"sps"],400,650+sliderY[4],False)
a_sps4 = Achievement("seed monster","make 1000 seeds per sec",[totalSPS,999,False,"sps"],400,705+sliderY[4],False)
a_sps5 = Achievement("mass producer","make 10000 seeds per sec",[totalSPS,9999,False,"sps"],400,760+sliderY[4],False)
a_sps6 = Achievement("seed vortex","make 100000 seeds per sec",[totalSPS,99999,False,"sps"],400,815+sliderY[4],False)
a_sps7 = Achievement("seed pulsar","make 1000000 seeds per sec",[totalSPS,999999,False,"sps"],400,870+sliderY[4],False)
a_sps8 = Achievement("seed quasar","make 10000000 seeds per sec",[totalSPS,9999999,False,"sps"],400,925+sliderY[4],False)

achievementList = [a_seed1,a_seed2,a_seed3,a_seed4,a_seed5,a_seed6,a_seed7,a_seed8,a_sps1,a_sps2,a_sps3,a_sps4,a_sps5,a_sps6,a_sps7,a_sps8]






isBugOnPlant = False
bugStorage = 0
bugX = 1540    
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("plant clicker")
timer = 0
shopcounter = [0,0,0]
shopprice = [15,100,1500]
#shopSPS= [0.1,1,10]
bugFull = False
font = pygame.font.Font(pygame.font.get_default_font(), 10)
fontBig = pygame.font.Font(pygame.font.get_default_font(), 20)
pygame.display.flip()
amountOfBuildings = [0,0,0]
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
        seeds += totalSPS
        bugCapacity = seeds/6
        bugChance = random.randint(0,50)
        print(bugChance)
        print(isBugOnPlant)
        if isBugOnPlant == False and bugChance <3:
            isBugOnPlant ==  True
        if isBugOnPlant == True and bugX > 130:
            bugX -= 20
        if isBugOnPlant == True and bugX <= 130:

            if bugStorage < bugCapacity:
                seeds -= bugCapacity/10
                bugStorage += bugCapacity/10
                bugColor = brown
            else: 
                bugColor = yellow
                bugFull = True
        achBackground = pygame.draw.rect(screen,skyC,(400,0,500,800))
        for i in achievementList:
            
            if changed:
                i.Y+=change
            if i.rec1[3] == "s":
                i.rec1[0]=seeds
            elif i.rec1[3] == "sps":
                i.rec1[0]=totalSPS
            i.run(screen,green,font,black)
        change=0
        changed=False

        

    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 60 and mpos1 < 160 and mpos2 > 100 and mpos2 < 280:
        seedGen = True
    if event.type == pygame.MOUSEBUTTONUP and mpos1 > 60 and mpos1 < 160 and mpos2 > 100 and mpos2 < 280 and seedGen:
        seeds += 1
        seedGen = False
        print(seeds)
    if event.type == pygame.MOUSEBUTTONDOWN and mpos2 > sliderY[0] and mpos2 < sliderY[1] and mpos1 >600 and mpos1 < 700 and seeds > shopprice[0]:
        totalSPS += 1
        seeds-=shopprice[0]
        shopprice[0]+=5
        amountOfBuildings[0]+=1
        shopcounter[0]+=1
    if event.type == pygame.MOUSEBUTTONDOWN and mpos2 > sliderY[1] and mpos2 < sliderY[2] and mpos1 >600 and mpos1 < 700 and seeds > shopprice[1]:
        totalSPS += 10
        seeds-=shopprice[1]
        shopprice[1]+=33
        amountOfBuildings[1]+=1
        shopcounter[1]+=1
    if event.type == pygame.MOUSEBUTTONDOWN and mpos2 > sliderY[2] and mpos2 < sliderY[3] and mpos1 >600 and mpos1 < 700 and seeds > shopprice[2]:
        totalSPS += 100
        seeds-=shopprice[2]
        shopprice[2]+=500
        amountOfBuildings[2]+=1
        shopcounter[2]+=1
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 550 and mpos1 < 570 and mpos2 > 150 and mpos2 < 170:
        sliderY[0]-=2
        sliderY[1]-=2
        sliderY[2]-=2
        sliderY[3]-=2
        sliderY[4]-=2
        change-=2
        changed=True
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 550 and mpos1 < 570 and mpos2 > 260 and mpos2 < 280:
        sliderY[0]+=2
        sliderY[1]+=2
        sliderY[2]+=2
        sliderY[3]+=2
        sliderY[4]+=2
        change+=2
        changed=True
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > bugX and mpos1 < bugX + 40 and mpos2 > 175 and mpos2 < 195 and bugFull:
        seeds += bugCapacity*2
        bugFull ==False
        isBugOnPlant == False
        bugX ==360
#    for i in range(0,totalSPS):
#       pygame.draw.rect(screen,brown,(0,random.randint(1,250),0,3,3))
    
    text_surface = fontBig.render(str(seeds)+" seeds", True, (0, 255, 0))
    
    plantHitbox = pygame.draw.rect(screen,skyC,(60,100,100,180))
    plantBackground = pygame.draw.rect(screen,skyC,(0,0,400,800))
    plantBackground = pygame.draw.rect(screen,skyC,(500,0,600,800))
    dirt = pygame.draw.rect(screen,brown,(0,250,250,40))
    stem = pygame.draw.rect(screen,green,(80,150,20,100))
    leaf1 = pygame.draw.rect(screen,green,(40,194,40,30))
    leaf2 = pygame.draw.rect(screen,green,(100,184,40,30))
    flower = pygame.draw.rect(screen,pink,(70,124,40,30))
    flower2 = pygame.draw.rect(screen,pink,(80,144,20,25))
    pollen = pygame.draw.rect(screen,yellow,(84,124,12,15))
    insect = pygame.draw.rect(screen,bugColor,(bugX,125,40,20))
    wall1 = pygame.draw.rect(screen,(70,50,0),(250,0,20,800))
    wall2 = pygame.draw.rect(screen,(70,50,0),(550,0,20,800))
    sliderfront = pygame.draw.polygon(screen,yellow,((570,260),(560,270),(550,260)),3)
    sliderback = pygame.draw.polygon(screen,yellow,((570,160),(560,150),(550,160)),3)
    text_tutorial = font.render("Welcome to plant clicker! Click the flower to ",True,(0,0,0))
    text_tutorial2 = font.render("get seeds, and click the buttons down below  ",True,(0,0,0))
    text_tutorial3 = font.render("to buy items ( or people ) that help you   ",True,(0,0,0))
    text_tutorial4 = font.render("gather seeds. More updates are coming! ",True,(0,0,0))
    text_tutorial5 = font.render("Have fun playing Plant Clicker!",True,(0,0,0))
    buttonSClip = pygame.draw.rect(screen,green,(570,sliderY[0],228,60))
    text_clip = font.render("clipper ", True, (0, 0, 0))
    text_clip_price = font.render("sps: 1 prc: "+str(shopprice[0])+" amount: "+str(amountOfBuildings[0]), True, (0, 0, 0))
    screen.blit(text_clip, dest=(600,sliderY[0]+2))
    screen.blit(text_clip_price, dest=(600,sliderY[0]+12))
    buttonSgardener = pygame.draw.rect(screen,green,(570,sliderY[1]+5,228,60,))
    text_grdr = font.render("gardener", True, (0, 0, 0))
    text_grdr_price = font.render("sps: 10 prc:"+str(shopprice[1])+" amount: "+str(amountOfBuildings[1]), True, (0, 0, 0))
    screen.blit(text_grdr, dest=(600,sliderY[1]+7))
    screen.blit(text_grdr_price, dest=(600,sliderY[1]+17))
    buttonSgarden = pygame.draw.rect(screen,green,(570,sliderY[2]+9,228,60))
    text_grd = font.render("garden", True, (0, 0, 0))
    text_grd_prc = font.render("sps: 100 prc: "+str(shopprice[2])+" amount: "+str(amountOfBuildings[2]), True, (0, 0, 0))
    text_totalSPS = font.render(str(totalSPS)+" SPS",True,(255,200,0))
    screen.blit(text_tutorial,dest=(3,3))
    screen.blit(text_tutorial2,dest=(3,13))
    screen.blit(text_tutorial3,dest=(3,23))
    screen.blit(text_tutorial4,dest=(3,33))
    screen.blit(text_tutorial5,dest=(3,43))
    screen.blit(text_totalSPS,dest=(80,80))
    screen.blit(text_grd, dest=(600,sliderY[2]+11,))
    screen.blit(text_grd_prc,dest=(600,sliderY[2]+21,))
    screen.blit(text_surface, dest=(60,60))
    round(seeds,1)
    pygame.display.flip()     
