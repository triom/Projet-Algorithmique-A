import random

G = {0: [1, 2], 1: [0, 2], 2: [0, 1]}


def graphe_barabasi():
    global G
    numNouveauNoeuds = int(input("Combien de noeud rajouter\t"))
    degreeTotal = 6
    # ajouter un nouveau sommet a au graphe avec ces voisons
    noeudsActuel = []
    for i in range(len(G)):
        noeudsActuel.append(i)
    print(noeudsActuel)
    # recuperer m et se rassurer a chaque fois que ce n'est pas plus grand quee le nombre de noeuds que nous avons
    m = int(input("Combien d'arretes creér par sommet\t"))
    while m > len(noeudsActuel):
        m = int(input("Combien d'arretes creér par sommet à rajouter\t"))

    noeudChoisis = []
    for i in range(numNouveauNoeuds):
        while m > 0:
            valeur = random.choice(noeudsActuel)
            noeudChoisis.append(valeur)
            # empecher que le random ne prenne la mm valeur deux fois
            noeudsActuel.remove(valeur)
            m -= 1
        print('Noeud auquel rajouter les arretes', noeudChoisis)

        # compter le degrée de chaque neoud
        for key, value in G.items():
            if key in noeudChoisis:
                print('Noeud: ', key, 'degré: ', len(value))
                probaRajoutArrete = len(value) / degreeTotal
                print('les arretes de', key, 'sont rajoutes avec proba: ',
                      probaRajoutArrete)

        # ajouter le nouveau graphe dans la liste de ses voisins
        nouveauNoeud = len(G)
        noeudAdj = {nouveauNoeud: noeudChoisis}
        print(G)
        print("before append")
        print(noeudAdj)
        G.update(noeudAdj)
        print(G)
        print("after update with new adjacency list for new vertex")
        for k in range(len(noeudChoisis)):
            G[noeudChoisis[k]].append(nouveauNoeud)
        print(G)
        print("after update with new adjacency list for old vertices")
        # update the graphe all the time and display


graphe_barabasi()
