import tkinter as tk
from labyrinthe import Labyrinthe, position_initiale, cherche_sortie


class Application(tk.Frame):
	def __init__(self, width=200, height=200):
		tk.Frame.__init__(self)
		self.grid()
		self.size = 40
		self.width = width * self.size
		self.height = height * self.size
		self.canvas = tk.Canvas(self, width=self.width, height=self.height)
		self.canvas.grid()




if __name__ == '__main__':
	app = Application(20, 20)
	app.mainloop()

N = 5
M = 10
L = Labyrinthe(N, M)
p_initiale = position_initiale(L)
print("La position initiale se situe: {}".format(p_initiale))
solution, chemin = cherche_sortie(L, p_initiale)
print(solution)
if chemin:
	L.afficher_chemin(chemin)
