import os
import keyboard
from time import time


if not os.path.isfile('data.csv') :
    with open('data.csv', 'x') as f :
        None

# Global Variables

keys = []
start_date = time() #Temps d'initialisation
last_date = start_date

del_time = time() #Marqueur afin de réinitialiser périodiquement le fichier tewte
real_time = time() #Temps réel (modifié en condtinue)
afk_time = time() #Compteur afin de sauter des lignes lorsque l'utilisateur est afk

# Cœur du programme

while True :
    while real_time - del_time < 3600 :

        event = keyboard.read_event()
        real_time = time()

        if event.name == 'esc': #Condition pour briser manuellement la boucle
            break

        if event.event_type == keyboard.KEY_DOWN : #Détecte le clavier
           log_time = real_time - last_date

           char = event.name
           if char == ',' :
               char = ';'
           item = [char, log_time]
           afk_time = time() #Variable de détection d'afk
           last_date = time()

           #Attention, il faut indiquer le bon chemin d'accès
           with open('/Users/anaelmarit/Documents/Prepa/Cesare_force/ngSoftware/Software/Legals/data.csv', 'a') as csv :
               csv.write(str(item[0]) + ',' + str(item[1]) + '\n')

        if abs(afk_time - real_time) > 10 :
            with open('/Users/anaelmarit/Documents/Prepa/Cesare_force/ngSoftware/Software/Legals/data.csv', 'a') as csv :
               csv.write('AFK,' + str(real_time - afk_time) + '\n')
            afk_time = time()

    with open('/Users/anaelmarit/Documents/Prepa/Cesare_force/ngSoftware/Software/Legals/data.csv', 'w') as csv :
               csv.write('')
    del_time = time()