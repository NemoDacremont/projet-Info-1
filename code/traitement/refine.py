#Module écrit par Anaël avec l'aide des bons conseils de Nemo

import os
from manipule_csv import *
from fusion import fusion

if __name__ == "__main__":
	print('>>> Pour recevoir de l\'aide, essayez help(tutoriel)')

###Globals###

#Chemins utiles
path = os.path.dirname(__file__) +'/' #Chemin courant
dictpath = path + 'Dictionnaires'


#Dictionnaire de transfert (les dictionnaires sont stockés en csv)
dict_str = dict(parse_CSV(dictpath + '/dict_str.csv', separator = ';'))
dict_maj = dict(parse_CSV(dictpath + '/dict_maj.csv', separator = ';'))
dict_alt = dict(parse_CSV(dictpath + '/dict_alt.csv', separator = ';'))
dict_acc_a = dict(parse_CSV(dictpath + '/dict_acc_a.csv', separator = ';'))
dict_acc_g = dict(parse_CSV(dictpath + '/dict_acc_g.csv', separator = ';'))
dict_trem = dict(parse_CSV(dictpath + '/dict_trem.csv', separator = ';'))
dict_circ = dict(parse_CSV(dictpath + '/dict_circ.csv', separator = ';'))
list_delete = ['space', 'ctrl', 'shift', 'alt', 'delete', 'AFK', 'verr.maj', 'tab', 'left', 'right', 'up', 'down', 'command']
list_butcher = ['space', 'ctrl', 'shift', 'delete', 'alt', 'AFK', 'verr.maj', 'left', 'right', 'up', 'down', 'command']

def tutoriel() : #Fonction qui fournit la marche à suivre pour le traitement.
    """
    
    Voici une liste des fonctions utiles. Pour recevoir une description détaillée de chacune, utilise 'help()'
    Un numéro a été ajouté entre parenthèses : il indique l'ordre dans lequel exécuter celles-ci pour un traitement optimal
    Ne pas respecter l'ordre a de fortes chances de conduire à des conflits, toutefois, il peut parfois être nécessaire d'éviter certains traitements.
    
    
    fine (1)
    fine_accent (2)
    fine_backspace (3)
	 fine_str (*)
    butcher_cut (4)
    parse_data(*)
    parse_CSV(*)
    save (*)
    extract (*)
    make_txt (*)
    refine(*)
	 discriminate (5)
    
    Les fonctions marquées d'une étoile peuvent être exécutées n'importe quand.
    
    Remarques importantes :
        - Il est fortement conseillé de travailler dans le dossier où se trouve le refine.py. Dans ce cas, l'argument 'chemin' de nombreuses fonctions devient optionnel
        - Les fonction parse_data et parse_CSV proviennent du module manipule_csv.py
        - Pour commencer le traitement, parse_data permet d'extraire les données du fichier récolté'
        - La fonction refine effectue tous les traitements d'un seul coup'

    """
    
    print('tapez help(tutoriel), le docstring est plus agréable à lire')
    
def save(S, chemin = path, name = 'new_file') :
    
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
        if os.path.isfile(chemin + name + '.txt') :
            save(S, chemin, name + '(copie)')
        else :
            with open(chemin + name + '.txt', 'x') as file :
                file.writelines(S)
    elif type(S) == list or type(S) == tuple :
        #Encore pour éviter les problèmes de doubles
        if os.path.isfile(chemin + name + '.csv') :
            save(S, chemin, name + '(copie)')
        else :
            with open(chemin +  name + '.csv', 'x') as file :
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
    

def fine(S : list, shift = True, alt = True) : #Relu par Daniel
    """
    

    Paramètres :
        S : liste du tuples (format similaire au fichier source)
        shift (optionnel) : booléen, par défaut True. Si spécifié, traite les majuscules
        alt (optionnel) : booléen, par défaut True. Si sspécifié, traite les alt
    
    Retourne une liste de tuple dont la partie str a été traitée pour être plus lisible.
    
    >>>fine([(a, 1), (b, 2), (shift, 3), (e, 4)], shift = True)
    [(a, 1), (b, 2), (E, 4)]

    """
    L = []
    n = len(S)
    verr_maj = False #Booléen qui détecte si la majuscule est verrouillée
    maj = False #Booléen qui permet de détecter lorsque la majuscule est maintenue enfoncée
    isAlt = False #Booléen qui permet de détecter si le bouton alt est maintenu enfoncé
    #Transtypage en liste pour la manipulation
    for i in range(n) :
        L.append(list(S[i]))
        
    I = [] #Liste d'indies à retirer
    for i in range(n) :
        #Modifier l'état majuscule verrouillée
        if L[i][0] == 'verr.maj' :
            verr_maj = not verr_maj
            I.append(i)
        #Modifier l'état majuscule enfoncée
        if L[i][0] == 'shift' :
            maj = not maj
            I.append(i)
        #Modifier l'état alt enfoncé
        if L[i][0] == 'alt' :
            isAlt = not isAlt
            I.append(i)
        #Traitement des majuscules
        if shift and (maj != verr_maj) :
            if L[i][0] in dict_maj :
                L[i][0] = dict_maj[L[i][0]]
        #Traitement des alt
        if alt and isAlt :
            if L[i][0] in dict_alt:
                L[i][0] = dict_alt[L[i][0]]
    
    #Supprimer les caractères indésirables
    for i in range(len(I) - 1 , -1, -1) :
        L.pop(I[i])
        
    #Recompilation en tuples
    for i in range(len(L)) :
        L[i] = tuple(L[i])
            
    return L
 
