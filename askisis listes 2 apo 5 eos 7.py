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

def eisagogiVathmologion():
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

#mesosOros()
#eisagogiVathmologion()


# askisi 6  
 #Να γράψετε μία συνάρτηση σε python η οποία θα παίρνει ως όρισμα μία λίστα με αριθμούς και
 #  θα επιστρέφει τον μικρότερο από αυτούς

#eisagogiVathmologion()

def findMin():
    min = bathmologies[0]
    for vathos in bathmologies:
        if vathos<min:
            min = vathos
    print("The number ", min, "is the smallest")
    return min
        

#findMin()




# askisi 7 
#Να γράψετε μία συνάρτηση σε python η οποία θα δέχεται ως όρισμα μία λίστα και θα υπολογίζει ποιος είναι 
# ο μικρότερος αριθμός και θα επιστρέφει πόσες φορές αυτός εμφανίζεται.



counter = 0
def counterOfSmallesNumberOfBathmologies():
    global counter
    min = findMin()
    for vathmos in bathmologies:
        if vathmos==min:
            counter = counter+1
    print("The number ", min, " is found ",counter," in the list.")
    
        

eisagogiVathmologion()
counterOfSmallesNumberOfBathmologies()