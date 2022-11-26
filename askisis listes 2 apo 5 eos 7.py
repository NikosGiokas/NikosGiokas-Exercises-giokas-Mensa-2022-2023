####
# askiseis listes 2
# 
#  @author Niko
#  Version  0.0.1
#  Date  23.11.2022    
#    
# #


# askisi  5
#Γράψτε πρόγραμμα σε python το οποίο θα γεμίζει μία λίστα με 10 βαθμολογίες από το 1 μέχρι το 20 
# ( Ελεγχος ορθότητας δεδομένων) και μετά  θα υπολογίζει και εμφανίζει το μέσο όρο τους.

bathmologies = []


while len(bathmologies)<10:
    bathmos = int(input("give me a value from 1 to 20: "))
    if bathmos>0 and bathmos<21:
        bathmologies.append(bathmos)
    else:
        print("please enter a valid number")

def mesosOros():
    sUm = 0
    global bathmologies
    for j in range(0,9):
        sUm += bathmologies[j]

    return print( sUm/10)

mesosOros()


# askisi 6  

#arithmoi = [int(input("give me a value")),int(input("give me a value")),int(input("give me a value")),]
#def mikrotero():
#    global arithmoi
#    if arithmoi[0] < arithmoi[1] and arithmoi[0]<arithmoi[2]:
#        return print(arithmoi[0]," is smaller")
#    elif arithmoi[1] < arithmoi[0] and arithmoi[1]<arithmoi[2]:
#        return print(arithmoi[1]," is smaller")
#    elif arithmoi[2] < arithmoi[1] and arithmoi[2]<arithmoi[0]:
#        return print(arithmoi[2]," is smaller")
#    else:
#        return print("some are the same")
#mikrotero()

# askisi 7 
#def posesForesMikro():
#    global arithmoi
#    if arithmoi[0] < arithmoi[1] and arithmoi[0]<arithmoi[2]:
#        return print(arithmoi[0]," is smaller")
#    elif arithmoi[1] < arithmoi[0] and arithmoi[1]<arithmoi[2]:
#        return print(arithmoi[1]," is smaller")
#    elif arithmoi[2] < arithmoi[1] and arithmoi[2]<arithmoi[0]:
#        return print(arithmoi[2]," is smaller")
#    elif arithmoi[0] == arithmoi[1]:
#        return print( arithmoi[0],"and", arithmoi[1],"are the same")
#    elif arithmoi[1] == arithmoi[2]:
#        return print( arithmoi[0],"and", arithmoi[1],"are the same")
#    elif arithmoi[2] == arithmoi[0]:
#        return print( arithmoi[0],"and", arithmoi[1],"are the same")
#posesForesMikro()

