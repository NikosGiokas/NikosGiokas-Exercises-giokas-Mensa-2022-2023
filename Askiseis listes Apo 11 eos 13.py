####
# Mathima ....
# 
#Askiseis listes
#Askiseis apo 11 eos 13
#  @author Niko
#  Version  0.0.1
#  Date  16.12.2022    
#    
# #


# askisi 11
#Γράψτε μία συνάρτηση σε python η οποία θα δέχεται ως όρισμα μία λίστα με αριθμούς 
# και θα επιστρέφει το άθροισμα των στοιχείων της. 


nums = [2,3,1]

finalNum = 0
def getAthroisma():
    global finalNum
    for num in nums:
        finalNum += num
    print("sum = ",finalNum)

#getAthroisma()


# askisi 12
#Γράψτε μία συνάρτηση σε python η οποία θα δέχεται ως όρισμα μία λίστα από λέξεις και 
# θα επιστρέφει τη λέξη με τα περισσότερα φωνήεντα.


lekseis =["notio ","hamster","kalos","aaaaaaa","number"]

maxvowel = 0
biggestWord = ""
def findWordWithMostVowels(words):
    global maxvowel
    num_vowels=0
    for word in words:
        for char in word:
            if char in "aeiouAEIOU":
                num_vowels = num_vowels+1
        if num_vowels > maxvowel:
            maxvowel = num_vowels
            biggestWord = word
        num_vowels = 0
    print( biggestWord," has the most vowels, ",maxvowel)

#findWordWithMostVowels(lekseis)


# Askisi 13
# Γράψτε μία συνάρτηση σε python η οποία θα δέχεται ως όρισμα μία λίστα από αριθμούς 
# (πιθανόν καθένας από αυτούς να εμφανίζεται περισσότερες από μία φορά) 
# και θα επιστρέφει μία λίστα όπου κάθε αριθμός εμφανίζεται μόνο μία φορά δηλαδή θα αφαιρεί 
# τυχόν διπλοεγγραφές