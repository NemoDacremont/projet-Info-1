
def data_to_string(data, separator=","):
	"""
		Entrée: - data: au format de liste de tuples au format 
						- separator: string du séparateur 
		Retourne: string au format CSV de data
	"""
	# liste des lignes du fichier
	tmp = []
	for i in range(len(data)):
		a = []
		for j in range(len(data[i])):
			a.append(str(j))
		
		# Stocke les données avant de les concaténées avec un séparateur
		tmp.append(separator.join(a))

	# il faut rajouter une nouvelle ligne à la fin du fichier pour que cela fonctionne en utilisant le mode 'a'
	return "\n".join(tmp) + '\n'


def sauvegarde(chemin, data, mode = 'a'):
	""" auteur: Nemo Anael
		Entrées: - data: string
		Retourne: Booléen, True si la sauvegarde a réussie, False sinon

		Sauvegarde au format CSV, séparateur: ','
		Il faudra faire attention lors de la sauvegarde du caractère ','
		il va falloir trouver un caractère de substitution ou un code.
	"""
	with open(chemin, mode) as csv :
		a = csv.write(data)
		return a
