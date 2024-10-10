from backend import *

# On initialise le tableau de jeu, 0 est vide, 1 est un bateau
tableau = [
#0,1,2,3,4,5,6,7,8,9
[0,0,1,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,0,0,0,0,0],
]

# On récupère la taille du tableau de jeu
longueur = longueur(tableau)
largeur = largeur(tableau)

# On l'affiche une première fois pour commencer le jeu
afficherTableau(tableau)

# On demande au joueur de choisir des coordonnées, puis on attaque la case correspondante
def play():
    y = int(input(f"Choissisez une coordonnée Y comprise entre 0 et {largeur} : "))
    x = int(input(f"Choissisez une coordonnée X comprise entre 0 et {longueur} : "))
    attaquer(tableau, x, y)
    
# On fait une boucle pour continuer à jouer tant que la partie n'est pas terminée
while(jeuEnCours(tableau)):
    play()

# Une fois la boucle terminée, le jeu est fini, on affiche un message de fin
print("Partie terminée !")