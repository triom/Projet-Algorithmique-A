import random
G = {0: [1, 2], 1: [0, 2], 2: [0, 1]}


def graphe_barabasi():
    global G
    m = 2
    degreeInit = 6
    probabilite = m / degreeInit
    # ajouter un nouveau sommet a au graphe avec ces voisons
    noeuds = []
    for i in range(len(G)):
        noeuds.append(i)
    print(noeuds)
    while m > 0:
        # empecher que le random ne prenne la mm valeur deux fois
        nouveauSommet = random.choice(noeuds)
        noeuds.remove(nouveauSommet)  #empecher que le random ne prenne la mm valeur deux fois
        m -= 1
        print(nouveauSommet)
    # ajouter le nouveau graphe dans la liste de ses voisins
