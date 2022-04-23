
# Modules python
import keyboard
import time
import sys
import os
import json

# Fichiers locaux
import sauvegarde_local
from manipulation_string import strings_egaux

## Global Variables
keys = []
start_date = time.time()
last_date = start_date
date_derniere_sauvegarde = time.time()
dernier_caractere = ''

# Caractères à laisser passer que ce soit pressé ou relaché
caracteres_importants = ["shift", "delete"]

caracteres_remplacement = {
	',' : '/v',#Dictionnaire pour normaliser l'écriture
	';' : '/pv', #Ceci permet de palier aux différences de système d'exploitation
	'maj' : 'shift', #Et d'éviter des conflits avec le csv
	'right shift' : 'shift',
	'caps lock' : 'verr.maj',
	'backspace' : 'delete',
	'\'' : '/a',
	'\"' : '/g',
    'gauche' : 'left',
    'droite' : 'right',
    'haut' : 'up',
    'bas' : 'down',
    'windows gauche' : 'cmd'
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

	# Permet de normaliser les systèmes linux et windows
	eventname = event.name
	if event.name in caracteres_remplacement:
		eventname = caracteres_remplacement[event.name]

  # teste le cas où le caractère entré est un caractère important
	est_un_caractere_important = eventname in caracteres_importants
  # teste si le caractère est un appui long, permet de ne pas compter plusieurs shift lorsqu'on reste appuyer dessus longtemps
  # avant de tapper d'autre caractères
	est_un_appuie_long = event.event_type == keyboard.KEY_DOWN and strings_egaux(eventname, dernier_caractere)

  # permet finalement de créer la condition d'ajout du caractère important
	caracteres_importants_a_ajouter = est_un_caractere_important and not est_un_appuie_long

	# Ne considère l'évennement que si la touche est pressée
	if caracteres_importants_a_ajouter or not(est_un_caractere_important) and event.event_type == keyboard.KEY_DOWN:
		date = time.time()
		test = date - last_date

		print(eventname, event.event_type)

		char = eventname
		# On doit normaliser certains caractères
        # Pour éviter des problèmes de csv et de différence d'os
		if char in caracteres_remplacement :
			char = caracteres_remplacement[char]

		item = (char, test)
		keys.append(item)

		last_date = date
		dernier_caractere = eventname

		# réinitialise le dernier caractère pour que l'appuie long fonctionne de nouveau
		# pour la détection des caractères spéciaux à ajouter
		if est_un_caractere_important and event.event_type == keyboard.KEY_UP:
			dernier_caractere = ''


#print("char,timecode")
#for el in keys:
#	print(f"{el[0]},{el[1]}")


print("sauvegarde vers", chemin_sauvegarde)
a_ecrire = sauvegarde_local.data_to_string(keys)
sauvegarde_local.sauvegarde(chemin_sauvegarde, a_ecrire)

