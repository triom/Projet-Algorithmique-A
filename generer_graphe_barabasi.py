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
    nouvelleArrete = []
    while m > 0:
        valeur = random.choice(noeuds)
        nouvelleArrete.append(valeur)
        # empecher que le random ne prenne la mm valeur deux fois
        noeuds.remove(valeur)
        m -= 1
    print(nouvelleArrete)

    # ajouter le nouveau graphe dans la liste de ses voisins
    nouveauNoeud = len(G)
    noeudAdj = {nouveauNoeud: nouvelleArrete}
    print(G)
    print("before append")
    print(noeudAdj)
    G.update(noeudAdj)
    print(G)
    print("after update with new adjacency list for new vertex")
    for k in range(len(nouvelleArrete)):
        G[nouvelleArrete[k]].append(nouveauNoeud)
    print(G)
    print("after update with new adjacency list for old vertices")


graphe_barabasi()
