
# Modules python
import keyboard
import time
import sys
import os
import json

# Fichiers locaux
import polymorph
import sauvegarde_local

## Global Variables
keys = []
start_date = time.time()
last_date = start_date
date_derniere_sauvegarde = time.time()

# Caractères à laisser passer que ce soit pressé ou relaché
caracteres_importants = ["maj", "right shift", "verr.maj"]

caracteres_remplacement = {
	"maj": "shift",
	"backspace": "delete",
	"right shift": "shift"
}

# Récupère la configuration depuis le fichier config.json
dossier_courant = os.path.dirname(__file__)
chemin_config = os.path.join(dossier_courant, "config.json")

config_file = open(chemin_config)
config = json.load(config_file)

chemin_sauvegarde = os.path.join(dossier_courant, config["sauvegarde_locale"])

#
#  Main
#
while True:
	# Attend l'envoie d'une 
	event = keyboard.read_event()

	# Permet d'arrêter le programme
	if event.name == 'esc':
		break

	print(event.name, event.event_type)
	
	# Ne considère l'évennement que si la touche est pressée
	if event.name in caracteres_importants or event.event_type == keyboard.KEY_DOWN:
		date = time.time()
		test = date - last_date

		char = event.name
		# on doit substituer ',' par un autre caractère pour pouvoir
		# le différencier du séparateur dans le format CSV
		if char == ',':
			char = '\;'

		item = (char, test)
		keys.append(item)

		last_date = date


#print("char,timecode")
#for el in keys:
#	print(f"{el[0]},{el[1]}")


print("sauvegarde vers", chemin_sauvegarde)
a_ecrire = sauvegarde_local.data_to_string(keys)
sauvegarde_local.sauvegarde(chemin_sauvegarde, a_ecrire)

