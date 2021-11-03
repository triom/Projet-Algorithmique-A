import random


def generer_graphe():
    #nombreSommets = int(input("Donnez un nombre de sommets\t"))
    nombreSommets = 3
    graphe_aleatoire = [
        [0 for i in range(nombreSommets)]for j in range(nombreSommets)]
    for i in range(0, nombreSommets):
        for j in range(0, nombreSommets):
            valeurProbilite = random.random()
            if (i != j) and valeurProbilite > 0.2:
                graphe_aleatoire[i][j] = 1
            else:
                break
    for i in range(len(graphe_aleatoire)):
        print(graphe_aleatoire[i])

    # reste a stocker les graphes et afficher soit la liste d'adjacence ou la matrice
generer_graphe()
