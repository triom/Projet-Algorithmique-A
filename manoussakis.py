"""
Partie III

Les deux algos de M. Manousakis, issue de l'article:
Manoussakis, George. "A new decomposition technique for maximal clique
enumeration for sparse graphs." Theoretical Computer Science 770 (2019): 25-33.
"""

import outils


def enum_max_clique_no_store(liste):
	"""
	Liste toutes les cliques maximale, sans les stoké en mémoire (deuxième
	algorithme de l'aticle).
	:param liste: Liste d'adjacence
	"""
	yield NotImplemented


if __name__ == "__main__":
	# Simple graphe en diamant
	liste = [
		[1, 2],
		[0, 2, 3],
		[0, 1, 3],
		[1, 2],
	]
	exp = [[0, 1, 2], [1, 2, 3]]

	# Test algo 2
	out = [*enum_max_clique_no_store(liste)]
	if out != exp:
		print("[FAIL] enum_max_clique_no_store")
		print(f"exp: {exp}")
		print(f"out: {out}")
	else:
		print("[OK] enum_max_clique_no_store")
