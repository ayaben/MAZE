import tkinter as tk
from labyrinthe import Labyrinthe, position_initiale, cherche_sortie, chemin


class Application(tk.Frame):
	def __init__(self, width, height):
		tk.Frame.__init__(self, bg='black')
		self.grid()
		self.agrandir = 40
		self.width = width * self.agrandir
		self.height = height * self.agrandir
		self.taille_case = int(self.width/width)
		self.canvas = tk.Canvas(self, width=self.width, height=self.height)
		self.canvas.grid()

		L = Labyrinthe(width, height)
		p_initiale = position_initiale(L)
		print("La position initiale se situe: {}".format(p_initiale))
		solution = cherche_sortie(L, p_initiale)
		print(solution)
		print(chemin)
		L.afficher_laby()
		#if chemin:
			#L.afficher_chemin(chemin)


		self.dessiner_laby(L)
		self.dessiner_entree(p_initiale)
		self.dessiner_sortie(L)
		
		if solution:
			print('dessiner chemin')
			self.dessiner_chemin(L, chemin)

	def dessiner_laby(self, laby):
		for x in range(0, laby.n):
			for y in range(0, laby.m):
				if laby.cases[x][y] == 1:
					# Couleur mur
					fill ='black'
				else:
					fill = 'white'
				self.canvas.create_rectangle(
					y*self.taille_case, x*self.taille_case,
					(y+1)* self.taille_case, (x+1) * self.taille_case, fill=fill)


	def dessiner_chemin(self, laby, chemin):
		for i in range(0, laby.n):
			for j in range(0, laby.m):
				if [i, j] in chemin:
					etape = chemin.index([i, j])
					if etape + 1 < len(chemin):
						prochaine_etape = chemin[etape + 1]
					else:
						prochaine_etape = laby.sortie
					if prochaine_etape[0] > i:
						fleche = '↓' 
					elif prochaine_etape[0] < i:
						fleche = '↑'
					elif prochaine_etape[1] > j:
						fleche = '→'
					else:
						fleche = '←'
						#self.cannvas.create_rectangle(
						#j*self.taille_case + (self.taille_case/2),
						#i*self.taille_case, i*self.taille_case,
						#(j+1) * self.taille_case, (i+1) * self.taille_case/2)
					self.canvas.create_text(
						j*self.taille_case + (self.taille_case/2),
						i*self.taille_case + (self.taille_case/2),
						text=fleche, font=("Times", "30"))
	
	def dessiner_sortie(self, laby):
		self.canvas.create_rectangle(
			laby.sortie[1] * self.taille_case, laby.sortie[0] * self.taille_case,
			(laby.sortie[1] + 1) * self.taille_case, (laby.sortie[0] + 1) * self.taille_case,
			fill='green')
	def dessiner_entree(self, position):
		self.canvas.create_rectangle(
			position[1] * self.taille_case, position[0] * self.taille_case,
			(position[1] + 1) * self.taille_case, (position[0] + 1) * self.taille_case,
			fill='blue')





if __name__ == '__main__':
	app = Application(10, 10)
	app.mainloop()

