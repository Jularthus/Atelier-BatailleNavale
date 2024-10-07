from colorama import Fore

board_size = 10
board = [['O' for _ in range(board_size)] for _ in range(board_size)]

def play(board):
    count = 0
    for i in board:
        for j in i:
            if j == 1:
                count+=1
    
    hit = 0
    while hit<count:
        while True:
            try:
                x = int(input("Indiquez la coordonnée X : "))
                if(x >= 0 and x < len(board[0])):
                    break
            except:
                print("Mauvaise donnée entrée ! N'écris qu'un chiffre compris entre 0 et {}".format(len(board[0])))
        while True:
            try:
                y = int(input("Indiquez la coordonnée Y : "))
                if(y >= 0 and y < len(board)):
                    break
            except:
                print("Mauvaise donnée entrée ! N'écris qu'un chiffre compris entre 0 et {}".format(len(board)))
        
        if(board[y][x]):
            print("Touché !")
            board[y][x] = 0
            print(Fore.GREEN)
            for i in len(board):
                for j in len(i):
                    if(i == y and j == x):
                        print(Fore.RED + 0)
            hit+=1
        else:
            print(Fore.GREEN)
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if(i == y and j == x):
                        print(Fore.RED + str(board[y][x]))
                    else:
                        print(board[j][i], end=" ")
            print("Raté !")
            
            

def place_ships(player):
    print(f"Joueur {player}: Positionne tes bateaux.")
    for ship in range(5):
        while True:
            try:
                row = int(input(f"Ligne du bateau {ship+1}: "))
                col = int(input(f"Colonne du bateau {ship+1}: "))
                if board[row][col] == 'O':
                    board[row][col] = 'S'
                    break
                else:
                    print("Cette position est déjà occupée. Réessaye.")
            except ValueError:
                print("Entrée invalide. Réessaye.")

def take_shot(player):
    print(f"Joueur {player}, à ton tour!")
    while True:
        try:
            row = int(input("Entrer la ligne: "))
            col = int(input("Entrer la colonne: "))
            if board[row][col] == 'O':
                print("Raté!")
                board[row][col] = 'X'
                break
            elif board[row][col] == 'S':
                print("Touché!")
                board[row][col] = 'H'
                break
            else:
                print("Tu as déjà tiré ici. Réessaye.")
        except ValueError:
            print("Entrée invalide. Réessaye.")


def gameNotEnded(board):
    for i in board:
        for j in i:
            if j == 1:
                return True
    return False

def attack(board, x, y):
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