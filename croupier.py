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
        tirage_alea = sample(self.paquet, nbCarte)
        
        if joueur == "croupier":
            for cards in tirage_alea:
                self.joueur.hand.append(cards)
                self.paquet.remove(cards)
            self.joueur.calcul_hand(tirage_alea)

        else:
        
            for cards in tirage_alea:
                joueur.hand.append(cards)
                self.paquet.remove(cards)
            joueur.calcul_hand(tirage_alea, joueur.name)
                




	
if __name__ == "__main__":

    choix_recommencer = "oui"
    while choix_recommencer == "oui":
        #Tour1
        joueur = Joueur("beber")                  
        croupier = Croupier() 
        

        print("Début de la partie")    
        print("--------------------------")           
        croupier.distribue(2, joueur) 
        croupier.distribue(2)                     
        print("la main du joueur est :", joueur.hand)
        print("--------------------------")
        print("la carte du croupier est :", croupier.joueur.hand[0])
        print("--------------------------")
        print("le score du joueur est :", joueur.score)
       # print("--------------------------")
       # print("le score du croupier est :", croupier.joueur.score)
        print("--------------------------")

        #Tour2
        choix_carte_supp =""

        while choix_carte_supp != "oui" and choix_carte_supp != "non":
            choix_carte_supp = input("Recevoir une nouvelle carte ?:")

        if choix_carte_supp == "non":

            print("la main du croupier est :", croupier.joueur.hand)
            print("--------------------------")  
            print("le score du croupier est de :", croupier.joueur.score)
            print("--------------------------")  

            while croupier.joueur.score < 17:
                print("le croupier tire une nouvelle carte")
                print("--------------------------")  
                croupier.distribue(1)
                #croupier.joueur.calcul_hand()
                print("la main du croupier est :", croupier.joueur.hand)
                print("--------------------------")  
                print("le score du croupier est de :", croupier.joueur.score)
                print("--------------------------")  
                
            while croupier.joueur.score != joueur.score:

                if croupier.joueur.score <= 21:
                    
                    var = {croupier.joueur.score: "le croupier", joueur.score:"le joueur"}
                    print("{} remporte la partie, avec un score de {}".format(var.get(max(var)),max(var)))
                    print("--------------------------")
                    choix_recommencer = input("voulez vous rejouer ?:")

                else:
                    var = {croupier.joueur.score: "le croupier", joueur.score:"le joueur"}
                    print("{} remporte la partie, avec un score de {}".format(var.get(min(var)),min(var)))
                    print("--------------------------")
                    choix_recommencer = input("voulez vous rejouer ?:")

            print("égalité")
            choix_recommencer = input("voulez vous rejouer ?:")
        while choix_carte_supp == "oui":

            croupier.distribue(1, joueur)
             
            print("la main du joueur est :", joueur.hand)
            print("le score du joueur est :", joueur.score)
            if joueur.score > 21:
                print("tu as perdu")
                choix_recommencer = input("voulez vous rejouer ?:")
                break
            else:
                choix_carte_supp =""
                while choix_carte_supp != "oui" and choix_carte_supp != "non":
                    choix_carte_supp = input("Recevoir une nouvelle carte ?:")
                if choix_carte_supp == "non":

                    print("la main du croupier est :", croupier.joueur.hand)
                    print("--------------------------")  
                    print("le score du croupier est de :", croupier.joueur.score)
                    print("--------------------------")  

                    while croupier.joueur.score < 17:
                        print("le croupier tire une nouvelle carte")
                        print("--------------------------")  
                        croupier.distribue(1)
                        #croupier.joueur.calcul_hand()
                        print("la main du croupier est :", croupier.joueur.hand)
                        print("--------------------------")  
                        print("le score du croupier est de :", croupier.joueur.score)
                        print("--------------------------")  
                        
                    
                    if croupier.joueur.score <= 21:
                        var = {croupier.joueur.score: "le croupier", joueur.score:"le joueur"}
                        print("{} remporte la partie, avec un score de {}".format(var.get(max(var)),max(var)))
                        print("--------------------------")
                        choix_recommencer = input("voulez vous rejouer ?:")

                    else:
                        var = {croupier.joueur.score: "le croupier", joueur.score:"le joueur"}
                        print("{} remporte la partie, avec un score de {}".format(var.get(min(var)),min(var)))
                        print("--------------------------")
                        choix_recommencer = input("voulez vous rejouer ?:")

    print("Merci et à bientot")                    

                                






       

                
