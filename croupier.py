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

    #choix_recommencer = "oui"
    #while choix_recommencer == "oui":
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
        joueur.calcul_hand(joueur)
        print("--------------------------")
        print("le score du joueur est :", joueur.score)
        croupier.joueur.calcul_hand()
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
                croupier.joueur.calcul_hand()
                print("la main du croupier est :", croupier.joueur.hand)
                print("--------------------------")  
                print("le score du croupier est de :", croupier.joueur.score)
                print("--------------------------")  
                
            
            if croupier.joueur.score <= 21:
                var = {croupier.joueur.score: "le croupier", joueur.score:"le joueur"}
                print("{} remporte la partie, avec un score de {}".format(var.get(max(var)),max(var)))
                print("--------------------------")  
            else:
                var = {croupier.joueur.score: "le croupier", joueur.score:"le joueur"}
                print("{} remporte la partie, avec un score de {}".format(var.get(min(var)),min(var)))
                print("--------------------------")  

        while choix_carte_supp == "oui":

            croupier.distribue(1, joueur)
            joueur.calcul_hand(joueur)
            print("la main du joueur est :", joueur.hand)
            print("le score du joueur est :", joueur.score)
            if joueur.score > 21:
                print("tu as perdu")
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
                        croupier.joueur.calcul_hand()
                        print("la main du croupier est :", croupier.joueur.hand)
                        print("--------------------------")  
                        print("le score du croupier est de :", croupier.joueur.score)
                        print("--------------------------")  
                        
                    
                    if croupier.joueur.score <= 21:
                        var = {croupier.joueur.score: "le croupier", joueur.score:"le joueur"}
                        print("{} remporte la partie, avec un score de {}".format(var.get(max(var)),max(var)))
                        print("--------------------------")  
                    else:
                        var = {croupier.joueur.score: "le croupier", joueur.score:"le joueur"}
                        print("{} remporte la partie, avec un score de {}".format(var.get(min(var)),min(var)))
                        print("--------------------------")

                        

                                






        #while choix_carte_supp == "oui" and joueur.score <=21:
         #   croupier.distribue(1, joueur)
          #  joueur.calcul_hand(joueur)
           # print("la nouvelle main du joueur est", joueur.hand)

                



'''
        choix_carte_supp =""
        while choix_carte_supp != "oui" and choix_carte_supp != "non":
            choix_carte_supp = input("le joueur veut continuer ?:")
            while choix_carte_supp == "oui" and joueur.score <= 21:
                croupier.distribue(1, joueur)
                joueur.calcul_hand()
                print("la nouvelle main du joueur est", joueur.hand)
                print("--------------------------")
                print("le nouveau score du joueur est", joueur.score)
                if joueur.score <= 21:
                    choix_carte_supp = input("le joueur veut continuer ?:")
            print(" Dommage, Vous avez dépassé 21!!")

                                                                                                                               
                print("on tire les mains du croupier pour comparer :")
            while croupier.joueur.score < 17:
                croupier.distribue(1)
                croupier.joueur.calcul_hand()
                print("la nouvelle main du croupier est :", croupier.joueur.hand)
                print("--------------------------")
                print("le score du croupier est :", croupier.joueur.score)
            if 17 <= croupier.joueur.score <= 21 :
                if joueur.score > croupier.joueur.score:
                    print("le joueur remporte la partie")
                elif joueur.score < croupier.joueur.score:
                    print("le croupier remporte la partie")
            else:
                print("le croupier à dépassé 21, le joueur remporte la partie")
            choix_recommencer = input("voulez vous rejouer ?:")
    print("Merci et à bientôt")
                # comparaison des mains..
     
        #choix_carte_supp = choix_carte_supp[0].lower()



        #print(croupier.joueur.score)
'''