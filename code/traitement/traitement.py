
def brute_force(liste, liste_de_mots):
	"""
		Entrée: - liste: liste de tuples au format ('c', timecode) avec 'c' un caractère et timecode un float
						- liste_de_mots: une liste de string, chaque string correspond à un mot

		Retourne: un dictionnaire avec comme clef les mots trouvés et pour valeurs le nombre d'occurences

		La fonction bruteforce parcourt la liste pour trouver toutes les occurences des mots contenus dans liste_de_mots
	"""
	mots_trouves = {}

	for mot in liste_de_mots:
		for i in range(len(liste)):
			mot_trouve = True
			for j in range(len(mot)):
				if liste[i+j][0] != mot[j]:
					mot_trouve = False
					break
				
			if mot_trouve:
				if mot in mots_trouves.keys():
					mots_trouves[mot].append(i)
				else:
					mots_trouves[mot] = [i]

		return mots_trouves




def find_s(a, S):
	"""écrit par Daniel
	Trouve le string a dans le string S"""
	for i in range(len(S)):
		if S[i] == a[0]:
			for k in range(len(a)):
				if S[i + k - 1] == a[1]:
					return [s for s in range(i, len(a))]

	else:
		return False


S = "Ma grosse saucisse"
SS = ["Magrossesaucisse", "Magrossesaucisse"]
T = "Greetings stranger, fortuned fellow, Tis a party for which I bellow. I invite The King In Yellow, so come all ye in Yhtil. Wear thine masks upon you to my masquerade until… HE may come to lost Yhtil. Hope for us there may be still Shadows lengthen, streets darken, to the curfew thou must harken. Why so loudly dost thou bark in the dimmed city of Yhtil? Only much attention quite unwholesome you’ll instill… from the souls of poor Yhtil. Why attract so much ill will? That is just what I must seek, see, hidden somewhere ‘mongst the meekly, ‘Tis one invitee I seek he – shall all my mistakes undo.Tis the king in yellow whose great wealth I shall accrue. When his shadow passes through, wealth will come to I and you Lo, your plans shall surely languish, and this whole town will know anguish, For the King is whom they say which shall this city indeed smite. If he comes, Yhtil, and you, and I will know his might. All’ll be lost within a night. What reward is worth that price? Wearing this expensive clothing, pardon from my family’s loathing – lasting til I’m decomposing, all my friends who’ve strife I’ve caused; Yes – preparing for this night, their forgiveness is the cause, they shall all be proud because, I had brought the king to us Welcome, company most cherished! May my loneliness thus perish To this evening we shall share much which would be wasted by myself. No attendants have arrived tonight alas, besides thyself. But I’ll be beside myself, when the King reveals himself. Lay thine hands upon my bodice, for before you stands a goddess – Know this guest of goldenrod is merely the first of the night. Let us drink to your great wealth, and family, and life, lasting til your afterlife, All’ll be yours once he arrives. Yes, until my schemes may flourish, we shall haunt my empty fortress. Let us dance a whirling dervish while we feed out appetites. By the ‘morrow we shall know if the King came tonight. Midnight marks the final chime. Until that comes, there is still time. Be thee graciously obeisant, demonstrate a courtly patience, He declines no invitation he receives upon his court. All who live in doomed Yhtil will know without report; The King arrived by your escort, A prophecy of grim import."


def find_U(a, S):
	"""écrit par Daniel
	Trouve un string a dans une liste de string S"""
	L = []
	for k in range(len(S)):
		for i in range(len(S[k])):
			if S[k][i] == a[0]:
				for u in range(len(a)):
					if S[k][i + u - 1] == a[1]:
						L.append([k, [s for s in range(i, len(a))]])
	return L


