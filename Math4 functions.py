



board = ["1","2","3","4","5","6","7","8","9",]
token = "X"

def func():
    global board
    print(" {0} | {1} | {2}".format(board[0],board[1],board[2]))
    print("---|---|---")
    print(" {0} | {1} | {2} ".format(board[3],board[4],board[5]))
    print("---|---|---")
    print(" {0} | {1} | {2} ".format(board[6],board[7],board[8]))



def readmove(token):
    global board
    while True:
        try:
            move = int(input("give me a number from 1 to 9: "))
        except:
            print("only numbers please")
            continue
        if move <1 or move >9:
            print("please enter a valid number")
        else:
            if board[move-1] in ("X","O"):
                print("box already taken")
            else:
                board[move-1] = token
                return
def changeturn():
    global token
    if token == "X":
        token = "O"
    else:
        token = "X"
def checkWinner():
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]:
            return True
    for i in range(3):
        if board[i]==board[i+3]==board[i+6]:
            return True
    if board[0]==board[4]==board[8]:
        return True
    if board[2]==board[4]==board[6]:
        return True
    return False
winner=""
for i in range(9):
    func()
    readmove(token)
    if checkWinner():
        winner = token
        print(winner + " has won!")
        break
    changeturn()
if winner == "":
    print("it's a tie") 
else:
    print(winner," has won")