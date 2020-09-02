from joueur import Joueur
from carte import Carte
from random import sample

class Croupier:

	def __init__(self):
		self.carte = Carte()
		self.paquet =[]
		self.creer_paquet()

	def creer_paquet(self):
		for couleur in self.carte.couleur:
			for valeur in self.carte.valeur:
				self.paquet.append((valeur,couleur))

	def main_joueur(self, joueur, nbCarte):
		for card in sample(self.paquet, nbCarte):
			joueur.hand.append(card)
		

if __name__ == "__main__":
	joueur = Joueur()
	jeu = Croupier()
	jeu.main_joueur(joueur, 2)
	print(joueur.hand)
	joueur.calcul_hand()
	print(joueur.score)
