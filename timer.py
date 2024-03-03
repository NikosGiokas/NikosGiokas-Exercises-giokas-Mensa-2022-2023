import pygame
import sys
pygame.init()
width = 400
height = 410
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("timer")
font = pygame.font.Font(pygame.font.get_default_font(), 15)
fontBig = pygame.font.Font(pygame.font.get_default_font(), 50)
open = True
time = 0
timerActive = False
sec = 0
while open:
    pygame.time.wait(20)
    time += 1
    for event in pygame.event.get():
        mpos = pygame.mouse.get_pos()
        mpos1 = mpos[0]
        mpos2 = mpos[1]
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    if time == 50 and timerActive:
        sec -=1
        time-=50
    if sec == 0:
        timerActive = False
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 45 and mpos1 < 145 and mpos2 > 300 and mpos2 < 350 :
        sec-=sec
        sec += 20
        time -= 5
        timerActive = True
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 150 and mpos1 < 250 and mpos2 > 300 and mpos2 < 350 :
        sec-=sec
        sec += 30
        time -= 5
        timerActive = True
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 255 and mpos1 < 355 and mpos2 > 300 and mpos2 < 350 :
        sec-=sec
        sec += 45
        time -= 5
        timerActive = True
    if event.type == pygame.MOUSEBUTTONDOWN and mpos1 > 150 and mpos1 < 250 and mpos2 > 355 and mpos2 < 405 :
        sec-=sec
    background = pygame.draw.rect(screen,(255,255,255),(0,0,400,410))
    button20 = pygame.draw.rect(screen,(50,50,255),(45,300,100,50))
    button30 = pygame.draw.rect(screen,(50,50,255),(150,300,100,50))
    button45 = pygame.draw.rect(screen,(50,50,255),(255,300,100,50))
    buttonReset = pygame.draw.rect(screen,(50,50,255),(150,355,100,50))
    text_button45 = font.render("45 seconds", True, (0, 0, 0))
    text_button30 = font.render("30 seconds", True, (0, 0, 0))
    text_button20 = font.render("20 seconds", True, (0, 0, 0))
    text_title = fontBig.render("TIMER", True, (0, 0, 0))
    text_reset = font.render("reset", True, (0, 0, 0))
    screen.blit(text_button20, dest=(55,320))
    screen.blit(text_button30, dest=(160,320))
    screen.blit(text_button45, dest=(265,320))
    screen.blit(text_title, dest=(120,30))
    screen.blit(text_reset, dest=(175,375))
    text_timer = fontBig.render(str(sec), True, (0, 0, 0))
    screen.blit(text_timer, dest=(180,100))
    pygame.display.flip()