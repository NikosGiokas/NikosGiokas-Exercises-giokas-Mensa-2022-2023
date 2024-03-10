import random


currentNum = 10
usedNum = currentNum
step = 0
sampletime = 97000
isSampleable = False
def isEven(num):
    if num%2==1:
        return True
        
    else:
        return False
    


while currentNum<=1000000:
    while usedNum!=1:
            if isEven(usedNum)==True:
                usedNum*=3
                usedNum+=1
                step+=1
            else:
                usedNum/=2
                step+=1
            if sampletime==0:
                isSampleable=True
            if usedNum==1 and isSampleable:
                print(currentNum)
                print(step)
                print("   ")
                sampletime+=random.randint(95000,150000)
                isSampleable=False
    
    
    
    currentNum+=1
    usedNum=currentNum    
    step=0
    sampletime-=1
    
    
    









