import os

#Module écrit par Nemo et relu par Anaël

def ouvre_fichier(chemin, encodage="utf8"):
	"""
		Entrée: - chemin: string, chemin vers le fichier à ouvrir
		Retourne: objet File, fichier ouvert

		Envoie une erreur si le fichier n'éxiste pas
	"""

	if os.path.exists(chemin):
		return open(chemin, "r", encoding=encodage)

	raise ValueError("file doesn't exists")

def parse_CSV(chemin, encodage="utf8", separator=","):
	"""
		Entrée: - chemin: string, chemin vers le fichier à ouvrir,
							le fichier doit être au format CSV
						- encodate: string, caractérise l'encodage du fichier
						- separator: séparateur utilisé dans le fichier CSV

		Retourne: Liste de listes des éléments
		 où str caractérise un caractère et timecode est un flottant
         
        Remarque : si la commande renvoie Error : list index out of range, essayez de mettre en argument separator = ';'.
        Il arrive que les csv se fassent en utilisant , ou ; comme séparateur
	"""
	fichier = ouvre_fichier(chemin, encodage)
	data = []

	lines = fichier.readlines()
	for line in lines:
		raw = line.split(separator)

		# on retire le caractère newline
		raw[-1] = raw[-1].replace("\n", "")

		data.append(raw)

	fichier.close()
	return data

def parse_data(chemin, encodage="utf8", separator=",", has_header=False):
	"""
		Entrée: - chemin: string, chemin vers le fichier à ouvrir qui doit être
							un fichier CSV au format: 'valeur,timecode' avec timecode un flottant
						- encodate: string, caractérise l'encodage du fichier
						- separator: séparateur utilisé dans le fichier CSV
						- has_header: booléen caractérisant la présence de header dans le fichier à ouvrir

		Retourne: Liste de listes au format [str, timecode] où str caractérise un caractère et 
							timecode est un flottant, à noter que le header est retiré de la liste
	"""
	data = parse_CSV(chemin, encodage, separator)

	# Retire le header du fichier si le fichier en a un
	if has_header:
		data.pop(0)

	# convertit les timecode en float
	for i in range(len(data)):
		data[i][1] = float(data[i][1])
	
	return data