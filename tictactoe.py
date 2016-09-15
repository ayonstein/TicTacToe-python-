gameover = False
win = False
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printBoard():
    for i in range(len(board)):
        if i>0 and i % 3 == 0:
            print ("\n--------------")
        print (" "+str(board[i])+" |"),
    print ("\n")

def checkAll():
    allDone = False
    for i in range(len(board)):
        if board[i]!="X" and board[i]!=0:
            allDone = True
    return allDone


def compInput():
    for i in range(len(board)):
        if i>0 and i % 3 == 0:
            print ("\n--------------")
        print (" "+str(board[i])+" |"),
    print ("\n")

def selectPosition(gameover):
    """gamer input"""
    selI = input("Select a position: ")
    if selI < 1 and selI > 9:
        print ("Wrong input!")
    elif board[selI-1]==0:
        if checkAll() == True:
            print ("Game Over!")
            gameover = True
        else:
            print ("Already blocked!")
        printBoard()
    else:
        board[selI-1] = 0
        printBoard()

    """computer input"""
    compInput()

    for i in range(len(board)):
        if (i%3 == 0):
            if(board[i]==board[i+1] and board[i+1]==board[i+2]):
                gameover = True
                win = True
                print ("You WIN!")
                break
        if (i<3 and board[i] == board[i+3] and board[i+3] == board[i+6]):
            gameover = True
            win = True
            print ("You WIN!")
            break;
    if((board[0] == board[4] and board[4] == board[8]) or  (board[2] == board[4] and board[4] == board[6])):
        gameover = True
        win = True
        print ("You WIN!")
    return gameover

print ("Welcome to TIC TAC TOE Game!")
print ("Let's see if you can beat me!")


printBoard()

while gameover == False:
    gameover = selectPosition(gameover)



