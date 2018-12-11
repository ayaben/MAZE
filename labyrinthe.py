import random 


class Labyrinthe:

##creation de labyrinthe
	cases = []
	laby_string = ''
	

	def __init__(self, n=5, m=6):
		self.n = n
		self.m = m
		self.creer_base_laby()
		self.sortie = self.piece_aleatoire()
		
		#self.afficher_laby()
		print("Sortie se situe: {}".format(self.sortie))

	def creer_base_laby(self):
		#print("Creation du labyrinthe de taille {}, {}".format(self.n,self.m))
		for i in range(0, self.n):
			self.cases.append([])
			for j in range(0, self.m):
				val = 0 if random.randint(0,2) > 0 else 1
				self.cases[i].append(val)
				

	def afficher_laby(self):
		for i in range(0, self.n):
			for j in range(0, self.m):
				self.laby_string += ' ' if self.cases[i][j] == 0 else '+'
			self.laby_string += '\n'
		print(self.laby_string)
	



	def afficher_chemin(self, chemin):
		reponse = ''
		for i in range(0, self.n):
			for j in range(0, self.m):
				if [i, j] in chemin:
					etape = chemin.index([i, j])
					if etape + 1 < len(chemin):
						prochaine_etape = chemin[etape + 1]
					else:
						prochaine_etape = self.sortie
					if prochaine_etape[0] > i:
						reponse += '↓' 
					elif prochaine_etape[0] < i:
						reponse += '↑'
					elif prochaine_etape[1] > j:
						reponse += '→'
					else:
						reponse += '←'
				elif self.cases[i][j] == 1:
					reponse += '+'
				else:
					reponse += ' '
			reponse += '\n'
		print(reponse)
				





	def piece_aleatoire(self):
		##On prend un nbre binaire aleatoire pour commencer avec les lignes ou les colonnes
		if random.randint(0, 1) == 0:
			ligne = random.randint(0, self.n-1)
			colonne = 0 if  random.randint(0, 1) else self.m-1
		else:
			colonne = random.randint(0, self.m-1)
			ligne = 0 if  random.randint(0, 1) else self.n-1
		#On modifie la case à 0 pour eviter d'avoir une case dans un mur 
		self.cases[ligne][colonne] = 0	
		return [ligne, colonne]

chemin = []


def cherche_sortie(laby, position):
	# Si la position correspond a la sortie le labyrinthe a une soltuion
	if position[0] == laby.sortie[0] and position[1] == laby.sortie[1]:
		return True
	# La case correspon à un mur
	elif laby.cases[position[0]][position[1]] == 1:
		return False
	# la case a déjà été visitée
	elif laby.cases[position[0]][position[1]] == 2:
		return False
	# on note la case comme étant deja visitée
	laby.cases[position[0]][position[1]] = 2
	# on ajoute la position au chemin parcouru 
	chemin.append(position)
	# parcourir les voisins récursivement
	if ((position[0] < (laby.n - 1) and cherche_sortie(laby, [position[0]+1, position[1]]))
		or (position[1] > 0 and cherche_sortie(laby, [position[0], position[1]-1]))
		or (position[0] > 0 and cherche_sortie(laby, [position[0]-1, position[1]]))
		or (position[1] < (laby.m-1) and cherche_sortie(laby, [position[0], position[1]+1]))):
		return True
	# On supprime la dernière case visitée car il n'y a plus de mouvement possible
	chemin.pop()
	# Si l'execution arrive jusqu'ici c'est qu'il n' y a plus de cases à tester donc pas de solution
	return False


def position_initiale(laby):
	x = random.randint(0, laby.n-1)
	y = random.randint(0, laby.m-1)
	if laby.cases[x][y] == 1:
		return position_initiale(laby)
	return [x, y]