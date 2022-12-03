####
# askiseis class Askisi2
# 
#  @author Niko
#  Version  0.0.1
#  Date  03.12.2022    
#    
# #



class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def repr(self):
        print('%d %d %d' % (self.x,self.y, self.z ))

myPoint = Point3D(1,2,3)
myPoint.repr()


        
