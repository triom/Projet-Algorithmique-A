import random
from Barabasi_Albert import Barabasi_Albert
from Barabasi_Albert import listeEnMatrice

class monGraphe:
	def __init__(self, size) :
		i = 0
		j = 0
		self.size = size
		self.matrice = []
		for i in range(size):
			self.matrice = self.matrice + [[]]
			for j in range(size):
				self.matrice[i] = self.matrice[i] + [0]

def voisins(v, graphe) :
    listeVoisins = []
    for i in range(len(graphe[0])) :
       if graphe[v][i] == 1 :
           listeVoisins.append(i)
    return listeVoisins

def maxVoisins(liste, graphe) :
    listeSommets = [0 for i in range(len(graphe[0]))]
    for i in liste:
        s = 0
        for j in range(len(graphe[0])):
            s += graphe [i][j]
        listeSommets[i] = s
    return listeSommets.index(max(listeSommets))

def supprimeSommets(liste1, liste2):
	print("Je suis liste1 ", liste1)
	print("Je suis liste2 ", liste2)
	for i in liste2 :
		print("Je suis i ", i)
		print("Je suis liste 1", liste1 )
		if i in liste1 :
			liste1.remove(i)
			print("Je suis la nouvelle liste1 ", liste1)
			print("Je suis la nouvelle liste2 ", liste2, "\n")
	return liste1

def Bron_Kerbosch(R, P, X, G, rep = []):
	if len(P) == 0 and len(X) == 0:
		rep.append(R)
	else :
		for i in P[:]:
			nouvR = R[:] + [i]
			nouvP = list(set(P).intersection(voisins(i,G)))
			nouvX = list(set(X).intersection(voisins(i,G)))
			Bron_Kerbosch(nouvR, nouvP, nouvX, G, rep)
			P.remove(i)
			X.append(i)
	return rep

def Bron_Kerbosch2(R, P, X, G, rep=[]):
	if len(P) == 0 and len(X) == 0:
		rep.append(R)
	else :
		copieP = P[:]
		u = maxVoisins(list(set().union(copieP,X)), G)
		PX = supprimeSommets(copieP, voisins(u,G))
		for i in PX :
			nouvR = R[:] + [i]
			nouvP = list(set(P).intersection(voisins(i,G)))
			nouvX = list(set(X).intersection(voisins(i,G)))
			Bron_Kerbosch2(nouvR, nouvP, nouvX, G, rep)
			P.remove(i)
			X.append(i)
	return rep

R = []
P = []
X = []
Gprime = Barabasi_Albert()
G = monGraphe(len(Gprime))
G.matrice = listeEnMatrice(Gprime)
for i in range(G.size):
	P = P + [i]
sommetsAtraiter = P[:]
for rep in Bron_Kerbosch2(R, P, X, G.matrice):
    print("\nUne clique maximale est : ", rep, "\n")
