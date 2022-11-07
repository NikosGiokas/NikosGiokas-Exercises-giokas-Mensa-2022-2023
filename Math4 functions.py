



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
        move = int(input("give me a number from 1 to 9: "))
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
    return True
for i in range(10):
    func()
    readmove(token)
    if checkWinner():
        print(token + " has won!")
        break
    changeturn()