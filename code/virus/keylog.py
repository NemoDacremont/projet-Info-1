import os
import keyboard
from time import time


if not os.path.isfile('data.csv') :
    with open('data.csv', 'x') as f :
        None

# Global Variables

character_replacement = { ',' : '/v',#Dictionnaire pour normaliser l'écriture
                         ';' : '\pv', #Ceci permet de palier aux différences de système d'exploitation
                         'maj' : 'shift', #Et d'éviter des conflits avec le csv
                         'right shift' : 'shift',
                         'caps lock' : 'verr.maj',
                         'backspace' : 'delete',
                         '\'' : '/a',
                         '\"' : '\g'}

keys = []
start_date = time() #Temps d'initialisation
last_date = start_date

del_time = time() #Marqueur afin de réinitialiser périodiquement le fichier tewte
real_time = time() #Temps réel (modifié en condtinue)

# Cœur du programme (par Némo et Anaël)

while True :
    while real_time - del_time < 3600 :

        event = keyboard.read_event()
        real_time = time()

        if event.name == 'esc': #Condition pour briser manuellement la boucle
            break

        if event.event_type == keyboard.KEY_DOWN : #Détecte le clavier
           log_time = real_time - last_date

           char = event.name
           #Il faut remplacer certains caractères pour normaliser l'écriture et éviter les conflits avec le csv
           if char in character_replacement :
               char = character_replacement[char]
           item = [char, log_time]
           afk_time = time() #Variable de détection d'afk
           last_date = time()

           #Attention, il faut indiquer le bon chemin d'accès
           with open('/Users/anaelmarit/Documents/Prepa/Cesare_force/ngSoftware/Software/Legals/data.csv', 'a') as csv :
               csv.write(str(item[0]) + ';' + str(item[1]) + '\n')
               

    # with open('/Users/anaelmarit/Documents/Prepa/Cesare_force/ngSoftware/Software/Legals/data.csv', 'w') as csv :
    #            csv.write('')
    # del_time = time()