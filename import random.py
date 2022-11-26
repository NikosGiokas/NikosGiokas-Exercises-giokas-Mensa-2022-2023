import random

secret = ""
zoes = 7
letters = []
hiddenword = ""
easyWords = ["apple","what","bush","hello","golf","moon"]
mediumWords = ["welcome","weird","error","snake","sin","beam"]
hardWords = ["sunshine","minecraft","machete","programmer","gaming","collision"]
def findWord():
    global easyWords,mediumWords,hardWords
    difficuty = int(input("type 0 for easy, 1 for medium, 2 for hard"))
    easy = 0
    medium = 1
    hard = 2
    if difficuty==0:
        return  random.choice(easyWords)
    if difficuty==1:
        return  random.choice(mediumWords)
    if difficuty==2:
        return  random.choice(hardWords)
word = findWord()
secret = findWord()
def readInput(sec):
    letterInput =  input("give me a letter ")
    if letterInput in word:
        print(letterInput," is in word")
        letters.append(letterInput)
    else:
        zoes-1
    if  letterInput == word:
        print("you won!")
    else:
        print("you lost. the word was ",word )
def checkWinner():
    global hiddenword
    if "_" in hiddenword
readInput(secret)











