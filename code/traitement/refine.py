from numpy import shape
import os
#Globals

#Chemin d'accès au fichier keylogger
path = ''
#Contenu du fichier
data_prime =() #Un tuple qui contient les données extraites du keylog
#Dictionnaire de transfert
dict_str = {'space' : ' ', 'AFK' : '\\', '\pv' : ';', '/v' : ',', '/a' : '\'', '\g' : '\"'}
dict_maj = {'a' : 'A', 'b' : 'B', 'c' : 'C', 'd' : 'D', 'e' : 'E', 'f' : 'F', 'g' : 'G', 'h' : 'H', 'i' : 'I', 'j' : 'J', 'k' : 'K', 'l' : 'L', 'm' : 'M', 'n' : 'N', 'o' : 'O', 'p' : 'P', 'q' : 'Q', 'r' : 'R', 's' : 'S', 't' : 'T', 'u' : 'U', 'v' : 'V', 'w' : 'W', 'x' : 'X', 'y' : 'Y', 'z' : 'Z', '<' : '>', '^' : '¨', ',' : '?', ';' : '.', ':' : '/', '!' : '§', 'ù' : '%', '$' : '€', '*' : 'µ', '&' : '1', 'é' : '2', '\g' : '3', '\a' : "4", '(' : '5', '-' : '7', 'è' : '7', '_' : '8', 'ç' : '9', 'à' : '0', ')' : '°', '=' : '+'}
dict_alt = {'é' : '~', '\g' : '#', '\a' : '{', '(' : '[' ,'-' : '|', 'è' : '`', '_' : '//', 'à' : '@', ')' : ']', '=' : '}', 'e' : '€'}
#dict_acc_a = {'a' : 'á', 'A' : 'Á', 'e' : 'é', 'E' : 'É', 'i' : 'í', 'I' : 'Í', 'o' : 'ó', 'O' : 'Ó'}
dict_acc_g = {'a' : 'à', 'e' : 'è', 'u' : 'ù'}
dict_trem = {'a' : 'ä', 'e' : 'ë', 'i' : 'ï', 'o' : 'ö', 'u' : 'ü', 'y' : 'ÿ', 'A' : 'Ä', 'E' : 'Ë', 'I' : 'Ï', 'O' : 'Ö', 'U' : 'Ü', 'Y' : 'Ÿ'}
dict_circ = {'a' : 'â', 'e' : 'ê', 'i' : 'î', 'o' : 'ô', 'u' : 'û', 'A' : 'Â', 'E' : 'Ê', 'I' : 'Î', 'O' : 'Ô', 'U' : 'Û'}
list_delete = ['space', 'ctrl', 'shift', 'alt', 'delete', 'AFK', 'verr.maj', 'tab', 'left', 'right', 'up', 'down']
list_butcher = ['space', 'ctrl', 'shift', 'delete', 'alt', 'AFK', 'verr.maj', 'left', 'right', 'up', 'down']

def ouvre_fichier(chemin = path, encodage="utf8"): ##Ecrit par Némo, relu par Anaël
	"""Entrée: - chemin: string, chemin vers le fichier à ouvrir
	Retourne: objet File, fichier ouvert
    Envoie une erreur si le fichier n'éxiste pas"""
	if os.path.exists(chemin):
		return open(chemin, "r", encoding=encodage)

	raise ValueError("file doesn't exists")
def tutoriel() : #Fonction qui fournit la marche à suivre pour le traitement. Ecrit par Anaël
    """
    
    Voici une liste des fonctions utiles. Pour recevoir une description détaillée de chacune, utilise 'help()'
    Un numéro a été ajouté entre parenthèses : il indique l'ordre dans lequel exécuter celles-ci pour un traitement optimal
    Ne pas respecter l'ordre a de fortes chances de conduire à des conflits, toutefois, il peut parfois être nécessaire d'éviter certains traitements.
    
    parse_CSV(*)
    fine (1)
    fine_accent (2)
    fine_backspace (3)
    butcher_cut (4)
    separate (*)
    save (*)
    
    Les fonctions marquées d'une étoile peuvent être exécutées n'importe quand
    
    Remarques importantes :
        stocker le chemin du dossier de travail dans 'path' permet de ne plus avoir à spécifier le chemin aux fonctions. LE CHEMIN DOIT FINIR PAR / (ceci est valable même si le chemin est spécifié manuellement)
        parse_CSV permet d'extraire les données stockées dans n'importe quel csv

    """
    
    print('tapez help(tutoriel), le docstring est plus agréable à lire')
    
    
