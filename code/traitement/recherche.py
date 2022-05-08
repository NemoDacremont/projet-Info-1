from refine import *

#Global 
top12K = extract(parse_CSV('top12K.csv'), 0)

def rover_tuple(L,M):
	"""Ecrit par Daniel
	L est une liste de string et M est une liste de tuples dont le premier indice est un string"""
	S = []
	c = 0
	d = 0
	for word in L:
		for k in range(len(M)-len(word)):
			for i in range(len(word)):
				if word[i] == M[k+i][0] or dict_str[M[k+i]] == word[i]:
					c = c+1
					if c == len(word):
						d = d+1
						c = 0
			c = 0
		S.append([word,d])
		c = 0
		d = 0
	return S

def brute_force(liste, liste_de_mots):
	"""
		Entrée: - liste: liste de tuples au format ('c', timecode) avec 'c' un caractère et timecode un float
						- liste_de_mots: une liste de string, chaque string correspond à un mot

		Retourne: un dictionnaire avec comme clef les mots trouvés et pour valeurs le nombre d'occurences

		La fonction bruteforce parcourt la liste pour trouver toutes les occurences des mots contenus dans liste_de_mots
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

#Listes de test
if __name__ == "__main__":
	S = parse_data('sauvegarde_locale.csv')
	S = fine(S)
	S = fine_accent(S)
	S = fine_backspace(S)
