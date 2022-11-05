
####
# askisi 4
#  @author Niko
#  Version  0.0.1
#  Date  15.10.2022
# 
# 
# 
# #



speed = int(input("what is your speed"))
badP = 0
if speed <= 70:
    print("okay") 
    
#mipos yparxei pio exypnos tropos apo auto???
if speed <= 75 and speed >= 71 :
    print("one bad point") 
    badP = 1
if speed <= 80 and speed >= 76 :
    print("two bad points") 
    badP = 2
if speed <= 85 and speed >= 81 :
    print("three bad points") 
    badP = 3
if speed <= 90 and speed >= 86 :
    print("four bad points") 
    badP = 4
if speed <= 95 and speed >= 91 :
    print("five bad points") 
    badP = 5
if speed <= 95 and speed >= 91 :
    print("six bad points") 
    badP = 6
if speed <= 95 and speed >= 91 :
    print("seven bad points") 
    badP = 7
if speed <= 100 and speed >= 96 :
    print("eight bad points") 
    badP = 8
if speed <= 105 and speed >= 101 :
    print("nine bad points") 
    badP = 9
if speed <= 110 and speed >= 105 :
    print("ten bad points") 
    badP = 10
if speed <= 115 and speed >= 111 :
    print("eleven bad points") 
    badP = 11
if speed <= 120 and speed >= 116 :
    print("twelwe bad points") 
    badP = 12
    print("bad points: > "+ str(badP))
if speed >= 121 :
    badP = 13
    print("license suspended")

    print("bad points: > "+ str(badP))
