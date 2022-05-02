import os
import cesaretri

def ouvre_fichier(chemin, encodage="utf8"):
	"""
		Entrée: - chemin: string, chemin vers le fichier à ouvrir
		Retourne: objet File, fichier ouvert

		Envoie une erreur si le fichier n'éxiste pas
	"""

	if os.path.exists(chemin):
		return open(chemin, "r", encoding=encodage)

	raise ValueError("file doesn't exists")

def parse_CSV(chemin, encodage="utf8"):
	"""
		Entrée: - chemin: string, chemin vers le fichier à ouvrir,
							le fichier doit être au format CSV
		Retourne: Liste de tuples au format (str, timecode)
		 où str caractérise un caractère et timecode est un flottant
	"""
	fichier = ouvre_fichier(chemin, encodage)
	data = []

	lines = fichier.readlines()
	for line in lines:
		raw = line.split(",")

		# Teste si la ligne contient bien 2 éléments	
		if len(raw) <= 1:
			continue

		# Teste si le premier caractère du second string est
		# un nombre, permet de passer le cas du header
		if ord(raw[1][1]) < 46 or ord(raw[1][1]) > 57:
			continue

		# Il faut retirer le caractère \n pour convertir
		timecode = float(raw[1].replace("\n", ""))
		item = (raw[0], timecode)

		data.append(item)

	fichier.close()
	return data

data = parse_CSV("data.csv", "utf16") # Wow ça marche


def rover_tuple(L,M):
	#Le programme n'est pas encore fini tout à fait
	# Il faut encore que je fasse une LISTE des indices de chaque mot dans les données brutes
	# L'indice renvoyé n'est que le dernier, ce qui ne fait pas tout
	"""Écrit par Daniel
	L : liste de mots que nous cherchons sous forme d'une liste de strings
	M : Données sous forme d'une liste de tuples dont le premier indice est un string
	--Permet de trouver le nombre d'occurence d'un mot ainsi que les indices où sa dernière lettre se situe--

	"""
	S = []
	c = 0
	d = 0
	for word in L:
		for k in range(len(M)-len(word)):
			for i in range(len(word)):
				if word[i] == M[k+i][0]:
					c = c+1
					if c == len(word):
						d = d+1
						c = 0
			c = 0
		S.append([word,d,i])
		c = 0
		d = 0
	return S

def big_plage(L,F = 5,S = 5):
	# Le programme n'est pas encore fini
	# Il faut que je m'occupe des exceptions dû à aux indices "out of range"
	"""Écrit par Daniel
	L est une liste de tuples dont le premier indice est un caractères
	F : Nombre de caractères avant
	S : Nombres de caractères après
	-- Affiche le voisinage
	"""
	if len(L) < S or len(L) < F:
		return "T'essaye quoi wesh"
	T = ["bonjou"]
	J = rover_tuple(T,L)
	print(J)
	P = []
	for i in range(len(J)):
		size = len(J[i][0])
		P.append([])
		if J[i][1] != 0:
			for k in range(J[i][2]-(F+size-1),J[i][2]+(S+1)):
				P[i].append(L[k][0])
	return P