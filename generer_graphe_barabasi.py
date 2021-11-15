import random

G = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

noeudChoisis = []


def graphe_barabasi():
    #faire appel au graphe de depart
    global G

    #Mettre le degré total à zero
    degreeTotal = 0
    # prendre le nombre de noeuds à rajouter
    numNouveauNoeuds = int(input("Combien de noeud rajouter\t"))
    # recuperer m
    m = int(input("Combien d'arretes creér par sommet\t"))

    #recuperer le dégre total du graphe avant modification
    for value in G.items():
        degreeTotal += len(value)
    print('Degré total du graphe avant modif: ', degreeTotal)

    #faire une boucle pour rajouter les noeuds
    for i in range(numNouveauNoeuds):
        global noeudChoisis
        # faire une liste des noeuds actuellement présents dans le graphes
        noeudsActuel = []
        for i in range(len(G)):
            noeudsActuel.append(i)
        print(noeudsActuel)
        print('Nombre de noeuds actuel', len(noeudsActuel))

        #se rassurer a chaque fois que ce n'est pas plus grand quee le nombre de noeuds que nous avons
        while m > len(noeudsActuel):
            m = int(
                input(
                    "Donnez un nombre d'arretes inferieur au nombre de noeuds\t"
                ))

        #choisir les neouds sur lesquels seront rajoutés les arretes avec le(s) nouveau(x) noeuds
        s = 0
        while s < m:
            valeur = random.choice(noeudsActuel)  #faire un choir aléatoir
            noeudChoisis.append(valeur)
            # empecher que le random ne prenne la mm valeur deux fois
            noeudsActuel.remove(valeur)
            m -= 1
            print('Noeud auquel rajouter les arretes', noeudChoisis)
            s += 1

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
        print('Graphe initial\n', G)
        print('Liste des voisons du nouveau noeud\n', noeudAdj)

        #rajouter la liste d'adjacence du nouveau noeud au graphe
        G.update(noeudAdj)

        # Faire la mise a jour des liste d'adjacence des noeuds liés au nouveau neoud
        for k in range(len(noeudChoisis)):
            G[noeudChoisis[k]].append(nouveauNoeud)
        print('Graphe final après rajout du noeud', nouveauNoeud, '\n', G)

    noeudChoisis.clear()
    #recuperer le dégre total du graphe après modification
    degreeTotal = 0
    for key, value in G.items():
        degreeTotal += len(value)
    print('Degré total du graphe après modif: ', degreeTotal)


graphe_barabasi()
