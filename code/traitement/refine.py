from numpy import shape
import os
#Globals

#Chemin d'accès au fichier keylogger
path = ''
#Contenu du fichier
data_prime =() #Un tuple qui contient les données extraites du keylog
#Dictionnaire de transfert
dict_str = {'space' : ' ', '\;' : ',', 'AFK' : '\\'}
dict_maj = {'a' : 'A', 'b' : 'B', 'c' : 'C', 'd' : 'D', 'e' : 'E', 'f' : 'F', 'g' : 'G', 'h' : 'H', 'i' : 'I', 'j' : 'J', 'k' : 'K', 'l' : 'L', 'm' : 'M', 'n' : 'N', 'o' : 'O', 'p' : 'P', 'q' : 'Q', 'r' : 'R', 's' : 'S', 't' : 'T', 'u' : 'U', 'v' : 'V', 'w' : 'W', 'x' : 'X', 'y' : 'Y', 'z' : 'Z'}
list_delete = ['space', 'ctrl', 'shift', 'delete', 'AFK', 'verr.maj']
list_butcher = ['space', 'ctrl', 'shift', 'delete', 'AFK', 'verr.maj', 'left', 'right', 'up', 'down']
def ouvre_fichier(chemin = path, encodage="utf8"): ##Ecrit par Némo, relu par Anaël
	"""Entrée: - chemin: string, chemin vers le fichier à ouvrir
	Retourne: objet File, fichier ouvert
    Envoie une erreur si le fichier n'éxiste pas"""
	if os.path.exists(chemin):
		return open(chemin, "r", encoding=encodage)

	raise ValueError("file doesn't exists")
    
def parse_CSV(chemin, encodage="utf8"):
	"""
		Entrée: - chemin: string, chemin vers le fichier à ouvrir,
							le fichier doit être au format CSV
		Retourne: Liste de tuples au format (str, timecode)
		 où str caractérise un caractère et timecode est un flottant
	"""
	fichier = ouvre_fichier(chemin, encodage)
	data = []

	lines = fichier.readlines()
	for line in lines:
		raw = line.split(",")

		# Teste si la ligne contient bien 2 éléments	
		if len(raw) <= 1:
			continue

		# Teste si le premier caractère du second string est
		# un nombre, permet de passer le cas du header
		if ord(raw[1][1]) < 46 or ord(raw[1][1]) > 57:
			continue

		# Il faut retirer le caractère \n pour convertir
		timecode = float(raw[1].replace("\n", ""))
		item = (raw[0], timecode)

		data.append(item)

	fichier.close()
	return data

def setpath(p : str, ex = True) : #Ecrit par Anaël, relu par Némo
    '''
    Fonction qui prend en argument un string indiquant le dossier de travail.
    Tous les fichiers manipulés et crés doivent se trouver dans ledit dossier
    
    Utiliser setpath est indispensable avant tout action de refine
    
    Si le chemin est changé en cours de travail, les fichiers devront être déplacés manuellement.
    
    Par défaut, setpath extrait les données du fichier. Spécifier ex = False pour éviter ceci.
    Si les données n'ont pas été extraites une fois, le programme ne fonctionnera pas'

    '''
    
    global path
    path = p
    
    if ex :
        global data_prime
        data_prime = parse_CSV(path + '/data.csv')
        
