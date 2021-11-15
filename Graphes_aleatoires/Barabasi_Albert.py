# import timeit
# import random

# def Barabasi_Albert():
#     #initialisation du graphe triangle sous forme de listes d'adjacence
#     graphe = {0: [1, 2], 1: [0, 2], 2: [0, 1]}

#     #variable initialisé au nombre de degrés du graphe initial
#     sommeDegres = 6

#     #recuperation du nombre de noeuds qu'on souhaite rajouter au graphe
#     n = input("Entrez le nombre de noeuds à ajouter : ")
#     noeuds = int(n)

#     #recuperation du nombre d'arêtes qu'on souhaite rajouter au graphe
#     arêtes = input("Entrez le nombre d'arêtes que vous souhaitez rajouter : ")
#     while int(arêtes) > 3:
#         arêtes = input(
#             "Entrez le nombre d'arêtes que vous souhaitez rajouter : ")
#     m = int(arêtes)
#     print("Le graphe initial est : ", graphe)

#     #on parcourt le nombre de noeuds qu'on souhaite rajouter
#     for i in range(noeuds):
#         k = 0
#         print("La somme des degrés est : ", sommeDegres, "\n")

#         #on recupère la liste des noeuds du graphe existant pour pouvoir choisir aléatoirement celui auquel on rajoutera une arête entre lui et le(les) noeud(s) qu'on va rajouter
#         listeNoeuds = list(graphe.keys())
#         print("La liste des noeuds du graphe est : ", listeNoeuds)

#         #on crée une liste de liste qui contiendra les noeuds qui auront été selectionnés aléatoirement pour pouvoir créer la liste des voisins du(des) noeud(s) qui seront rajoutés
#         listeNoeudsSelectionnes = []

#         #on choisit aléatoirement le nombre d'arêtes à rajouter entre 1 et le nombre d'arêtes entré au départ
#         nombreAretesRajoutees = random.randint(1, m)
#         print("Le nombre d'arêtes à rajouter est : ", nombreAretesRajoutees,
#               "\n")

#         #on fait une boucle tant que (où le k est initialisé à 1) qui nous permettra de ne pas mettre deux fois le même noeud dans la liste des noeuds selectionnés ; lorsque le noeud choisit aléatoirement sera déjà ajouté dans la liste, le k restera égal à lui même dans le cas contraire il s'incrémentera de 1
#         while k < nombreAretesRajoutees:
#             noeudSelectionne = random.choice(listeNoeuds)
#             if noeudSelectionne not in listeNoeudsSelectionnes:
#                 listeNoeudsSelectionnes.append(int(noeudSelectionne))
#                 #on met à jour les noeuds qui auront pour voisin le noeud qu'on va rajouter
#                 graphe[int(noeudSelectionne)].append(i + 3)
#                 print("Noeud selectionné : ", noeudSelectionne)
#                 print("Arête créée entre", i + 3, " et ",
#                       int(noeudSelectionne))
#                 print("Avec une probabilité de : ",
#                       nombreAretesRajoutees / sommeDegres, "\n")
#                 k += 1
#             else:
#                 print("Le noeud refusé est : ", noeudSelectionne)
#                 k = k
#                 print("k vaut : ", k, "\n")

#         print("La liste des noeuds selectionnés est : ",
#               listeNoeudsSelectionnes, "\n")

#         #on ajoute au graphe le noeud à rajouter ainsi que sa liste de voisins
#         graphe.update({i + 3: listeNoeudsSelectionnes})
#         print("Le nouveau graphe est : ", graphe, "\n")

#         #on met à jour la somme des degrés du nouveau graphe
#         sommeDegres += nombreAretesRajoutees * 2
#         print("La nouvelle somme des degrés est : ", sommeDegres, "\n")
#         print("****************************************\n")

#     return graphe

# graphe = Barabasi_Albert()

# def listeEnMatrice(g):
#     #recuperer le temps de début
#     temps_debut = timeit.timeit()

#     matrice = []

#     #recuperation des noeuds dans une liste du graphe généré par la fonction Barabasi_Albert et de la taille de cette liste
#     listeNoeuds = list(g.keys())
#     taille = len(listeNoeuds)

#     #initialisation d'une matrice vide
#     for i in range(taille):
#         matrice = matrice + [[]]
#         for j in range(taille):
#             matrice[i] = matrice[i] + [0]

#     #mise à jour de la matrice à l'aide de la nouvelle liste de voisins générée par la fonction Barabasi_Albert
#     for i in listeNoeuds:
#         listeVoisins = list(g[i])
#         for j in listeVoisins:
#             matrice[i][j] = 1

#     return matrice
#     print("La matrice du graphe généré par barabasi est : ", matrice, "\n")

#     temps_fin = timeit.timeit()
#     print("Temps d'éxecution--- %s seconds ---" % (temps_fin - temps_debut))

# listeEnMatrice(graphe)