def fine_str(S) :
	"""
	
	Prend en argument une liste de tuples au format (str, float).
	Traite les caractères spéciaux (virgule, point-virgule, apostrophe, guillemet) qui sont par défaut codés différemment.
	
	ATTENTION : Si ces caractères sont par défaut codés de la sorte, c'est parce qu'il peuvent occasionner des bugs avec la syntaxe python et/ou avec le format csv.
	A utiliser à vos risques et périls.

	>>>fine_str([['l', 1], ['\a', 2]])
	[['l', 1], ["'", 2]]

	"""
	
	for i in range(len(S)) :
		if S[i][0] in dict_str :
			S[i] = (dict_str[S[i][0]], S[i][1])
			
	return S

def fine_accent(S : list) :
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
    for i in range(n - 1) :
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
    for i in range(len(I) - 1, -1, -1) :
        L.pop(I[i])
        
        #Recompilation en tuples
    for i in range(len(L)) :
        L[i] = tuple(L[i])
            
    return L

def fine_backspace(S : list): #
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
            for j in range(1, i + 1) :
                if i - j not in I and L[i - j][0] not in list_delete :
                    I.append(i - j)
                    break
  
    I = fusion(I)
    #Supprimer les caractères indésirables
    for i in range(len(I) -1, -1, -1) :
        L.pop(I[i])
        
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
    for i in range(len(I) - 1, -1, -1) :
        L.pop(I[i])
    
    return L

def extract(S, n = '*') :
    """
    
    Arguments :
        - S : liste de listes ou liste de tuples
        - n : int
    Ressort une liste ne contenant que le n-ième élément de chaque sous-liste ou sous-tuple
    
    Si n n'est pas spécifié', alors ressort une liste de listes dont la i-ème sous liste correspond à l'extraction du i-ème terme'
    
    extract_str([('a' , 1), ('b' , 2) , ('c' , 3)], 0)
    >>> ['a' , 'b' , 'c']
    
    """
    if type(n) == int :
        txt = []
        for i in range(len(S)) :
            txt.append(S[i][n])
        return txt
    elif n == '*' :
        txt = [extract(S, j) for j in range(len(S[0]))]
        return txt

def make_txt(S) :
    """
    
    Prend en argument une liste de str.
    Concaténe le tout en un seul str.
    
    make_txt(['a' , 'b' , 'c'])
    >>> 'abc'

    """
    txt = ''
    for i in range(len(S)) :
        if S[i] in dict_str:
            txt += dict_str[S[i]]
        elif S[i] == '/pv' :
            txt += ';'
        elif S[i] == '/v' :
            txt += ','
        else :
            txt += S[i]
    return txt

def refine(S) :
    """
    
    Prend en argument une liste de tuples, ressort une liste de tuples.
    Effectue tous les traitements dans l'ordre, c'est-à-dire fine, fine_accent, fine_backspace et butcher_cut.

    """
    S = fine(S)
    S = fine_accent(S)
    S = fine_backspace(S)
    S = butcher_cut(S)
    return S

def discriminate(S, temps = 10) :
	"""
	
	Paramètres :
		- S : une liste de tuples au format (str, float)
		- temps (optionnel) : un float, par défaut 10
	Retourne la liste S découpée selon des critères discriminants pour ensuite faciliter la recherche (diviser pour mieux régner).
	L'idée est de subdiviser la liste de données dans laquelle on recherchera les mots de passe en repérant certains points qui permettent avec une quasi certitude de dire qu'un mot de passe n'est pas à cheval sur ce point.
	'temps' permet de configurer la durée entre deux input à partir de laquelle on considère qu'un mot de passe ne se trouve pas entre les deux input.
	
	Il est nécessaire d'avoir traité la liste avant ! (au minimum fine ; un traitement complet est préférable.'
	
	Discriminate([(a, 1), (b, 2), (tab, 2), (c, 2), (d, 10), (e, 2)])
	>>> [[(a, 1), (b, 2)], [(c, 2)], [(d, 10), (e, 2)]]

	"""
	I = [] #Création d'une liste pour les points de jonctions
	index = [] #Sera transtypé en dictionnaire ; permet d'éviter de perdre de l'info
	#Dans le cas où le critère est le temps
	
	#Balayage pour repérer les jonctions
	for i in range(len(S)) :
		if S[i][0] == 'tab' or S[i][0] == 'enter' or S[i][0] == ' ' :
			I.append(i)
		elif S[i][1] >= temps :
			I.append(i)
			index.append((i, S[i])) #Stockage dans le dictionnaire
	index = dict(index)
	
	L = [0 for i in range(len(I) + 1)]
	L[0] = S[0 : I[0]]
	for i in range(len(I) - 1) :
		item = []
		#Condition pour ne pas perdre de l'info
		if I[i] in index :
			item.append(index[I[i]])
		item += S[I[i] + 1 : I[i + 1]]
		L[i + 1] = item
	item = []
	if I[-1] in index :
		item.append(index[I[-1]])
	item += S[I[-1] + 1 : len(S)]
	L[-1] = item
	
	return L