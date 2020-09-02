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

    choix_recommencer = "oui"
    while choix_recommencer == "oui":
        #Tour1
        joueur = Joueur("beber")                  
        croupier = Croupier() 
        print("Début de la partie")    
        print("--------------------------")           
        croupier.distribue(2,joueur) 
        croupier.distribue(1)                     
        print("la main du joueur est :", joueur.hand)
        print("--------------------------")
        print("la carte du croupier est :", croupier.joueur.hand[0])
        joueur.calcul_hand()
        print("--------------------------")
        print("le score du joueur est :", joueur.score)
        croupier.joueur.calcul_hand()
        print("--------------------------")
        print("le score du croupier est :", croupier.joueur.score)

        print("--------------------------------")

        #Tour2
    
        choix_carte_supp =""
        while choix_carte_supp != "oui" and choix_carte_supp != "non":
            choix_carte_supp = input("le joueur veut continuer ?:")
            if choix_carte_supp == "oui":
                croupier.distribue(1, joueur)
                joueur.calcul_hand()
                print("la nouvelle main du joueur est", joueur.hand)
                print("--------------------------")
                print("le nouveau score du joueur est", joueur.score)
                while joueur.score < 21:
                    choix_carte_supp = input("le joueur veut continuer ?:")
                    croupier.distribue(1, joueur)
                    joueur.calcul_hand()
                    print("la nouvelle main du joueur est :", joueur.hand)
                    print("--------------------------")
                    print("le nouveau score du joueur est :", joueur.score)
            elif choix_carte_supp == "non":
                print("on tire les mains du croupier pour comparer :")
                croupier.distribue(1)
                print("la main du croupier est :", croupier.joueur.hand)
                croupier.joueur.calcul_hand()
                print("le score du croupier est :", croupier.joueur.score)
            choix_recommencer = input("le joueur veut rejouer ?:")
    print("Merci et à bientôt")
                # comparaison des mains..
               
        #choix_carte_supp = choix_carte_supp[0].lower()



        #print(croupier.joueur.score)