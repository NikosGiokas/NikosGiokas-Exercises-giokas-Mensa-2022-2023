import random
import time
import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Hangman")

#RBG
BLACK = (0,0,0)
WHITE = (255,255,255)
PURPLE = (140,0,120)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

secret = ""
lives = 7
letters = []
words = []
guess=""

hanghorizontal = pygame.Rect(10,20,175,20)
hangvertical = pygame.Rect(10,20,20,300)

torso = pygame.Rect(100,100,50,100)
hand1 = pygame.Rect(75,100,20,70)
hand2 = pygame.Rect(155,100,20,70)
leg1 = pygame.Rect(100,205,20,100)
leg2 = pygame.Rect(130,205,20,100)

base_font = pygame.font.Font(None,32)

def drawhang():
    global screen, hanghorizontal, hangvertical, GREEN
    pygame.draw.rect(screen,GREEN,hanghorizontal)
    pygame.draw.rect(screen,GREEN,hangvertical)


def drawhangman(lives):
    #zografizo anthrwpaki
    if lives <= 6:
        #zografizo to kefali
        pass
    if lives <= 5:
        #zografiso to soma
        pass        
    pass    

def loadwordfile():
    global words
    with open("enable1.txt",encoding="utf-8") as f:
        words = f.read().splitlines()
        
def chooseword(mylist):
    return random.choice(mylist)

def readinput(sec,text):
    global lives,letters
    if text in letters:
        return True
    if text in sec:
        letters.append(text)
    else:
        lives = lives-1
        letters.append(text)
    return True

def checkwinnerbyletters(hiddenword):
    if "_" in hiddenword:
        return False
    #print("You have won!")
    return True

def updateHiddenWord(sec,let):
    hiddenword = ""
    for l in sec:
        if l in let:
            hiddenword+=l
            #print(l,end=" ")
        else:
            hiddenword+="_"
            #print("_",end=" ")
    #print("")
    #print(hiddenword)
    return hiddenword

loadwordfile()
secret = chooseword(words)
hiddenword = updateHiddenWord(secret,letters)
done = False
while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_a, pygame.K_z + 1):
                guess = event.unicode.lower()
                if readinput(secret,guess) :
                   if checkwinnerbyletters(hiddenword):
                        done = True
                hiddenword = updateHiddenWord(secret,letters)


    screen.fill(BLACK)
    drawhang()
    drawhangman(lives)

    text_surface = base_font.render(hiddenword,True,BLUE)
    screen.blit(text_surface,(200,200))

    text_surface = base_font.render(str(lives),True,RED)
    screen.blit(text_surface,(400,32))

    pygame.display.update()
    clock.tick(15)

time.sleep(10)
pygame.quit()

