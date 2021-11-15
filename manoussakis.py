"""
Partie III

Les deux algorithme de M. Manousakis, issue de l'article:
Manoussakis, George. "A new decomposition technique for maximal clique
enumeration for sparse graphs." Theoretical Computer Science 770 (2019): 25-33.
"""

import outils


def enum_max_clique_hash(liste):
	"""
	Liste toutes les cliques maximale, est les stokant dans une table de hachage.
	:param liste: Liste d'adjacence.
	:return: Un iterateur donnant les cliques sous forme de tableau.
	"""
	ordre = outils.genenerate_order(liste)
	liste_degenerate = outils.degenerate_liste(liste, ordre)
	deja_vu = set()
	for j in range(len(liste)):
		for k in Bron_Korsch_j(liste_degenerate, ordre, j):
			# Nous avons besoin d'un tuple pour la recherche dans deja_vu
			k = tuple(k)
			if not k in deja_vu:
				for i in range(len(k)):
					deja_vu.add(k[i:])
				yield [*k]


def enum_max_clique(liste):
	"""
	Liste toutes les cliques maximale, sans les stoker en mémoire.
	:param liste: Liste d'adjacence.
	:return: Un iterateur donnant les cliques sous forme de tableau.
	"""
	ordre = outils.genenerate_order(liste)
	liste_degenerate = outils.degenerate_liste(liste, ordre)
	for j in range(len(liste)):
		for k in Bron_Korsch_j(liste_degenerate, ordre, j):
			if len(k) == 1:
				continue
			if outils.no_exist_lower_neightbors(liste_degenerate, k, ordre, j):
				yield [*k]


def Bron_Korsch_j(liste_degenerate, ordre, j):
	"""
	Itère sur les cliques maximale de G_j
	:param liste_degenerate: Liste d'adjacence dégénéré
	:param ordre: Un tableau donnant un ordre de dégénérecence, indexé par sommet
	:param j: sommet
	:return: Un itérateur donnant un set contenant une clique.
	"""
	candidats = []
	for c in liste_degenerate[j]:
		if ordre[c] < ordre[j]:
			break
		else:
			candidats.append(c)
	yield from Bron_Korsch_aux(liste_degenerate, candidats, set([j]), set())
def Bron_Korsch_aux(liste, p, r, x):
	if len(p) == 0 and len(x) == 0:
		yield r
	for v in p:
		yield from Bron_Korsch_aux(liste, [*set.intersection(set(p), liste[v])], set.union(r, [v]), set.intersection(x, liste[v]))
		p = p[1:]
		x = x.union([v])


if __name__ == "__main__":
	# Simple graphe en diamant
	liste = [
		[1, 2],
		[0, 2, 3],
		[0, 1, 3],
		[1, 2],
	]
	exp = [[0, 1, 2], [1, 2, 3]]

	def test(f):
		out = [*f(liste)]
		if out != exp:
			print("[FAIL]", f.__name__)
			print(f"exp: {exp}")
			print(f"out: {out}")
		else:
			print("[OK]", f.__name__)

	test(enum_max_clique_hash)
	test(enum_max_clique)
