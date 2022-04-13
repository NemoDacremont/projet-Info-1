
def data_to_string(data):
	"""
	"""
	tmp = []
	for i in range(len(data)):
		a = []
		for j in range(len(data[i])):
			a.append(str(data[i][j]))
		tmp.append(",".join(a))

	return "\n".join(tmp)


def sauvegarde(chemin, data):
	""" auteur: Nemo Anael
		Entrées: - data: 
		Retourne: Booléen, True si la sauvegarde a réussie, False sinon

		Sauvegarde au format CSV, séparateur: ','
		Il faudra faire attention lors de la sauvegarde du caractère ','
		il va falloir trouver un caractère de substitution ou un code.
	"""
	csv = open(chemin, "w")
	a = csv.write(data)
	return a


