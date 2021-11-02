import random


def generer_graphe():
    nombreSommets = int(input("Donnez un nombre de sommets\t"))
    graphe_aleatoire = [
        [0 for i in range(nombreSommets)]for j in range(nombreSommets)]
    print(str(graphe_aleatoire))
    # for i in range(0, nombreSommets):
    #     for j in range(0, nombreSommets):
    #         valeurProbilite = random.random()
    #         if (i != j) and valeurProbilite > 0.2:
    #             print(valeurProbilite)
    #             graphe_aleatoire = [[i]]
    #             # print(i)
    #             # print(j)
    #         else:
    #             print("valeur inferieur")
    #             print(valeurProbilite)

    # reste a stocker les graphes et afficher soit la liste d'adjacence ou la matrice
