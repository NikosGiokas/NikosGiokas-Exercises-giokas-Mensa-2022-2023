####
# 
#Askiseis listes
#Askisi 9 and 10 
# 
#   @author Niko
#  Version  0.0.1
#  Date  19.11.2022    
#    
# #

#Γράψτε μία συνάρτηση η οποία θα παίρνει ως όρισμα μία λίστα και μία τιμή και θα ελέγχει
#  σε ποια θέση της λίστας πρωτοεμφανίζεται η τιμή. Σε περίπτωση που η τιμή δεν υπάρχει καθόλου
#  στη λίστα θα επιστρέφεται -1.


bathmologies = [4,5,1,9,7]
num = int(input("for what number do you want to search"))

listPointer = 0
def counterOfNumberOfBathmologies(bathmologies, nun):
    global listPointer
    for vathmos in bathmologies:
        if vathmos==num:
            listPointer = bathmologies.index(vathmos)
    print("The number ", num, " is found at position ",listPointer+1," of the list.")

counterOfNumberOfBathmologies(bathmologies, num)

# 10. Na γράψετε μία συνάρτηση σε python η οποία θα παίρνει ως ορίσματα μία λίστα και έναν αριθμό 
# και θα επιστρέφει πόσες φορές περιέχεται αυτός ο αριθμός στη λίστα.

#bathmologies = [3,4,5,1,3,9,7,3,1,5,3,8,9,7]
#num = int(input("for what number do you want to search"))

listPointer = 0
def counterOfNumberOfBathmologies(bathmologies, nun):
    global listPointer
    for vathmos in bathmologies:
        if vathmos==num:
            listPointer = listPointer+1
    print("The number ", num, " is found ",listPointer," time/s in the list.")

#counterOfNumberOfBathmologies(bathmologies, num)
