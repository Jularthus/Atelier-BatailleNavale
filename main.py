from backend import *

board = [
[0,0,1,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0],
]

def play():
    x = int(input(f"Choissisez une coordonnée X comprise entre 0 et {len(board[0])-1} : "))
    y = int(input(f"Choissisez une coordonnée Y comprise entre 0 et {len(board)-1} : "))
    
    attack(board, x, y)
    
while(gameNotEnded(board)):
    play()

print("Partie terminée !")