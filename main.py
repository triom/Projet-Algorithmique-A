from Graphes_aleatoires.graphe_alea import generer_graphe_aleatoire
from Graphes_aleatoires.Barabasi_Albert import Barabasi_Albert

if __name__ == "__main__":
    print("-> Generation des graphes aleatoire\n")
    print("\t1:-> Generer de façon standard\n")
    print("\t2:-> Generer par Barabasi\n")
    print("-> Enumération des cliques avec L'algorithme de Bron Kerbosch\n")
    print("\t3:-> Version standard\n")
    print("\t4:-> Version améliorée\n")
    print("-> Amelioration énumération des cliques Partie 3\n")
    print("\t5:->Algo 1\n")
    print("\t6:-> Algo 2\n")
    print("7:-> Quitter\n")
    choix = int(input("Votre choix:\t"))
    if choix == 1:
        generer_graphe_aleatoire()
    elif choix == 2:
        print("barabasi")
    elif choix == 3:
        print("cliques standars")
    elif choix == 4:
        print("cliques améliorée")
    elif choix == 5:
        print("Algo 1")
    elif choix == 6:
        print("Algo 2")
    else:
        quit()