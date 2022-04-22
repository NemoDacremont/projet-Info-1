
def data_to_string(data, separator=","):
	"""
		Entrée: - data: au format de liste de listes correspondant à des données CSV
						- separator: string du séparateur 
		Retourne: string au format CSV de data
	"""
	# liste des lignes du fichier
	tmp = []
	for i in range(len(data)):
		# Stocke les données avant de les concaténées avec un séparateur
		a = []
		for j in range(len(data[i])):
			a.append(str(data[i][j]))

		tmp.append(separator.join(a))

	return "\n".join(tmp)


def sauvegarde(chemin, data):
	""" auteur: Nemo Anael
		Entrées: - data: string
		Retourne: Booléen, True si la sauvegarde a réussie, False sinon

		Sauvegarde au format CSV, séparateur: ','
		Il faudra faire attention lors de la sauvegarde du caractère ','
		il va falloir trouver un caractère de substitution ou un code.
	"""
	csv = open(chemin, "w")
	a = csv.write(data)
	return a


