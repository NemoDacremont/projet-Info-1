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
				if word[i] == M[k+i][0] or refine.dict_str[M[k+i]] == word[i]:
					c = c+1
					if c == len(word):
						d = d+1
						c = 0
			c = 0
		S.append([word,d])
		c = 0
		d = 0
	return S

#Listes de test

S = parse_data('sauvegarde_locale.csv')
S = fine(S)
S = fine_accent(S)
S = fine_backspace(S)