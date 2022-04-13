
import requests

def envoie(url, data):
	"""
		Entrée: -url: string, chemin vers le serveur
						-data: string, données au format CSV à envoyer au serveur

		Effectue une requête POST en envoyant data dans le body
	"""

	requests.post(url, data)
