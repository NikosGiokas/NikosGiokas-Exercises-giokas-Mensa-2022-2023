import pygame 
import random
# base code
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("myGame")
#
# COLORS
N = (0,0,0)
R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
YEL = (255,255,0)
PUR = (255,0,255)
W = (255,255,255)
#
# player
class Player:
    def __init__(self):
        self.hp  = 100
        self.atk = 5
        self.equip = ["punch"]
        self.color = YEL
        self.speed = 20
        self.size = 20
        self.x = screen.get_width()/2
        self.y = screen.get_height()/2
    def draw(self):
        pygame.draw.rect(screen,self.color,((self.x,self.y),(self.size,self.size)))
    def move(self,directions): 
        if directions==-1:
            self.y += self.speed
        elif directions==1:
            self.y -= self.speed
        elif directions==2:
            self.x -= self.speed
        elif directions==-2:
            self.x += self.speed
pl = Player()
def getDistance(obj1,obj2):
    distanceX = obj1.x-obj2.x
    distanceY = obj1.y-obj2.y
    return round(distanceX - distanceY/2)
class Enemy:
    def __init__(self,kind,pl):
        self.kind = kind 

        self.x = random.randint(0,pl.x-70)
        self.y = random.randint(0,pl.y-70)
        self.color = (255,180,0)
        self.atkdraw = self.atkdraw0
        self.size = 20
    def atkdraw0(self):
        if(getDistance(pl,self)<70):
            pl.hp-=0.1
        pygame.draw.rect(screen,self.color,((self.x,self.y),(self.size,self.size)))
        
lava = Enemy(0,pl)

            
        
#game loop
done = False
while done == False and pl.hp > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if(event.key==pygame.K_DOWN):
                pl.move(-1 )
            elif event.key == pygame.K_UP:
                pl.move(1 )
            elif event.key == pygame.K_LEFT:
                pl.move(2 )
            elif event.key == pygame.K_RIGHT:
                pl.move(-2 )
     
    screen.fill(G)
    pl.draw()
    lava.atkdraw0() 
    pygame.display.update()
    clock.tick(60)

pygame.quit()