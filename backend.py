def jeuEnCours(board):
    for i in board:
        for j in i:
            if j == 1:
                return True
    return False

def longueur(board):
    return len(board[0])-1

def largeur(board):
    return len(board)-1

def afficherTableau(board):
    print("\033[33m" + "  X =  0 1 2 3 4 5 6 7 8 9", end="")
    print("\033[0m", end="")
    for i in range(len(board)):
        print()
        print("\033[33m" +"Y = " + str(i) + ":", end ="\033[0m ")
        for j in range(len(board[i])):
            print("🛥️" if board[i][j] else "\033[34m~", end="\033[0m ")
    print()

def attaquer(board, x, y):
    (x,y) = (y,x)
    if(x < 0 or x >= len(board) or y < 0 or y >= len(board[0])):
        print("\033[31m" + "Coordonnées invalides !" + "\033[0m")
        return
    hit = False
    print("\033[33m" + "  X =  0 1 2 3 4 5 6 7 8 9", end="")
    for i in range(len(board)):
        print()
        print("\033[33m" +"Y = " + str(i) + ":", end ="\033[0m ")
        for j in range(len(board[i])):
            if(i == x and j == y):
                if(board[i][j] == 1):
                    print("\033[32m" + "X", end = " ")
                    board[i][j] = 0
                    hit = True
                else:
                    print("\033[31m" + str(board[x][y]), end = " ")
                print("\033[0m", end = "")
            else:
                print("🛥️" if board[i][j] else "\033[34m~", end="\033[0m ")     
    print()
    print("\033[32m" + "Touché !" + "\033[0m" if hit else "\033[31m" + "Raté !" + "\033[0m")
    print()
    
    
# \033[0m   : Reset
# \033[31m  : Red
# \033[32m  : Green