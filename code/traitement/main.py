
# importation des dépendences
import os
import json

# Importation des fichiers locaux
import refine
import manipule_csv
import traitement
import recherche

dossier_courant = os.path.dirname(__file__)
chemin_config = f"{dossier_courant}/config.json"

config_file = open(chemin_config)
config = json.load(config_file)
config_file.close()

ip_serveur = config["ip"]

liste_des_mdp = manipule_csv.parse_CSV("./top12k_pass.txt")
liste_des_mdp = refine.extract(liste_des_mdp, 0)

# Actualise les données depuis le serveur, sauvegardée dans le dossier ./data
manipule_csv.download_from_server(ip_serveur)
csv = manipule_csv.parse_CSV("./data")

csv = refine.fine(csv)
csv = refine.fine_accent(csv)
csv = refine.fine_backspace(csv)
csv = refine.fine_str(csv)

print(recherche.brute_force(csv, liste_des_mdp))
