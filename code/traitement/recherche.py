from refine import *
from itertools import product

def trouve(S, liste_de_mots, erreur, premier = False):
	"""Ecrit par Daniel
	Arguments :
		- S est une liste de tuples dont le premier élément est un str
		- liste_de_mots est une liste de str contenant les mots à chercher
		- erreur : entier positif indiquant le nombre de lettres fausses tolérées dans le mot pour le compter correct
		
	Retourne un dictionnaire au format {mot : [positions]}, avec [position[ la liste des indices des occurences du mot
																								
	Nota Bene : il est suggéré d'avoir traité S avant"""
	for word in liste_de_mots:
		e = len(word) - erreur
		#Evite les problèmes si le mot est plus court que l'erreur autorisée
		if e <= 0 :
			e = 1
		indices = []
		for k in range(len(S)-len(word) + 1):
			for i in range(len(word)):
				if word[i] == S[k+i][0] :
					c = c+1
				elif i == 0 and not premier :
					break
				if c >= e :
					indices.append(k)
					break
			c = 0
		L.append((word,indices))
		c = 0
	L = dict(L)
	return L

def brute_force(liste, liste_de_mots):
	"""
		Entrée: - liste: liste de tuples au format ('c', timecode) avec 'c' un caractère et timecode un float
						- liste_de_mots: une liste de string, chaque string correspond à un mot

		Retourne: un dictionnaire avec comme clef une contenant l'indice du premier caractère du mot de passe

		La fonction bruteforce parcourt la liste pour trouver toutes les occurences des mots contenus dans liste_de_mots

		>>> brute_force([['1', 1], ['2', 1], ['3', 2], ['4', 2], ['5', 1], ['6', 4]])
		{ "123456": [1] }
	"""
	mots_trouves = {}

	for mot in liste_de_mots:
		for i in range(len(liste)):
			mot_trouve = True
			for j in range(len(mot)):
				if liste[i+j][0] != mot[j]:
					mot_trouve = False
					break
				
			if mot_trouve:
				if mot in mots_trouves.keys():
					mots_trouves[mot].append(i)
				else:
					mots_trouves[mot] = [i]

		return mots_trouves

def plage(S, indices, apres, avant = 0) :
	
	"""
	Arguments :
		- S : Liste dans laquelle rechercher
		- indices : liste d'indices à rechercher dans S. S'il n'y a qu'un indice, peut être un int
		- apres : entier, nombre d'éléments à retourner après chaque indice ciblé
		- avant (optionnel, par défaut 0) : entier, nombre d'éléments à retourner avant chaque indice ciblé
			
	Renvoie une liste des plages trouvées.
	
	Permet de rechercher dans une liste des plages d'éléments autour d'indices précis, avec une largeur paramétrable.
	
	Remarque : si tous les indices sont bien liés à des éléments de la liste, le programme peut adapter seul la taille des plages si celles-ci dépassent les capacités de la liste.
	
	plage([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [1, 7], apres = 3, avant = 3)
	>>> [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
	"""
	plages = [0 for i in range(len(indices))]
	
	#Permet d'utiliser un seul indice plutô qu'une liste
	if type(indices) in [int, float] :
		indices = [int(indices)]
		
	for i in range(len(indices)) :
		debut = indices[i] - avant
		fin = indices[i] + apres + 1
		#Pas de risque de dépassement
		if debut < 0 :
			debut = 0
		if fin > len(S) :
			fin = len(S)
		
		plages[i] = S[debut : fin]
		
	return plages

def target(S, cible, erreur, premier = False) :
	
	"""
	Arguments :
		- S : liste de tuples au format (str, float)
		- cible : str
		erreur = entier positif ou nul
		premier (optionnel) :  booléen, par défaut False
		
	Ressort un dictionnaire au format {cible : [positions]}
	
	target permet de rechercher toutes les occurences de la cible dans la liste S.
	Erreur indique le nombre de caractères manquants tolérés. Par exemple, si cible = 'king' et erreur = 1, alors 'kin', 'kng' ou encore 'ing' sont tolérés
	Si premier est spécifié, tolère également que la première lettre soit différente de la première lettre de cible.
	
	Remarque : la complexité du calcul s'acroît de manière factorielle par rapport à erreur. De plus, plus l'erreur est élevée, plus le programme a de chances de trouver de fausses occurences de cible.
	"""
	
	def combinaisons(k, n) : #Extraire toutes les combinaisons de k éléments parmi n, sans répétition
		if k == 0:
			return[[]]
		elif k == 1 :
			L = [[i] for i in range(0, n)]
			return L
		elif k == n:
			return [list(range(0, n))]
		else :
			L1 = combinaisons(k - 1, n - 1)
			for i in range(len(L1)) :
				L1[i] = L1[i] + [n - 1]
			return L1 + combinaisons(k, n - 1)
	
	n = len(cible)
	e = n - erreur
	#Récupérer les combinaisons possibles
	cibles = combinaisons(e, n)
	n = len(cibles)
	for j in range(n):
		item = ''
		for i in cibles[j] :
			item += cible[i]
		cibles[j] = item
		
	if not premier :
		for word in cibles :
			if word[0] != cible[0] :
				cibles.remove(word)
	
	return brute_force(S, cibles)

#Listes de test
if __name__ == "__main__":
	S = parse_data('sauvegarde_locale.csv')
	S = fine_str(S)
	S = fine(S)
	S = fine_accent(S)
	#