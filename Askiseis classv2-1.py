####
# 
#Askiseis class v2
#Askisi 1
# 
#   @author Niko
#  Version  0.0.1
#  Date  19.11.2022    
#    
# #

class Car:
    def __init__(self, make, color, year):
        self.make=make
        self.speed  = 60
        self.color  = color
        self.year = year
    def speed_up(self,speed):
        self.speed  = speed
        print ("I am driving at a speed", self.speed,"km/h")
    def turn(self):
        turnDirection = int(input("0 for left, 1 for right"))
        if ( turnDirection == 0):
            print ("I am turning left ")
        else:
            print ("I am turning right ")



convertible = Car("bmw",60,"black",2013)

sedan = Car("toyota",90,"red",2009)

convertible.turn()
sedan.speed_up(90)



