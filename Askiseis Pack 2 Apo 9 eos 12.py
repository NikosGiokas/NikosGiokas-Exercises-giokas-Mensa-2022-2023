####
# Mathima ....
# Askiseis Pack 2 
# 
# 
#  @author Niko
#  Version  0.0.1
#  Date  19.11.2022    
#    
# #
# askisi 9

#paidia = int(input("Dose aritho paidion: "))
#misthos = int(input("Dose basiko mistho: "))
#def epidoma():
#    global paidia, misthos
#    if paidia > 3:
#        bonus = (paidia - 3) * 0.08 + 0.11
#    elif paidia == 3:
#        bonus = 0.11
#    elif paidia == 2:
#        bonus = 0.06
#    elif paidia == 1:
#        bonus = 0.03
#    return print("o misthos sou einai: ",misthos + bonus * misthos / 10 )
#epidoma()
# askisi 10
# Να γράψετε πρόγραμμα σε Python που θα δέχεται τον προφορικό και το γραπτό βαθμό 
# ενός μαθητή και θα υπολογίζει το μέσο όρο του και εξάγει αποτέλεσμα προαγωγής. 
# Ο μαθητής προάγεται αν έχει μέσο όρο πάνω από 9.5, διαφορετικά παραπέμπεται για
#  επανεξέταση.

#
#graptoBathmo = int(input("graptos Bathmos: "))
#proforikoBathmo = int(input("proforikos Bathmos: "))
#def bathmos():
#    global graptoBathmo, proforikoBathmo
#    Bathmos = (graptoBathmo + proforikoBathmo) / 2
#    if Bathmos > 9.4:
#        print("perases!")
#    else:
#        print("den perases")
#bathmos()

# askisi 11
#Ένα θέατρο έχει 3 κατηγορίες εισιτηρίων,
# για ενήλικους, για ανήλικους και για φοιτητές.
#  Οι ενήλικοι πληρώνουν 15 €, ενώ οι ανήλικοι 10 €.
#   Οι φοιτητές είναι ηλικίας 18-25 και έχουν έκπτωση 25% στο εισιτήριο των ενηλίκων.
#  Να γραφεί πρόγραμμα σε Python το οποίο θα ζητά την ηλικία ενός θεατή,
# θα υπολογίζει και θα εμφανίζει το κόστος του εισιτηρίου του.


#spectatorAge = int(input("please give me your age: "))

def price():
    global spectatorAge
    cost = 0
    if spectatorAge < 18:
        cost = 10
    elif spectatorAge >= 18 and spectatorAge < 26:

        cost = 15*0.75
    else:


        cost = 15
    print("it will cost",cost,"€")
#price()


#askisi 12

#Να γραφτεί πρόγραμμα σε γλώσσα Python που να υπολογίζει το μισθό ενός εργαζομένου,
# ο οποίος δουλεύει με σύμβαση ωρομισθίου σε μια εταιρεία. Να διαβάζει το όνομά του,
# τις ώρες εργασίας του μήνα, το ωρομίσθιό του και αν είναι έγγαμος ή άγαμος. 
# Οι κρατήσεις που του γίνονται, εξαρτώνται από το ύψος του μισθού. 
# Αν ο μισθός είναι μέχρι 1000€ το μήνα, έχει 15% κρατήσεις, ενώ διαφορετικά έχει 25% κρατήσεις. 
# Επίσης, αν είναι έγγαμος, έχει ένα επίδομα 50€.


workerName = input("give me the name of the worker: ")
workerHours = input("give me the hours of the worker: ")
workerSalary = int(input("give me the salary of the worker: "))
isWorkerMarried = int(input("give me a 1 if the worker is married: "))
deduction = 0
def workerDeduction():
    global workerSalary
    if workerSalary > 1000:
        deduction = 0.75
    else:
        deduction = 0.85
    
    workerSalary*=deduction

    if isWorkerMarried == 1:
        workerSalary+=50
    print(workerSalary)
workerDeduction()