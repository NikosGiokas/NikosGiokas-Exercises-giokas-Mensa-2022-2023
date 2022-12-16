####
# 
#Askiseis listes 2
#Askisi 8 
# 
#   @author Niko
#  Version  0.0.1
#  Date  19.11.2022    
#    
# #

#Γράψτε μία συνάρτηση σε python η οποία θα δέχεται ως όρισμα μία λίστα
#  από λέξεις και θα εμφανίζει τη λέξη με το μεγαλύτερο μήκος

words = [""]

for word in words:
    word=input("give me a word: ")
    if word == "":
        break
    else:
        words.append(word)


print("the biggest word is ",max(words,key=len))






