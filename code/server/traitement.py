
import os

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
		if ord(raw[1][1]) < 48 or ord(raw[1][1]) > 57:
			continue

		# Il faut retirer le caractère \n pour convertir
		timecode = float(raw[1].replace("\n", ""))
		item = (raw[0], timecode)

		data.append(item)

	fichier.close()
	return data

print(parse_CSV("data.csv", "utf16")) # Wow ça marche

