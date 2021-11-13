def genenerate_order(liste):
	"""
	Calcule un ordre de dégénérecence.
	Complexité: O(m) soit proportionnelle au nombre d'arrêtes du graphe.
	:param liste: Une liste d'adjacence
	:return: pos[sommet] = indice dans l'ordre de dégénérecence

	Source: V. Batagelj, M. Zaversnik, An O (m) algorithm for cores
	decomposition of networks, CoRR, arXiv:cs .DS /0310049, 2003.
	https://arxiv.org/pdf/cs/0310049
	"""

	n = len(liste)
	deg = [len(liste[v]) for v in range(n)]
	md = max(deg)

	# Initialise bin comme un tableau countenant le nombre sommet ayant i degré.
	# bin[i] = |{v in V: degre(v) = i}|
	bin = [0] * (md+1)
	for v in range(n):
		bin[deg[v]] += 1
	# (A) bin devient un tableau référençant le début des sommets dans vert
	# ayant i degré.
	# bin[i] = v où degree[v] = i
	start = 0
	for d in range(md+1):
		num = bin[d]
		bin[d] = start
		start += num
	# Initialise les tableaux vert et pos
	pos = [None] * n # pos[sommet] = ordre
	vert = [None] * n # vert[ordre] = sommet
	for v in range(n):
		pos[v] = bin[deg[v]]
		vert[pos[v]] = v
		bin[deg[v]] += 1
	# Remet bin dans l'état (A)
	for d in range(md, 1, -1):
		bin[d] = bin[d-1]
	bin[0] = 0

	# La décomposition elle-même.
	for v in vert:
		for u in liste[v]:
			if deg[u] > deg[v]:
				# Si u n'est pas le premier sommet ayant deg[u] degré,
				# alors échange u avec le premier élément qui est w.
				du = deg[u]
				pu = pos[u]
				pw = bin[du]
				w = vert[pw]
				if u != w:
					pos[u] = pw
					vert[pu] = w
					pos[w] = pu
					vert[pw] = u
				# Décrémente le degré de u.
				bin[du] += 1
				deg[u] -= 1

	return pos


def degenerate_liste(liste, ordre):
	"""
	Prend une liste de d'adjacence et un ordre de dégénérescence
	(indexé par les sommets), retourne une liste d'adjacence dégénérée.
	:param liste: Liste d'adjacence
	:param ordre: Ordre de dégénérescence, indexé par les sommets.
	:return: Liste d'adjacence dégénérée
	"""
	degenerateListe = []
	for v in range(len(liste)):
		ordreDeV = ordre[v]
		voisins = []
		for voisin in liste[v]:
			if ordreDeV < ordre[voisin]:
				voisins.append(voisin)
		for voisin in liste[v]:
			if ordre[voisin] < ordreDeV:
				voisins.append(voisin)
		degenerateListe.append(voisins)
	return degenerateListe
 
