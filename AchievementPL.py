import pygame

class Achievement:
    def __init__(self,name,rec,rec1,X,Y,taken):
        self.name = name 
        self.rec = rec
        self.rec1 = rec1
        self.X = X
        self.Y = Y
        self.taken=taken
    def hide(self,screen,color):
        pygame.draw.rect(screen,color,(self.X,self.Y,100,50))
        print("drawn")
    def show(self,screen,font,fontColor):
        textR = font.render(self.name,True,fontColor)
        textR2 = font.render(self.rec,True,fontColor)
        screen.blit(textR,dest=(self.X+3,self.Y+3))
        screen.blit(textR2,dest=(self.X+3,self.Y+13))        
        #textR2 = font.render(self.rec2,True,black)
        #screen.blit(textR,dest=(self.X+3,self.Y+13))
        print("written")
    def run(self,screen,color,font,fontColor):
        self.hide(screen,color)
        if self.rec1[0]>self.rec1[1] or self.taken:
            self.show(screen,font,fontColor)
            self.taken=True