def salomon(S, n=5):
	"""écrit par Daniel
	Découpe la liste S en liste de listes L de n éléments"""
	L = []
	for i in range((len(S) // n) + 1):
		L.append([])
		print(L)
		if i == ((len(S) // n) + 1):
			for s in range((len(S)) % n):
				L[i][s] = S[s + n * i]
		else:
			for k in range(n):
				print(k, range(n))
				print(L)
				L[i].append(S[k + n * i])
	return L


def data_salomon(S,t = 5):
	"""écrit par Daniel
	Découpe la liste selon les espaces et les temps"""
	L = []
	a = ""
	for i in range(len(S)):
		if i <= len(S):
			while S[i][0] != 'space' or S[i][1] < t:
				if S[i] == S[-1]:
					a += S[i][0]
					S.pop(i)
					break
				a += S[i][0]
				S.pop(i)
			if a != "":
				L.append(a)
			a = ""
		elif i > len(S):
			return L

def rover(L,M):
	S = []
	c = 0
	for word in L:
		for k in range(len(M)//len(word)):
			for i in range(len(word)):
				if word[i] == M[k*len(word)+i]:
					c = c+1
		S.append([word,c])
		c = 0
	return S

def rover_mk2(L,M):
	"""écrit par Daniel
	L est une liste de string et M est un string"""
	S = []
	c = 0
	d = 0
	for word in L:
		for k in range(len(M)-len(word)):
			for i in range(len(word)):
				if word[i] == M[k+i]:
					c = c+1
					if c == len(word):
						d = d+1
						c = 0
			c = 0
		S.append([word,d])
		c = 0
		d = 0
	return S


def inverse(L):
	U = []
	for i in range(len(L)):
		U.append(L[-(1+i)])
	return U

def data_salomon_time(S,t = 5):
	"""écrit par Daniel
	Découpe la liste selon les espaces et les temps"""
	L = []
	a = ""
	P = 0
	for i in range(len(S)):
		if i <= len(S):
			P = S[i][1]
			while S[i][0] != 'space' or S[i][1] < t:
				if S[i] == S[-1]:
					a += S[i][0]
					S.pop(i)
					break
				a += S[i][0]
				S.pop(i)
			if a != "":
				L.append([a,P])
			a = ""
		elif i > len(S):
			return L

def plage(L,S = 5):
	if len(L) < S:
		return "T'essaye quoi wesh"
	J = []
	T = ["oueap",".com",".fr"]
	for i in range(len(T)):
		for k in range(len(L)):
			if T[i] == L[k]:
				J.append([])
				for t in range(S):
					J[i].append(L[t+(k+1)])
	return J

def terminator_2(L):
	for i in range(len(L)):
		if L[i][0] == 'backspace':
			L.pop(i)
	return L

def terminator(L):
	i = 0
	while L[i] != L[len(L)-1]:
		print(i, len(L))
		if L[i][0] == 'backspace':
			L.pop(i)
		i = i + 1
	return L

# def rover_tuple(L,M):
# 	"""écrit par Daniel
# 	L est une liste de string et M est une liste de tuples dont le premier indice est un string"""
# 	S = []
# 	c = 0
# 	d = 0
# 	for word in L:
# 		for k in range(len(M)-len(word)):
# 			for i in range(len(word)):
# 				if word[i] == M[k+i][0] or refine.dict_str[M[k+i]] == word[i]:
# 					c = c+1
# 					if c == len(word):
# 						d = d+1
# 						c = 0
# 			c = 0
# 		S.append([word,d])
# 		c = 0
# 		d = 0
# 	return S

def plage_bis(L,S = 5):
	"""L est une liste de string et S est le nombre de caractères renvoyé"""
	if len(L) < S:
		raise ValueError("Liste trop courte")
	J = []
	T = ["oueap",".com",".fr"]
	t = 0
	for i in range(len(T)):
		for k in range(len(L)):
			if T[i] == L[k]:
				J.append([])
				while len(J)<S:
					print("mot :",L[t+(k+1)])
					for y in range(len(L[t+(k+1)])):
						print("y :",y)
						print("len :",len(L[t + (k + 1)]),"L[t+(k+1)][y] :",L[t+(k+1)][y])
						print("len(J) :",len(J),"J",J)
						J[i].append(L[t+(k+1)][y])
					t = t + 1
	return J

#print(data_salomon(parse_CSV("data.csv", "utf16")))
#print(plage_bis(data_salomon(parse_CSV("data.csv", "utf16"))))
#print(rover_mk2(["Yhtil","King","yellow"],T))
#print(cesaretri.fusion(rover_mk2(["Yhtil","King","yellow"],T)))

