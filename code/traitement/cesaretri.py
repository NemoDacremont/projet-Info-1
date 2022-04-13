import random as rd

def EstTriMieux(L) : #En pratique, on se contente de savoir si la liste est croissante
    n = len(L)
    cro = (L[0] - L[-1] <= 0) #Booléen qui prend la valeur True si la liste est croissante
    for i in range(1, n) :
        if (L[i -1] - L[i] > 0) == cro:
            return False
    return True

def EstTri(L) :
    n = len(L)
    for i in range(1, n) :
        if L[i-1] > L[i] :
            return False
    return True

def echange(l, a, b) :
    '''
    

    Parameters
    ----------
    l : Liste
    a : entier
    b : entier

    Echange les éléments d'indice a et b dans la liste l'

    '''
    c = l[a]
    l[a] = l[b]
    l[b] = c
    return l

def rechercheMin(l, k) :
    n = len(l)
    m = k
    for i in range(k, n) :
        if l[m] > l[i]:
            m = i
    return(m)
    

#Tri à bulle

def bulle(L) :
    n = len(L)
    if n == 0 :
        return None
    for i in range(n) :
        for j in range (i, n - 1) :
            if L[j] > L[j+1] :
                a = L[j]
                L[j+1] = L[j]
                L[j] = a
    return(L)

#Tri par sélection

def selec(L) :
    n = len(L)
    for k in range(n - 1) :
        L = echange(L, k, rechercheMin(L, k))
        #Pas besoin de return car l'algorithme agit direct sur la liste

#Tri par insertion


def TriInsertion(l) :
    def insertion(l, k) :
        x = l[k + 1] #Valeur à insérer
        a = k + 1
        for i in range(k + 1) : #Boucle pour trouver la position où insérer
            if l[i] > x :
                a = i
                break
            if a != k + 1 :
                for i in range(k + 1, a, -1) :
                    l[i] = l[i - 1]
                    l[a] = x
        
    n = len(l)
    for i in range(n - 1):
        insertion(l, i)

#Tri Fusion

def fusion(L) :
    
    def merge(l, m): #Sous programme fusionnant deux listes triées
        n = len(l) + len(m)
        a = 0
        b = 0
        i = 0
        X = [0 for i in range(n)]
        while i < n and a < len(l) and b < len(m) : #Boucle de tri
            if l[a][1] <= m[b][1] and a < len(l) :
                X[i] = l[a]
                a += 1
            else :
                X[i] = m[b]
                b += 1
            i += 1
        if a == len(l) and b < len(m) :
            for j in range(i, n) :
                X[j] = m[b]
                b += 1
        if b == len(m) and a < len(l) :
            for j in range(i, n) :
                X[j] = l[a]
                a += 1
        return(X)
    
    def forge(l, m) : #Algorithmes récursif de tri
        if len(l) == 1 and len(m) == 1 :
            return(merge(l, m))
        else :
            if len(l) > 1 :
                Xl = l[0 : int(len(l) / 2)]
                Yl = l[int(len(l) / 2) : -1] + [l[-1]]
                l = forge(Xl, Yl)
            if len(m) > 1 :
                Xm = m[0 : int(len(m) / 2)]
                Ym = m[int(len(m) / 2) : -1] + [m[-1]]
                m = forge(Xm, Ym)
            return(merge(l, m))
    
    X = L[0 : int(len(L) / 2)]
    Y = L[int(len(L) / 2) : -1] + [L[-1]]
    return(forge(X, Y))


#Définition des listes de test

C = [1, 2, 3, 4, 5]
D = [5, 4, 3, 2 ,1]
F = [1, 3, 2, 4, 5]

def R(n) : #Création d'une liste aléatoire de longueur n
    return [rd.randint(0, n) for i in range(n)]