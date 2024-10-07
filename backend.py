def gameNotEnded(board):
    for i in board:
        for j in i:
            if j == 1:
                return True
    return False

def attack(board, x, y):
    (x,y) = (y,x)
    hit = False
    for i in range(len(board)):
        print()
        print("Ligne " + str(i) + ":", end =" ")
        for j in range(len(board[i])-1):
            if(i == x and j == y):
                if(board[i][j] == 1):
                    print("\033[32m" + "X", end = " ")
                    board[i][j] = 0
                    hit = True
                else:
                    print("\033[31m" + str(board[x][y]), end = " ")
                print("\033[0m", end = "")
            else:
                print(board[i][j], end=" ")     
    print()
    print("\033[32m" + "Touché !" + "\033[0m" if hit else "\033[31m" + "Raté !" + "\033[0m")
    print()
    
    
# \033[0m   : Reset
# \033[31m  : Red
# \033[32m  : Green