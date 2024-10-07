from colorama import Fore


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
                    print(Fore.GREEN + "X", end = " ")
                    board[i][j] = 0
                    hit = True
                else:
                    print(Fore.RED + str(board[y][x]), end = " ")
                print(Fore.RESET, end = "")
            else:
                print(board[i][j], end=" ")     
    print()
    print(Fore.GREEN + "Touché !" + Fore.RESET if hit else Fore.RED + "Raté !" + Fore.RESET)
    print()