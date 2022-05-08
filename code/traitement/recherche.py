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




#Listes de test
if __name__ == "__main__":
	S = parse_data('sauvegarde_locale.csv')
	S = fine(S)
	S = fine_accent(S)
	S = fine_backspace(S)