def separate(S = data_prime, types = tuple, assamble = False, create = False, name = 'extracted_data') : #Ecrit par Anaël 
    
    '''
    Arguments : S : liste de tuple, assamble (optionnel) : booléen, create (optionel) : booléen, name (optionnel) : str, type : tuple ou list (par défaut tuple)
    
    Permet d'extraire les données de la liste S en plaçant d'un côté les str, de l'autre les temps.
    Par défaut, traîte les données directement extraites du fichier source
    Renvoie par défaut une tuple de listes. Si list est choisit, retourne une liste de listes Si assamble est spécifié, compile les sous listes en un seul élément.
    
    Si create est spécifié, stocke les données extraites dans différents fichiers txt (désactivé par défaut)
    Si un nom est spécifié, les fichiers créés prendront celui-ci
    
    Exemples pour un fichier source [[a, 1], [b, 2], [c, 3], [d, 4], [e, 5]]
    
    separate()
    >>> [[a, b, c, d, e], [1, 2, 3, 4, 5]]
    
    separate(assamble = True)
    >>> [abcde, 12345]
    '''
    
    I, J = shape(S)
    store = [[] for j in range(J)]
    for j in range (J) :    
        item = [0 for i in range(I)]
        for i in range(I) :
            item[i] = S[i][j]
        store[j] = item
    
    if assamble :
        block = [0, 0]
        I, J = shape(store)
        k = ''
        l = ''
        for j in range(J) :
            k += str(store[0][j])
            l += str(store[1][j])
        block[0] = k
        block[1] = l
        if create :
            for j in range(len(block)) :
                with open(path + '/' + name + str(j) + '.txt', 'x') as f :
                    f.write(block[j])
                    
        return types(block)
      
    elif create :
       for j in range(J) :
           with open(path + '/' + name + str(j) + '.txt', 'x') as f :
             for s in store[j] :
                 f.write(s + "\n")
    return types(store)

def fine(S : list, shift = False) :
    """
    

    Paramètres :
        S : liste du tuples (format similaire au fichier source)
        shift (optionnel) : booléen, par défaut False. Si spécifié, traite les majuscules
    
    Retourne une liste de tuple dont la partie str a été traitée pour être plus lisible.
    
    >>>fine([(a, 1) , (b, 2) , (shift, 3), (e, 4)], shift = True)
    [(a, 1), (b, 2), (E, 4)]

    """
    #Evite de modifier la liste mère (optionnel)
    L = []
    n = len(S)
    verr_maj = False #Booléen qui détecte si la majuscule est verrouillée
    #Transtypage en liste pour la manipulation
    for i in range(n) :
        L.append(list(S[i]))
        
    I = [] #Liste d'indies à retirer
    for i in range(n) :
        #Modifier l'état majuscule verrouillée
        if L[i][0] == 'verr.maj' :
            if verr_maj :
                verr_maj = False
            else :
                verr_maj = True
            I.append(i)
        #Traitement des caractères spéciaux
        if L[i][0] in dict_str :
            L[i][0] = dict_str[L[i][0]]
        #Traitement des majuscules
        if shift and ((S[i][0] == 'shift') != verr_maj) and i != len(S) - 1 :
            if L[i + 1][0] in dict_maj :
                L[i + 1][0] = dict_maj[L[i + 1][0]]
                if not verr_maj :
                    I.append(i)
    
    #Supprimer les caractères indésirables
    for i in range(1, len(I) + 1) :
        L.pop(I[-1 * i])
        
    #Recompilation en tuples
    for i in range(len(L)) :
        L[i] = tuple(L[i])
            
    return L

def fine_backspace(S : list):
    """
    
    Traite les backspace dans une liste de tuples.
    ATTENTION : il est primordiale d'avoir traité la liste avant'

    """
    L = []
    n = len(S)
    #Transtypage en liste pour la manipulation
    for i in range(n) :
        L.append(list(S[i]))
        
    I = [] #Liste d'indies à retirer
    for i in range(len(L)) :
        if L[i][0] == 'delete' :
            I.append(i)
            j = 1
            while j < i :
                if i - j not in I and L[i - j][0] not in list_delete :
                    I.append(i - j)
                    break
                j += -1
    
    #Supprimer les caractères indésirables
    for i in range(1, len(I) + 1) :
        print(L.pop(I[-1 * i]))
        
    #Recompilation en tuples
    for i in range(len(L)) :
        L[i] = tuple(L[i])
            
    return L

def butcher_cut(S : list) :
    """
    

    Fonction de traitement final et radical, à n'utiliser qu'en dernier recours.
    Prend en argument une liste de tuple de format simillaire aux données extraites.
    Coupe tous les caractères parasites qui n'ont pas pu être traités'

    """
    
    L = S.copy()
    I = [] #Liste d'indices à retirer
    for i in range(len(S)) :
        if L[i][0] in list_butcher :
            I.append(i)
    for i in range(1, len(I) + 1) :
        L.pop(I[-1 * i])
    
    return L
    
        

setpath('/Users/anaelmarit/Documents/Prepa/Cesare_force/ngSoftware/Software/Legals/')