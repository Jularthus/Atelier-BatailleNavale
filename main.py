from backend import *

board = [
#0,1,2,3,4,5,6,7,8,9
[0,0,1,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0],
]

tailleX = getSizeX(board)
tailleY = getSizeY(board)

printBoard(board)

def play():
    x = int(input(f"Choissisez une coordonnée X comprise entre 0 et {tailleX} : "))
    y = int(input(f"Choissisez une coordonnée Y comprise entre 0 et {tailleY} : "))
    attack(board, x, y)
    
while(gameNotEnded(board)):
    play()

print("Partie terminée !")