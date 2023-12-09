import pygame

class Box():
    def __init__(self,size,x,y,color,x_vel,y_vel):
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.x_vel = x_vel
        self.y_vel = y_vel

    def move(self,screen):
        self.x += self.x_vel
        self.y += self.y_vel
        if (self.x<=0) or (self.x>=screen.get_width()-self.size):
            self.x_vel = - self.x_vel
        if (self.y<=0) or (self.y>=screen.get_height()-self.size):
            self.y_vel = - self.y_vel 
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,((self.x,self.y),(self.size,self.size))) 