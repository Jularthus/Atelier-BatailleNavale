from main import *

board = [
[0,0,1,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0],
]

def play():
    x = int(input("Choissisez une coordonnée X : "))
    y = int(input("Choissisez une coordonnée Y : "))
    
    attack(board, x, y)
    
while(gameNotEnded(board)):
    play()

print("Partie terminée !")