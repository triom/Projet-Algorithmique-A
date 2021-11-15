from outils import generate_order
from outils import degenerate_liste

def create_Gi(liste, i):
	"""
	prend une liste d'adjacence et un numéro de sommet, retourne la liste d'adjacence du graphe induit Gi = G[N[Vi] inter Vi]
	"""
	rep = []
	for j in range(len(liste) - i):
		rep.append([])
		for k in range(len(liste[j + i])):
			if liste[j + i][k] >= i:
				rep[j].append(liste[j + i][k] - i)
	return rep

def isNeighborsInGwithLowerRankThanVjAdjacentToAllInK(vertex, rank, listeDegeneree, K):
	rep = False
	for i in range(len(K)):
		Adjacence = True
		for j in range(len(listeDegeneree)):
			if j > rank:
				if K[i] not in listeDegeneree[j]:
					if j in listeDegeneree[vertex]:
						Adjacence = False
		if Adjacence:
			rep = True
	return rep
		
	

def Manoussakis(liste):
	"""
	prend une liste d'adjacence, retourne la liste des cliques maximales 
	"""
	rep = []
		ordre = generate_order(liste)
		listeDegeneree = degenerate_liste(liste, ordre)
		for j in range(len(listeDegeneree)):
			newListe = create_Gi(liste, j + 1)
			potentielles = Manoussakis(newListe)
			for k in range(len(potentielles)):
				validee = True
				for x in range(len(potentielles[k])):
					if isNeighborsInGwithLowerRankThanVjAdjacentToAllInK(x, j, listeDegeneree, potentielles[k]):
						validee = False
				if validee :
					rep.append(potentielles[k])
	return rep

liste = [[1], [0,2], [1,3], [2]]
ordre = generate_order(liste)
print(ordre)
liste2 = degenerate_liste(liste, ordre)
print(liste2)
liste3 = create_Gi(liste2, 0)
liste4 = Manoussakis(liste)
print(liste4)
