####
# askisi 1.a
# 
#  @author Niko
#  Version  0.0.1
#  Date  29.10.2022    
#    
# #

'''
# askisi 1.a
listOfPointers = [0,1,2,3,4]
print(listOfPointers)
listOfPointers.clear() #einai synartisi thelei ()

# askisi 1.b
listOfNumbers = []
for decimal in range(0,10):
    listOfNumbers.append(decimal)

print(listOfNumbers)


# askisi 1.c
numDiv2 = 500
listOfhalves = [500]
for number in range(0,11):
    numDiv2 = numDiv2/2
    listOfhalves.append(numDiv2)

print(listOfhalves)



# askisi 2
personalList = []
for i in range(1,11): 
    personalList.append(input("give me a number: "))
print(personalList)

'''

# askisi 3
# Να γράψετε πρόγραμμα σε python το οποίο θα δημιουργεί μία λίστα και θα τη γεμίζει με 
# αριθμούς που θα δίνει ο χρήστης. Η εισαγωγή θα τελειώνει όταν ο χρήστης θα δίνει το μηδέν. 
# Το μηδέν δεν θα εισάγεται στη λίστα. 
persList = [] #den sou leei na bazeis proto stoixeio diko sou
while(True):
    persListnum=int(input("give me a number: "))
    if(persListnum != 0):
        persList.append(persListnum)
    else:
        break
print(persList)











# askisi 4
# Pos tha mporouse na ginei kalutera??????
persList = [] # den sou leei na bazeis proto stoixeio
while(True):
    persListstr=input("give me a word: ")
    if(persListstr != "end"):
        persList.append(persListstr)
    else:
        break

print(persList)