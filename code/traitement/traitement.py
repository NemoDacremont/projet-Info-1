
import os

def ouvre_fichier(chemin, encodage="utf8"):
	"""
		Entrée: - chemin: string, chemin vers le fichier à ouvrir
		Retourne: objet File, fichier ouvert

		Envoie une erreur si le fichier n'éxiste pas
	"""

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
		if ord(raw[1][1]) < 48 or ord(raw[1][1]) > 57:
			continue

		# Il faut retirer le caractère \n pour convertir
		timecode = float(raw[1].replace("\n", ""))
		item = (raw[0], timecode)

		data.append(item)

	fichier.close()
	return data

print(parse_CSV("data.csv", "utf16")) # Wow ça marche


def find_s(a, S):
	"""Trouve le string a dans le string S"""
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
	"""Trouve un string a dans une liste de string S"""
	L = []
	for k in range(len(S)):
		for i in range(len(S[k])):
			if S[k][i] == a[0]:
				for u in range(len(a)):
					if S[k][i + u - 1] == a[1]:
						L.append([k, [s for s in range(i, len(a))]])
	return L


def salomon(S, n=5):
	"""Découpe la liste S en liste de listes L de n éléments"""
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
	"""Découpe la liste selon les espaces et les temps"""
	L = []
	a = ""
	for i in range(len(S)):
		#print("i =", i,"len =", len(S))
		if i <= len(S):
			while S[i][0] != 'space' or S[i][1] < t:
				if S[i] == S[-1]:
					a += S[i][0]
					S.pop(i)
					break
				a += S[i][0]
				S.pop(i)
				#print(S)
			if a != "":
				L.append(a)
			a = ""
		elif i > len(S):
			return L

def rover(L,M):
	S = []
	c = 0
	for word in L:
		print("word =",word)
		for k in range(len(M)//len(word)):
			print("k =",k)
			for i in range(len(word)):
				print("i =",i)
				if word[i] == M[k*len(word)+i]:
					c = c+1
		S.append([word,c])
		c = 0
	return S

def rover_mk2(L,M):
	S = []
	c = 0
	d = 0
	for word in L:
		#print("word =",word)
		for k in range(len(M)-len(word)):
			#print("k =",k)
			for i in range(len(word)):
				#print("i =",i,"word =",word[i],"Mword =",M[k+i])
				if word[i] == M[k+i]:
					c = c+1
					#print("######## C = ############",c)
					if c == len(word):
						d = d+1
						c = 0
						#print("@@@@@@@@@ D = @@@@@@@@@@@@",d)
			c = 0
		S.append([word,d])
		c = 0
		d = 0
	return S

print(data_salomon(parse_CSV("data.csv", "utf16")))