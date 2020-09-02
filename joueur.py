
class Joueur:
    def __init__(self):

        self.hand=[]
        self.score=0

    def calcul_hand(self) :
        for i in self.hand[0:]:
            
            if i[0] == 'valet' or i[0] == 'roi' or i[0] == 'dame':
                self.score += 10
            elif i[0] == 'as':
                choix = 0
                while choix !="1" and choix != "11" :
                    choix = input("choisir 1 ou 11: ")

                self.score += int(choix)
                
            else :
                self.score += int(i[0])

	