def parse_CSV(name, chemin = path, encodage="utf8"): #Ecrit par Némo, relu par Anaël
	"""
		Entrée:
            - name : str, nom du fichier à ouvrir, avec son extension (qui doit être csv)
            - chemin (optionnel) : str, indique le chemin du dossier où est stocké le fichier
            - encodage (optionnel) : str
		Retourne: Liste de tuples au format (str, timecode)
		 où str caractérise un caractère et timecode est un flottant
	"""
	fichier = ouvre_fichier(chemin + name, encodage)
	data = []

	lines = fichier.readlines()
	for line in lines:
		raw = line.split(";")

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

    
def save(S, chemin = path, name = 'new_file') : #Ecrit par Anaël
    
    """
    Arguments :
        - S : str ou liste de tuples. Données à sauvegarder.
        - chemin (optionnel) : str. Chemin complet où faire la sauvegarde. Par défaut le chemin de setpath
        - name (optionnel) : str. Nom du fichier créé, par défaut new_file. Pas d'inquiétudes sur les duplicata, le programme ne plantera pas si le fichier existe déjà. NE PAS AJOUTER D'EXTENSION
        
    Permet de sauvegarder le travail de traitement en cours dans un fichier extérieur.
    Si S est un str, la sauvegarde sera au format txt. Si c'est une liste, la sauvegarde sera au format csv' 
    
    ATTENTION : il peut être nécessaire d'appliquer fine sur des données extraites d'un fichier créé par save.
    En effet, les caractères point-virgule, apostrophe et guillemet entrant en conflit avec le csv, ils sont remplacés par des alias.
    Aucun autre traitement préalablement fait ne sera impacté (en particulier les majuscules, les alt, les backspace...)
    """
    
    if type(S) == str :
        #Si le fichier existe, rajoute (copie) au nom pour éviter les problèmes
        if os.path.isfile(chemin + '/' + name + '.txt') :
            save(S, chemin, name + '(copie)')
        else :
            with open(chemin + name + '.txt', 'x') as file :
                None
            with open(chemin + name + '.txt', 'w') as file :
                file.writelines(S)
    elif type(S) == list or tuple :
        #Encore pour éviter les problèmes de doubles
        if os.path.isfile(chemin + name + '.csv') :
            save(S, chemin, name + '(copie)')
        else :
            with open(chemin +  name + '.csv', 'x') as file :
                None
            with open(chemin + name + '.csv', 'w') as file :
                for item in S :
                    #Tests successifs, certais caractères posant problème au csv (en particulier le point-virgule, l'apostrophe et le guillemet)
                    if item[0] == ';' :
                        file.write('\pv' + ';' + str(item[1]) + '\n')
                    elif item[0] == '\"' :
                        file.write('\g' + ';' + str(item[1]) + '\n')
                    elif item[0] == '\'' :
                        file.write('\a' + ';' + str(item[1]) + '\n')
                    else :
                        file.write(item[0] + ';' + str(item[1]) + '\n')
    else :
        raise ValueError('Format de données non supporté. Attendu : string ou liste de tuples')
        
def separate(S = data_prime, chemin = path, types = tuple, assamble = False, create = False, name = 'extracted_data') : #Ecrit par Anaël, relu par Némo et Daniel
    
    '''
    Arguments :
        S : liste de tuple, 
        chemin  (optionnel): string indiquant le dossier de travail (par défaut le chemin indiqué dans setpath)
        assamble (optionnel) : booléen
        create (optionel) : booléen, name (optionnel) : str
        type (optionnel) : tuple ou list (par défaut tuple)
    
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
                with open(chemin + name + str(j) + '.txt', 'x') as f :
                    f.write(block[j])
                    
        return types(block)
      
    elif create :
       for j in range(J) :
           with open(chemin + name + str(j) + '.txt', 'x') as f :
             for s in store[j] :
                 f.write(s + "\n")
    return types(store)

def fine(S : list, shift = False, alt = False) : #Ecrit par Anaël, relu par Némo et Daniel
    """
    

    Paramètres :
        S : liste du tuples (format similaire au fichier source)
        shift (optionnel) : booléen, par défaut False. Si spécifié, traite les majuscules
        alt (optionnel) : booléen, par défaut False. Si spécifié, traite les alt
    
    Retourne une liste de tuple dont la partie str a été traitée pour être plus lisible.
    
    >>>fine([(a, 1), (b, 2), (shift, 3), (e, 4)], shift = True)
    [(a, 1), (b, 2), (E, 4)]

    """
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
        #Traitement des alt
        if alt and S[i][0] == 'alt' and i != len(S) - 1 :
            if L[i + 1][0] in dict_alt:
                L[i + 1][0] = dict_alt[L[i + 1][0]]
                I.append(i)
    
    #Supprimer les caractères indésirables
    for i in range(1, len(I) + 1) :
        L.pop(I[-1 * i])
        
    #Recompilation en tuples
    for i in range(len(L)) :
        L[i] = tuple(L[i])
            
    return L

def fine_accent(S : list) : #Ecrit par Anaël
    """
    

    Traite les accents dans une liste de tuples.
    ATTENTION : si cette fonction est exécutée avant le traitement des majuscules, peut créer des conflits.
    Il est recommandé de d'abord traiter les majuscules'

    """
    
    L = []
    n = len(S)
    #Transtypage en liste pour la manipulation
    for i in range(n) :
        L.append(list(S[i]))
        
    I = [] #Liste d'indies à retirer
    for i in range(n) :
        if i != n - 1 :
            if L[i][0] == '^' and L[i + 1][0] in dict_circ :
                L[i + 1][0] = dict_circ[L[i + 1][0]]
                I.append(i)
            if L[i][0] == '¨' and L[i + 1][0] in dict_trem :
                L[i + 1][0] = dict_trem[L[i + 1][0]]
                I.append(i)
            if L[i][0] == '`' and L[i + 1][0] in dict_acc_g :
                L[i + 1][0] = dict_acc_g[L[i + 1][0]]
                I.append(i)
        #Retirer les caractères parasites
    for i in range(1, len(I) + 1) :
        L.pop(I[-1 * i])
        
        #Recompilation en tuples
    for i in range(len(L)) :
        L[i] = tuple(L[i])
            
    return L

def fine_backspace(S : list): #Ecrit par Anaël
    """
    
    Traite les backspace dans une liste de tuples.
    ATTENTION : il est primordiale d'avoir traité la liste avant

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

def butcher_cut(S : list) : #Ecrit par Anaël
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

path = '/Users/anaelmarit/Documents/Prepa/Cesare_force/ngSoftware/Software/Legals/'
print('>>> Pour recevoir de l\'aide, essayez help(tutoriel)')