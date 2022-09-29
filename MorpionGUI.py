from tkinter import *
from random import randint

grille = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

boutons = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]


#Fenêtre de base
fenetre = Tk()
fenetre.title('Morpion')

def logique_jeu(l, c):
    mouvements = 0
    gagnant = gagne(mouvements)
    #Placement des pions
    if libre(l, c) == True and gagnant == False: #Vous
        grille[l][c] = "X"
        boutons[l][c].configure(text = "X")
        mouvements += 1
        gagnant = gagne(mouvements)
    elif libre(l, c) == False and gagnant == False:
        return None
    
    ai_player() #Ordinateur
    gagnant = gagne(mouvements)
    mouvements += 1

def libre(l, c):
    #Vérifie si la case est libre
    return grille[l][c] == " "

def ai_player():
    #Joueur automatique
    ligne = randint(0, 2)
    case = randint(0, 2)
    if libre(ligne, case) == True:
        grille[ligne][case] = "O"
        boutons[ligne][case].configure(text = "O")
    elif libre(ligne, case) == False:
        ai_player()

def gagne(m):
    #Vérifie si les conditions de victoires sont réunies
    #et pour quel joueur, retourne le gagnant
    gagnant = " "
    #Lignes horizontales:
    for ligne in grille:
        if ligne == ["X", "X", "X"]:
            gagnant = "Vous !"
        elif ligne == ["O", "O", "O"]:
            gagnant = "Ordinateur !"

    #Lignes verticales:
    ligne_vert = [[ligne[0] for ligne in grille], [ligne[1] for ligne in grille], [ligne[2] for ligne in grille]]
    for ligne in ligne_vert:
        if ligne == ["X", "X", "X"]:
            gagnant = "Vous !"
        elif ligne == ["O", "O", "O"]:
            gagnant = "Ordinateur !"

    #Diagonales:
    diago = [[grille[0][0], grille[1][1], grille[2][2]], [grille[0][2], grille[1][1], grille[2][0]]]
    for ligne in diago:
        if ligne == ["X", "X", "X"]:
            gagnant = "Vous !"
        elif ligne == ["O", "O", "O"]:
            gagnant = "Ordinateur !"

    #Match nul:
    if m == 8:
        gagnant = "Aucun, match nul !"
    
    #Fenêtre de victoire:
    if gagnant != " ":
        for widget in fenetre.winfo_children():
            widget.destroy()
        annonce = "Gagnant : " + gagnant
        texte = Text(fenetre, height=20)
        texte.grid()
        texte.insert(1.0, annonce)

    #Aucune condition remplie
    return False

#Zone de jeu
for i in range(3):
    for j in range(3):
        boutons[i][j] = Button(master=fenetre,
                                height=5, width=10,
                                command = lambda l=i, c=j : logique_jeu(l, c))
        boutons[i][j].grid(row = i, column = j)


fenetre.mainloop()
