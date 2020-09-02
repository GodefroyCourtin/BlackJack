from joueur import Joueur
from carte import Carte
from random import sample

class Croupier:

    def __init__(self):
        self.carte = Carte()
        self.paquet =[]
        self.creer_paquet()
        self.joueur = Joueur("croupier")

    def creer_paquet(self):
        for couleur in self.carte.couleur:
            for valeur in self.carte.valeur:
                self.paquet.append((valeur,couleur))

    def distribue(self, nbCarte, joueur="croupier"):
        if joueur == "croupier":
            for card in sample(self.paquet, nbCarte):
                self.joueur.hand.append(card)
                self.paquet.remove(card)

        else:
            for card in sample(self.paquet, nbCarte):
                joueur.hand.append(card)
                self.paquet.remove(card)

		
	
if __name__ == "__main__":

    #Tour1
    joueur = Joueur("beber")                  # un joueur arrive à la table
    croupier = Croupier()                     # le croupier deballe le paquet
    croupier.distribue(2,joueur) 
    croupier.distribue(1)                      # le croupier distribue 
    print(joueur.hand)
    print(croupier.joueur.hand[0])
    joueur.calcul_hand()
    print(joueur.score)
    croupier.joueur.calcul_hand()
    print(croupier.joueur.score)

    #Tour2
    choix_carte_supp =""
    while choix_carte_supp != "oui" and choix_carte_supp != "non":
        choix_carte_supp = input("continuer ?:")
        if choix_carte_supp == "oui":
            croupier.distribue(1, joueur)
            joueur.calcul_hand()
            print(joueur.hand)
            print(joueur.score)
        elif choix_carte_supp == "non":
            print("on compare les mains")
    #choix_carte_supp = choix_carte_supp[0].lower()


    #si arret
    #print(croupier.joueur.score)