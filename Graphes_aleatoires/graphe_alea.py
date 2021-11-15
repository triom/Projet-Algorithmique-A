import timeit
import random


def generer_graphe_aleatoire_aux(nombreSommets):
    #initialiser notre matrice vide
    graphe_aleatoire = [[0 for i in range(nombreSommets)]
                        for j in range(nombreSommets)]
    #boucler sur
    for i in range(0, nombreSommets):
        for j in range(0, nombreSommets):
            #generer une probabilité aleatoire entre 0 et 1 pour obtenir notre graphe aléatoire
            valeurProbilite = random.random()
            #ne prendre que des probabilités superieurs a 0.1
            if (i != j) and valeurProbilite > 0.1:
                #assigné la valeur 1 aux voisins de chaque sommet dans le graphe
                graphe_aleatoire[i][j] = 1
            else:
                break
    # afficher la matrice d'adjacence
    for i in range(len(graphe_aleatoire)):
        print(graphe_aleatoire[i])

    # afficher la matrice d'adjacence 
    for i in range(0, nombreSommets):
        print("[", i, "]")


def generer_graphe_aleatoire():
    #recuperer le temps de début
    temps_debut = timeit.timeit()
    #recuperer le nombre de sommets
    n = int(input("Donnez un nombre de sommets\t"))
    generer_graphe_aleatoire_aux(n)
    temps_fin = timeit.timeit()
    print("Temps d'éxecution--- %s seconds ---" % (temps_fin - temps_debut))
