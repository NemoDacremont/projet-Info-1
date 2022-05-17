def fusion(L) :
    
    def merge(l, m): #Sous programme fusionnant deux listes triées
        n = len(l) + len(m)
        a = 0
        b = 0
        i = 0
        X = [0 for i in range(n)]
        while i < n and a < len(l) and b < len(m) : #Boucle de tri
            if l[a] <= m[b] and a < len(l) :
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
    
    if len(L) == 0 :
	    return L
    X = L[0 : len(L) // 2]
    Y = L[len(L) // 2 : -1] + [L[-1]]
    return(forge(X, Y))
 
def fusion_bis(L) :
	def merge(L1, L2) :
		def aux(a, b, c) :
			if a == [] :
				return c + b
			elif b == [] :
				return c + a
			else :
				if a[0] < b[0] :
					c.append(a.pop(0))
					return aux(a, b, c)
				else :
					c.append(b.pop(0))
					return aux(a, b, c)
		return aux(L1, L2, [])
	if len(L) <= 1 :
		return L
	else :
		L1 = fusion_bis(L[0 : len(L) // 2])
		L2 = fusion_bis(L[len(L) // 2 : len(L)])
		return merge(L1, L2)

#Partie de test
if __name__ == "__main__" :
	from random import randint
	P = [randint(0, 100000) for i in range(100000)]
	Q = [randint(0, 1000000) for i in range(1000000)]
	#fusion_bis ne peut pas trier ces listes en général
	#fusion le peut ; nous l'avons gardée malgré sa syntaxe curieuse